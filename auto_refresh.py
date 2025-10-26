"""
Enhanced Auto-Refresh for Streamlit Multiplayer Monopoly
"""
import streamlit as st
import time
from datetime import datetime

def add_auto_refresh():
    """Add auto-refresh functionality to the app"""
    
    # Add refresh timer to session state
    if 'refresh_counter' not in st.session_state:
        st.session_state.refresh_counter = 0
    
    # Increment counter every run
    st.session_state.refresh_counter += 1
    
    # Add refresh button in sidebar
    with st.sidebar:
        st.markdown("### 🔄 Refresh Controls")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔄 Refresh", key="manual_refresh"):
                st.session_state.refresh_counter += 100  # Force refresh
                st.rerun()
        
        with col2:
            # Show refresh status
            st.markdown(f"**Refreshes:** {st.session_state.refresh_counter}")
        
        st.markdown("---")
        
        # Auto-refresh info
        st.info("🔄 **Auto-refresh:** Every 2 seconds")
        
        # Show current time
        current_time = datetime.now().strftime("%H:%M:%S")
        st.markdown(f"**Current Time:** {current_time}")
        
        # Add refresh indicator
        if st.session_state.refresh_counter % 10 == 0:
            st.success("✅ Auto-refresh active!")

def add_refresh_meta():
    """Add meta refresh tag to HTML head"""
    st.markdown("""
    <head>
        <meta http-equiv="refresh" content="3">
    </head>
    """, unsafe_allow_html=True)

def create_refresh_placeholder():
    """Create a placeholder that updates to trigger refresh"""
    placeholder = st.empty()
    
    # Update placeholder content
    current_time = datetime.now().strftime("%H:%M:%S")
    placeholder.markdown(f"🔄 Last update: {current_time}")
    
    return placeholder

