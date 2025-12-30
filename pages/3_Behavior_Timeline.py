import streamlit as st
import pandas as pd
import plotly.express as px

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
Visual analysis of student activity over time
</p>
<hr>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_excel("student_activity.xlsx")

df = load_data()

# ---------------- SIDEBAR ----------------
st.sidebar.header("🎯 Timeline Filters")

student_ids = df["student_id"].unique().tolist()
selected_student = st.sidebar.selectbox(
    "Select Student ID",
    student_ids
)

# Filter student data
student_df = df[df["student_id"] == selected_student]

# ---------------- METRICS ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("📌 Sessions", len(student_df))
col2.metric("⏱ Avg Session (min)", round(student_df["session_duration"].mean(), 2))
col3.metric("⚡ Avg Actions/min", round(student_df["actions_per_minute"].mean(), 2))
col4.metric("📂 Avg Files Accessed", round(student_df["files_accessed"].mean(), 2))

st.markdown("---")

# ---------------- LOGIN TIME TIMELINE ----------------
st.subheader("🕒 Login Time Distribution")

fig_login = px.scatter(
    student_df,
    x=student_df.index,
    y="login_hour",
    size="session_duration",
    color="day_type",
    labels={
        "login_hour": "Login Hour",
        "day_type": "Day Type (0=Weekday, 1=Weekend)",
        "index": "Session Index"
    },
    title="Login Time vs Sessions",
)

st.plotly_chart(fig_login, use_container_width=True)

# ---------------- SESSION DURATION ----------------
st.subheader("⏱ Session Duration Over Time")

fig_session = px.line(
    student_df,
    x=student_df.index,
    y="session_duration",
    markers=True,
    title="Session Duration Trend",
    labels={
        "session_duration": "Session Duration (minutes)",
        "index": "Session Index"
    }
)

st.plotly_chart(fig_session, use_container_width=True)

# ---------------- ACTION SPIKE ----------------
st.subheader("⚡ Actions Per Minute (Behavior Intensity)")

fig_actions = px.bar(
    student_df,
    x=student_df.index,
    y="actions_per_minute",
    title="Actions per Minute per Session",
    labels={
        "actions_per_minute": "Actions / Minute",
        "index": "Session Index"
    }
)

st.plotly_chart(fig_actions, use_container_width=True)

# ---------------- INTERPRETATION ----------------
st.markdown("---")
st.subheader("🧠 Behavioral Insights")

abnormal_logins = student_df[
    (student_df["login_hour"] < 5) | (student_df["login_hour"] > 22)
]

device_changes = student_df["device_change"].sum()

st.markdown(f"""
- 🔍 **Abnormal login times:** {len(abnormal_logins)}
- 🔁 **Device changes detected:** {device_changes}
- 📊 **High activity sessions:** {(student_df["actions_per_minute"] > 40).sum()}
""")

# ---------------- FOOTER ----------------
st.markdown("""
<hr>
<p style="text-align:center;color:gray;">
Student Behavior Risk System • AI Behavioral Analytics
</p>
""", unsafe_allow_html=True)

