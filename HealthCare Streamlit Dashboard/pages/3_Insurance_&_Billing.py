import streamlit as st
from utils import initialize_page, load_data, create_sidebar, create_page_navigation

# Initialize page
initialize_page()

try:
    # Load data
    df = load_data()
    
    # Create sidebar
    current_start, current_end, prev_start, prev_end, comparison_label, filtered_df = create_sidebar(df)
    
    st.session_state['current_page'] = 'Insurance & Billing'
    
    # Create navigation
    create_page_navigation()
    
    # Page content
    st.header('Insurance & Billing')
    st.info("Insurance & Billing content is under development")

except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()