import streamlit as st

st.set_page_config(layout="wide")

if st.button("Dashboard Intro"):
    st.markdown(
        "<script>window.location.hash='dashboard';</script>",
        unsafe_allow_html=True
    )

with open("class_trial.html", "r", encoding="utf-8") as file:
    html_content = file.read()

st.markdown("<div id='dashboard'></div>", unsafe_allow_html=True)

st.components.v1.html(html_content, height=1200)
