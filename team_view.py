"""
Team View - Interface for individual teams
"""
import streamlit as st
import random
from game_state import GameState
from config import CHANCE_QUESTIONS, MYSTERY_OPTIONS

def render_team_view(game_state: GameState, team_id: str):
    """Render the team's control panel"""
    
    team = game_state.get_team_by_id(team_id)
    if not team:
        st.error("Team not found!")
        return
    
    # Header
    st.title(f"🎮 {team.name} Control Panel")
    st.markdown(f"<div style='background-color: {team.color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 20px;'>"
                f"<h2>Balance: ₹{team.balance:,}</h2>"
                f"<p>Position: {team.position} | {game_state.properties[team.position].name}</p>"
                f"</div>", unsafe_allow_html=True)
    
    # Action buttons
    st.markdown("### Action Center")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🎲 Roll Dice", use_container_width=True, type="primary"):
            # Add action to queue
            game_state.add_action("roll_dice", team_id)
            st.success("✅ Dice roll request sent to admin! Waiting for approval...")
            st.rerun()
        
        if st.button("✅ End Turn", use_container_width=True):
            if game_state.get_current_team().team_id == team_id:
                game_state.add_action("end_turn", team_id)
                st.success("✅ Turn end request sent to admin!")
                st.rerun()
            else:
                st.warning("⚠️ It's not your turn yet!")
    
    with col2:
        if st.button("💰 Buy Property", use_container_width=True):
            prop = game_state.properties[team.position]
            if prop.owner is None and prop.price > 0:
                if team.balance >= prop.price:
                    game_state.add_action("buy_property", team_id, {"property_index": team.position})
                    st.success("✅ Buy property request sent to admin!")
                    st.rerun()
                else:
                    st.error("❌ Insufficient balance!")
            else:
                st.warning("⚠️ This property cannot be purchased!")
        
        if st.button("🏠 My Properties", use_container_width=True):
            st.info("Check 'Owned Properties' section below")
    
    # Current property info
    st.markdown("---")
    st.subheader("📍 Current Position")
    prop = game_state.properties[team.position]
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"**{prop.name}**")
        if prop.price > 0:
            st.markdown(f"- Price: ₹{prop.price:,}")
            st.markdown(f"- Rent: ₹{prop.rent:,}")
            if prop.owner:
                owner_team = game_state.get_team_by_id(prop.owner)
                st.markdown(f"- Owner: {owner_team.name if owner_team else 'Unknown'}")
        else:
            st.markdown(f"- Special: {prop.name}")
    
    # Owned properties
    st.markdown("---")
    st.subheader("🏠 Owned Properties")
    owned_props = [p for p in game_state.properties if p.owner == team_id]
    
    if owned_props:
        for prop in owned_props:
            refund = prop.price // 2
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{prop.name}** - Rent: ₹{prop.rent:,}")
            with col2:
                if st.button("Sell", key=f"sell_{prop.index}", use_container_width=True):
                    game_state.add_action("sell_property", team_id, {"property_index": prop.index})
                    st.success("✅ Sell request sent to admin!")
                    st.rerun()
    else:
        st.info("You don't own any properties yet")
    
    # Pending actions status
    st.markdown("---")
    pending_for_team = [a for a in game_state.get_pending_actions() if a.team_id == team_id]
    if pending_for_team:
        st.subheader("⏳ Pending Actions")
        for action in pending_for_team:
            status_icon = "⏳" if action.status == 'pending' else "✅" if action.status == 'approved' else "❌"
            st.markdown(f"{status_icon} {action.action_type} - {action.status}")
    
    # Current dice roll display
    if game_state.current_dice_roll > 0 and game_state.get_current_team().team_id == team_id:
        st.markdown("---")
        st.markdown(f"### 🎲 Dice Roll: {game_state.current_dice_roll}")

def handle_chance_button(game_state: GameState, team_id: str):
    """Handle chance card display"""
    if f'chance_show_{team_id}' not in st.session_state:
        st.session_state[f'chance_show_{team_id}'] = False
    
    # Show chance button if on chance tile
    team = game_state.get_team_by_id(team_id)
    if team.position in [4, 8, 16, 20]:  # CHANCE tiles
        if st.button("🎯 Chance Card", use_container_width=True):
            # Select a random chance question
            question = random.choice(CHANCE_QUESTIONS)
            st.session_state[f'chance_question_{team_id}'] = question
            st.session_state[f'chance_show_{team_id}'] = True
            st.rerun()
        
        # Show chance question if active
        if st.session_state.get(f'chance_show_{team_id}', False):
            question = st.session_state.get(f'chance_question_{team_id}')
            if question:
                render_chance_question(game_state, team_id, question)

def render_chance_question(game_state: GameState, team_id: str, question: dict):
    """Render chance question with options"""
    st.markdown("---")
    st.markdown("## 🎯 CHANCE CARD")
    st.markdown(f"### {question['question']}")
    
    cols = st.columns(2)
    for idx, option in enumerate(question['options']):
        label = ["A", "B", "C", "D"][idx]
        with cols[idx % 2]:
            if st.button(f"{label}. {option}", key=f"chance_{team_id}_{idx}", use_container_width=True):
                # Send answer to admin for approval
                game_state.add_action("chance_answer", team_id, {
                    "question": question['question'],
                    "answer": idx,
                    "correct": question['correct']
                })
                st.session_state[f'chance_show_{team_id}'] = False
                st.success("✅ Answer sent to admin!")
                st.rerun()

def handle_mystery_button(game_state: GameState, team_id: str):
    """Handle mystery wheel"""
    team = game_state.get_team_by_id(team_id)
    if team.position in [2, 10, 14, 22]:  # MYSTERY tiles
        if st.button("🎡 Spin Mystery Wheel", use_container_width=True):
            result = random.choice(MYSTERY_OPTIONS)
            game_state.add_action("spin_mystery", team_id, {"result": result})
            st.info(f"🎡 You got: **{result['text']}**")
            st.rerun()

