import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="AivancityX Mobile Dashboard",
    page_icon="🎓",
    layout="centered"  # Centered layout feels more like a mobile app on desktop
)

# 2. Custom CSS to match the mobile styling and primary colors
st.markdown("""
    <style>
    /* Force main background */
    .stApp {
        background-color: #f6f6f8;
    }
    
    /* Header/Nav styling */
    header[data-testid="stHeader"] {
        background-color: white;
        border-bottom: 1px solid #e2e8f0;
    }
    
    /* Custom Metric Card (Mobile Optimized) */
    div[data-testid="stMetric"] {
        background-color: white;
        padding: 15px;
        border-radius: 16px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        border: 1px solid #f1f1f1;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: white;
        border-right: 1px solid #e2e8f0;
    }
    
    /* Style titles */
    h2 {
        font-weight: 800 !important;
        color: #1a1a2e;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Menu)
with st.sidebar:
    st.markdown("""
        <div style='display: flex; align-items: center; gap: 10px; margin-bottom: 20px;'>
            <div style='background-color: #1313ec; color: white; padding: 6px; border-radius: 8px;'>🎓</div>
            <h1 style='font-size: 20px; margin: 0;'>AivancityX</h1>
        </div>
    """, unsafe_allow_html=True)
    st.page_link("app.py", label="Dashboard", icon="📊")
    st.page_link("app.py", label="Students", icon="👥")
    st.page_link("app.py", label="Progress", icon="📈")
    st.page_link("app.py", label="Settings", icon="⚙️")
    st.divider()
    st.button("Log Out")

# 4. Mobile App Header
col_header_1, col_header_2 = st.columns([4, 1])
with col_header_1:
    st.title("Overview")
with col_header_2:
    st.image("https://ui-avatars.com/api/?name=Admin&background=1313ec&color=fff", width=40)

st.write("Welcome back, Administrator.")

# 5. Mobile Metric Grid (Vertical stacking for mobile feel)
st.metric(label="Total Students", value="1,240", delta="12%")
st.metric(label="Active Students", value="850", delta="5%")

# 6. Progress Section (Visual Bar Chart)
st.markdown("### Student Progress")
st.caption("Avg. completion by module")

# Dummy data for modules
progress_data = pd.DataFrame({
    "Module": ["M1", "M2", "M3", "M4", "M5"],
    "Progress": [45, 75, 60, 85, 30]
})

# Custom Chart with primary brand color
st.bar_chart(progress_data, x="Module", y="Progress", color="#1313ec")

# 7. Quick Actions (Common in mobile dashboards)
st.markdown("### Quick Actions")
q1, q2 = st.columns(2)
with q1:
    st.button("➕ Add Student", use_container_width=True)
with q2:
    st.button("📥 Export CSV", use_container_width=True)

# 8. Footer/Status
st.info("System status: All modules active.")
