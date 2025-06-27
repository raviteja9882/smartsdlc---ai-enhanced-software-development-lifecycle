import streamlit as st
from utils import summarize_code

st.set_page_config(page_title="Code Summarizer", layout="centered")
st.title("📘 SmartSDLC – Code Summarizer")

user_code = st.text_area("Paste your Python code to summarize:", height=250)

if st.button("Summarize Code"):
    if user_code.strip():
        with st.spinner("Summarizing..."):
            summary = summarize_code(user_code)
        st.success("Here's the AI-generated explanation:")
        st.write(summary)
    else:
        st.warning("Please enter your code first.")