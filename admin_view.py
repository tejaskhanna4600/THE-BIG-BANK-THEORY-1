"""
Admin View - Control panel for game administrator
"""
import streamlit as st
import random
from game_state import GameState
from config import CHANCE_QUESTIONS, MYSTERY_OPTIONS

def render_admin_view(game_state: GameState):
    """Render the admin control panel"""
    
    st.title("🏦 Admin Control Panel")
    
    # Game controls
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("▶️ Start Game", use_container_width=True, type="primary"):
            game_state.game_started = True
            game_state.save()
            st.success("Game started!")
        
        if st.button("🔄 Reset Game", use_container_width=True):
            game_state.current_team_idx = 0
            for team in game_state.teams:
                team.balance = 10_000_000
                team.position = 0
            for prop in game_state.properties:
                prop.owner = None
            game_state.actions_queue = []
            game_state.save()
            st.success("Game reset!")
    
    with col2:
        if st.button("📊 Show All Teams", use_container_width=True):
            st.session_state['show_all_teams'] = True
    
    with col3:
        if st.button("💾 Save Game State", use_container_width=True):
            game_state.save()
            st.success("Game state saved!")
    
    # Current team display
    current_team = game_state.get_current_team()
    st.markdown("---")
    st.markdown(f"<div style='background-color: {current_team.color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 20px;'>"
                f"<h2>Current Turn: {current_team.name}</h2>"
                f"<p>Balance: ₹{current_team.balance:,} | Position: {current_team.position}</p>"
                f"</div>", unsafe_allow_html=True)
    
    # Pending actions queue
    st.markdown("---")
    st.subheader("⏳ Pending Action Requests")
    
    pending_actions = game_state.get_pending_actions()
    
    if pending_actions:
        for action in pending_actions:
            team = game_state.get_team_by_id(action.team_id)
            if not team:
                continue
            
            with st.container():
                st.markdown(f"### {team.name} - {action.action_type}")
                st.markdown(f"**Parameters:** {action.params}")
                st.markdown(f"*Requested at: {action.timestamp}*")
                
                col1, col2, col3 = st.columns([1, 1, 2])
                
                with col1:
                    if st.button("✅ Approve", key=f"approve_{action.action_id}", use_container_width=True):
                        approved_action = game_state.approve_action(action.action_id)
                        if approved_action:
                            execute_action(game_state, approved_action)
                            st.success("Action approved and executed!")
                
                with col2:
                    if st.button("❌ Reject", key=f"reject_{action.action_id}", use_container_width=True):
                        game_state.reject_action(action.action_id)
                        st.warning("Action rejected!")
                
                with col3:
                    # Show context
                    if action.action_type == "chance_answer":
                        question = action.params.get('question', '')
                        answer_idx = action.params.get('answer', 0)
                        correct_idx = action.params.get('correct', 0)
                        is_correct = answer_idx == correct_idx
                        st.markdown(f"**Correct:** {is_correct}")
                
                st.markdown("---")
    else:
        st.info("No pending actions")
    
    # All teams status
    st.markdown("---")
    st.subheader("👥 All Teams Status")
    
    cols = st.columns(5)
    for idx, team in enumerate(game_state.teams):
        with cols[idx]:
            st.markdown(f"<div style='border: 2px solid {team.color}; padding: 10px; border-radius: 5px;'>"
                       f"<h4>{team.name}</h4>"
                       f"<p>₹{team.balance:,}</p>"
                       f"<p>Pos: {team.position}</p>"
                       f"</div>", unsafe_allow_html=True)
    
    # Manual controls for admin
    st.markdown("---")
    with st.expander("🔧 Manual Controls"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Manual Move**")
            team_select = st.selectbox("Team:", options=[t.team_id for t in game_state.teams])
            new_pos = st.number_input("New Position:", min_value=0, max_value=23, value=0)
            if st.button("Move Team"):
                team = game_state.get_team_by_id(team_select)
                team.position = new_pos
                game_state.save()
                st.success(f"Moved to position {new_pos}")
        
        with col2:
            st.markdown("**Adjust Balance**")
            team_select2 = st.selectbox("Team:", options=[t.team_id for t in game_state.teams], key="team_select2")
            amount = st.number_input("Amount (can be negative):", value=0)
            if st.button("Adjust Balance"):
                team = game_state.get_team_by_id(team_select2)
                team.balance += amount
                game_state.save()
                st.success(f"Balance adjusted by ₹{amount:,}")

def execute_action(game_state: GameState, action):
    """Execute an approved action"""
    team = game_state.get_team_by_id(action.team_id)
    if not team:
        return
    
    if action.action_type == "roll_dice":
        # Roll dice and move
        dice = random.randint(1, 6)
        game_state.current_dice_roll = dice
        
        # Move player
        new_pos = (team.position + dice) % 24
        
        # Check if passed GO
        if team.position + dice >= 24:
            team.balance += 2_000_000
        
        team.position = new_pos
        game_state.save()
    
    elif action.action_type == "buy_property":
        prop_index = action.params.get('property_index')
        prop = game_state.properties[prop_index]
        
        if prop.owner is None and team.balance >= prop.price:
            team.balance -= prop.price
            prop.owner = team.team_id
            game_state.save()
    
    elif action.action_type == "sell_property":
        prop_index = action.params.get('property_index')
        prop = game_state.properties[prop_index]
        
        if prop.owner == team.team_id:
            refund = prop.price // 2
            team.balance += refund
            prop.owner = None
            game_state.save()
    
    elif action.action_type == "end_turn":
        game_state.current_team_idx = (game_state.current_team_idx + 1) % len(game_state.teams)
        game_state.current_dice_roll = 0
        game_state.save()
    
    elif action.action_type == "chance_answer":
        answer_idx = action.params.get('answer')
        correct_idx = action.params.get('correct')
        
        if answer_idx == correct_idx:
            bonus = random.randint(500_000, 2_000_000)
            team.balance += bonus
        game_state.save()
    
    elif action.action_type == "spin_mystery":
        result = action.params.get('result')
        if result['action'] == "move":
            team.position = (team.position + result['value']) % 24
        elif result['action'] == "goto":
            team.position = result['value']
        game_state.save()
    
    # Re-approve action after execution
    game_state.approve_action(action.action_id)

