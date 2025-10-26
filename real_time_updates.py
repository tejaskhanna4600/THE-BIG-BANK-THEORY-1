"""
Real-time Updates Solution for Streamlit Cloud
"""
import streamlit as st
import time
from datetime import datetime

def add_real_time_indicator():
    """Add a visual indicator that shows the app is live"""
    st.markdown("---")
    
    # Show current time
    current_time = datetime.now().strftime("%H:%M:%S")
    
    # Create columns for status
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown(f"**🕐 {current_time}**")
    
    with col2:
        st.markdown("**🟢 LIVE**")
    
    with col3:
        # Show a pulsing dot to indicate activity
        st.markdown("**●**")

def add_action_feedback():
    """Add feedback for actions"""
    if 'action_feedback' in st.session_state:
        feedback = st.session_state.action_feedback
        if feedback:
            st.success(feedback)
            # Clear feedback after showing
            st.session_state.action_feedback = None

def set_action_feedback(message):
    """Set feedback message for next display"""
    st.session_state.action_feedback = message

def add_auto_refresh_meta():
    """Add meta refresh tag for browsers that support it"""
    st.markdown("""
    <head>
        <meta http-equiv="refresh" content="10">
    </head>
    """, unsafe_allow_html=True)

def create_live_status():
    """Create a live status indicator"""
    placeholder = st.empty()
    
    # Update placeholder with current time
    current_time = datetime.now().strftime("%H:%M:%S")
    placeholder.markdown(f"🕐 **Live Status:** {current_time}")
    
    return placeholder

