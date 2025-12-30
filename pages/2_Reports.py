
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("📊 Student Reports & Behavioral Timeline")

if "sessions" not in st.session_state or not st.session_state.sessions:
    st.warning("No session data available")
else:
    df = pd.DataFrame(st.session_state.sessions)
    st.dataframe(df, use_container_width=True)

    st.subheader("📈 Trust Score Trend")
    st.line_chart(df["Trust Score"])
