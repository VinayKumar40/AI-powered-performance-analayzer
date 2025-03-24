import streamlit as st
# Set page config
st.set_page_config(page_title="System Analyzer", page_icon="🖥", layout="wide")

# Sidebar navigation
st.sidebar.title("🔍 Navigation")
selected_page = st.sidebar.radio("Select the page:", ["Home", "System Performance", "Gantt Chart", "AI Analyzer"])

# Display the selected page
if selected_page == "Home":
    st.title("🔹 System Analyzer Dashboard")
    st.write("Welcome! Use the sidebar to navigate.")
elif selected_page == "System Performance":
    from app1 import system_performance
    app2.system_performance()

elif selected_page == "Gantt Chart":
    from app4 import process_gantt_chart
    process_gantt_chart()

elif selected_page == "AI Analyzer":
    import app3
    from app3 import ai_system_performance_analyzer
    app3.ai_system_performance_analyzer()
