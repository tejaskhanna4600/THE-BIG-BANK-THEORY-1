"""
Arthvidya Monopoly - Multiplayer Streamlit App
Main entry point with authentication and routing
"""
import streamlit as st
from game_state import GameState
from config import PASSWORDS, USER_TYPES
from team_view import render_team_view
from admin_view import render_admin_view

def check_password():
    """Password-based authentication"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.user_type = None
    
    if not st.session_state.authenticated:
        # Login form
        st.title("🎲 Arthvidya Monopoly")
        st.markdown("---")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("### Login")
            user_type = st.selectbox(
                "Select your role:",
                options=list(USER_TYPES.keys()),
                format_func=lambda x: USER_TYPES[x]
            )
            password = st.text_input("Password:", type="password")
            
            if st.button("Login", use_container_width=True, type="primary"):
                if password == PASSWORDS.get(user_type):
                    st.session_state.authenticated = True
                    st.session_state.user_type = user_type
                    st.rerun()
                else:
                    st.error("❌ Incorrect password!")
        
        st.markdown("---")
        st.info("👥 Share this link with participants. Each team needs their password to access their panel.")
        
        return False
    
    return True

def main():
    st.set_page_config(
        page_title="Arthvidya Monopoly",
        layout="wide",
        page_icon="🎲",
        initial_sidebar_state="collapsed"
    )
    
    # Check authentication
    if not check_password():
        return
    
    # Hide default Streamlit elements
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    # Initialize or load game state
    if 'game_state' not in st.session_state:
        st.session_state.game_state = GameState()
        st.session_state.game_state.load()
        st.session_state.game_state.load_actions_queue()
    
    game_state = st.session_state.game_state
    user_type = st.session_state.user_type
    
    # Route to appropriate view
    if user_type == "ADMIN":
        render_admin_view(game_state)
    elif user_type in ["T1", "T2", "T3", "T4", "T5"]:
        render_team_view(game_state, user_type)
    else:
        st.error("Invalid user type")
    
    # Logout button
    with st.sidebar:
        if st.button("🚪 Logout", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

if __name__ == "__main__":
    main()

