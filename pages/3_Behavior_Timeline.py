import streamlit as st
import pandas as pd
import plotly.express as px

# ================= ML LOGIC IMPORT =================
from logic.anomaly_detector import detect_anomaly
from logic.spike_detector import detect_activity_spike
from logic.risk_explainer import explain_risk
from logic.timeline_builder import build_timeline

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Behavior Timeline",
    page_icon="📈",
    layout="wide"
)

# ---------------- TITLE ----------------
st.markdown("""
<h1 style="text-align:center;">📈 Student Behavior Timeline</h1>
<p style="text-align:center;color:gray;">
Visual & AI-driven analysis of student activity over time
</p>
<hr>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_excel("student_activity.xlsx")

df = load_data()

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("🎯 Timeline Filters")
student_ids = df["student_id"].unique().tolist()
selected_student = st.sidebar.selectbox("Select Student ID", student_ids)

# Filter data for the selected student
student_df = df[df["student_id"] == selected_student]

# ---------------- METRICS ----------------
col1, col2, col3, col4 = st.columns(4)
col1.metric("📌 Sessions", len(student_df))
col2.metric("⏱ Avg Session (min)", round(student_df["session_duration"].mean(), 2))
col3.metric("⚡ Avg Actions/min", round(student_df["actions_per_minute"].mean(), 2))
col4.metric("📂 Avg Files Accessed", round(student_df["files_accessed"].mean(), 2))

st.markdown("---")

# ================= BEHAVIOR TIMELINE =================
st.subheader("🕒 Login & Session Timeline")
timeline_df = build_timeline(student_df)  # ML logic to build enriched timeline

fig_timeline = px.scatter(
    timeline_df,
    x="session_index",
    y="login_hour",
    size="session_duration",
    color="risk_level",
    hover_data=["actions_per_minute", "files_accessed", "device_change", "anomaly_score"],
    labels={"login_hour": "Login Hour", "session_index": "Session Index"},
    title="Login Time vs Sessions with Risk Highlight"
)
st.plotly_chart(fig_timeline, use_container_width=True)

# ---------------- SESSION DURATION TREND ----------------
st.subheader("⏱ Session Duration Over Time")
fig_session = px.line(
    timeline_df,
    x="session_index",
    y="session_duration",
    markers=True,
    title="Session Duration Trend",
    labels={"session_duration": "Session Duration (minutes)", "session_index": "Session Index"}
)
st.plotly_chart(fig_session, use_container_width=True)

# ---------------- ACTION SPIKE DETECTION ----------------
st.subheader("⚡ Actions Per Minute (Behavior Intensity)")
timeline_df["spike"] = timeline_df.apply(detect_activity_spike, axis=1)

fig_actions = px.bar(
    timeline_df,
    x="session_index",
    y="actions_per_minute",
    color="spike",
    title="Actions per Minute with Spikes Highlighted",
    labels={"actions_per_minute": "Actions / Minute", "session_index": "Session Index"}
)
st.plotly_chart(fig_actions, use_container_width=True)

# ---------------- RISK ANALYSIS ----------------
st.markdown("---")
st.subheader("🧠 Behavioral Insights & Risk Explanation")

# Detect anomalies
timeline_df["anomaly_score"] = timeline_df.apply(detect_anomaly, axis=1)
timeline_df["risk_reason"] = timeline_df.apply(explain_risk, axis=1)

abnormal_logins = timeline_df[(timeline_df["login_hour"] < 5) | (timeline_df["login_hour"] > 22)]
device_changes = timeline_df["device_change"].sum()
high_activity_sessions = (timeline_df["actions_per_minute"] > 40).sum()
anomalous_sessions = (timeline_df["anomaly_score"] > 0).sum()

st.markdown(f"""
- 🔍 **Abnormal login times:** {len(abnormal_logins)}
- 🔁 **Device changes detected:** {device_changes}
- ⚡ **High activity sessions (>40 actions/min):** {high_activity_sessions}
- ⚠️ **Anomalous sessions detected:** {anomalous_sessions}
""")

# Show risk reasons table
st.subheader("📝 Explainable Risk Reasons")
st.dataframe(
    timeline_df[["session_index", "anomaly_score", "risk_reason"]],
    use_container_width=True
)

# ---------------- FOOTER ----------------
st.markdown("""
<hr>
<p style="text-align:center;color:gray;">
Student Behavior Risk System • AI Behavioral Analytics
</p>
""", unsafe_allow_html=True)
