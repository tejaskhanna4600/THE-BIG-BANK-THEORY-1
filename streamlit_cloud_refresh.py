"""
Streamlit Cloud Compatible Auto-Refresh Solution
"""
import streamlit as st
import time
from datetime import datetime

def add_streamlit_cloud_refresh():
    """Add refresh mechanism that works on Streamlit Cloud"""
    
    # Add a refresh button that's always visible
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("🔄 Refresh Game", key="refresh_game", use_container_width=True):
            st.rerun()
    
    with col2:
        # Show last update time
        current_time = datetime.now().strftime("%H:%M:%S")
        st.markdown(f"**Last update:** {current_time}")
    
    # Add JavaScript-based auto-refresh (works in some browsers)
    st.markdown("""
    <script>
    // Auto-refresh every 5 seconds
    setTimeout(function() {
        if (window.location.href.includes("share.streamlit.io")) {
            setTimeout(function() {
                window.location.reload();
            }, 5000);
        }
    }, 1000);
    </script>
    """, unsafe_allow_html=True)

def add_refresh_indicator():
    """Add visual indicator for refresh status"""
    st.markdown("---")
    st.markdown("### 🔄 Refresh Status")
    
    # Show current time
    current_time = datetime.now().strftime("%H:%M:%S")
    st.markdown(f"**Current Time:** {current_time}")
    
    # Instructions
    st.info("""
    **For Streamlit Cloud:**
    - Click "🔄 Refresh Game" button to see updates
    - Page will auto-refresh every 5 seconds (if browser supports it)
    - Manual refresh is most reliable
    """)

def create_refresh_placeholder():
    """Create a placeholder that updates to show activity"""
    placeholder = st.empty()
    
    # Update with current time
    current_time = datetime.now().strftime("%H:%M:%S")
    placeholder.markdown(f"🔄 **Last Activity:** {current_time}")
    
    return placeholder

