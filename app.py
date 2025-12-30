import streamlit as st

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Student Behavior Risk System",
    page_icon="🎓",
    layout="wide"
)

# ================= SIDEBAR NAVIGATION =================
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio(
    "Go to",
    ("🏠 Home", "📡 Live Monitoring", "📊 Reports", "📈 Behavior Timeline")
)

# ================= HOME PAGE =================
if page == "🏠 Home":
    st.markdown("""
    <div style="text-align:center;padding:40px;background:linear-gradient(90deg,#0f172a,#1e3a8a);border-radius:12px;color:white;">
        <h1>🎓 Student Behavior Risk System</h1>
        <p>AI-based Behavioral Monitoring & Cyber-Aware Analytics</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="display:flex;justify-content:space-around;margin-top:30px;">
        <div style="background:#f2f2f2;padding:20px;border-radius:12px;width:30%;text-align:center;">
            <h2>📡 Live Monitoring</h2>
            <p>Real-time student behavior analysis</p>
        </div>
        <div style="background:#f2f2f2;padding:20px;border-radius:12px;width:30%;text-align:center;">
            <h2>📊 Reports</h2>
            <p>Entry & trust score reports</p>
        </div>
        <div style="background:#f2f2f2;padding:20px;border-radius:12px;width:30%;text-align:center;">
            <h2>📈 Behavior Timeline</h2>
            <p>Visual & AI-driven student activity analysis</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================= LIVE MONITORING PAGE =================
elif page == "📡 Live Monitoring":
    from pages import 1_Live_Monitor
    1_Live_Monitor.main()  # assuming your 1_Live_Monitor.py has a main() function

# ================= REPORTS PAGE =================
elif page == "📊 Reports":
    from pages import 2_Reports
    2_Reports.main()  # assuming your 2_Reports.py has a main() function

# ================= BEHAVIOR TIMELINE PAGE =================
elif page == "📈 Behavior Timeline":
    from pages import 3_Behavior_Timeline
    3_Behavior_Timeline.main()  # assuming your 3_Behavior_Timeline.py has a main() function

# ================= FOOTER =================
st.markdown("""
<hr>
<p style="text-align:center;color:gray;">
© 2025 Student Behavior Risk System | AI Behavioral Analytics
</p>
""", unsafe_allow_html=True)

