import streamlit as st
import pandas as pd

# --- PAGE SETUP ---
st.set_page_config(page_title="AivancityX Admin", layout="wide")

# --- CUSTOM BRANDING (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #f6f6f8; }
    div[data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #e2e8f0;
        padding: 15px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🎓 AivancityX")
    st.selectbox("Main Menu", ["Dashboard", "Students", "Progress", "Settings"])
    st.divider()
    if st.button("Log Out"):
        st.info("Logging out...")

# --- HEADER ---
st.header("Dashboard Overview")
st.caption("Welcome back, Administrator.")

# --- KPI METRICS (The 4 Cards) ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Students", "1,240", "+12%")
col2.metric("Active Students", "850", "+5%")
col3.metric("Completion Rate", "68%", "+2%")
col4.metric("Certifications", "412", "+8%")

st.write("##") # Spacer

# --- CHARTS SECTION ---
c1, c2 = st.columns([2, 1])

with c1:
    st.subheader("Student Progress by Module")
    chart_data = pd.DataFrame({
        "Module": ["Mod 1", "Mod 2", "Mod 3", "Mod 4", "Mod 5"],
        "Progress": [45, 75, 60, 85, 30]
    })
    st.bar_chart(chart_data, x="Module", y="Progress", color="#1313ec")

with c2:
    st.subheader("Course Status")
    status_data = pd.DataFrame({
        "Status": ["Completed", "In-Progress", "Pending"],
        "Value": [65, 25, 10]
    })
    st.dataframe(status_data, hide_index=True, use_container_width=True)

# --- STUDENT TABLE ---
st.subheader("Student Overview")

# Sample Data
students = pd.DataFrame([
    {"Name": "John Doe", "Program": "Data Science MSc", "Progress": 85, "Status": "Active"},
    {"Name": "Alice Smith", "Program": "AI Ethics", "Progress": 100, "Status": "Completed"},
    {"Name": "Robert Johnson", "Program": "Machine Learning", "Progress": 45, "Status": "Pending"},
    {"Name": "Emma Lee", "Program": "Data Science MSc", "Progress": 92, "Status": "Active"},
])

# Interactive Table with Progress Bars
st.data_editor(
    students,
    column_config={
        "Progress": st.column_config.ProgressColumn(
            "Progress", min_value=0, max_value=100, format="%d%%"
        ),
        "Status": st.column_config.SelectboxColumn(
            "Status", options=["Active", "Completed", "Pending"]
        ),
    },
    use_container_width=True,
    hide_index=True
)
