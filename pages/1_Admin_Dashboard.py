import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("🛡 Admin Dashboard")

if "sessions" not in st.session_state or not st.session_state.sessions:
    st.warning("No data available")
else:
    df = pd.DataFrame(st.session_state.sessions)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sessions", len(df))
    col2.metric("Suspicious Sessions", len(df[df["Status"] == "Suspicious"]))
    col3.metric("Trusted Sessions", len(df[df["Status"] == "Trusted"]))

    st.subheader("⚠ High Risk Students")
    st.dataframe(df[df["Status"] == "Suspicious"], use_container_width=True)

