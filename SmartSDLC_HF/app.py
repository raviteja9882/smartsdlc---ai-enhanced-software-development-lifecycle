import streamlit as st
from utils import extract_text_from_pdf, ask_ai

# Page settings
st.set_page_config(page_title="SmartSDLC", layout="centered")
st.title("SmartSDLC – Requirement Classifier")
st.write("Upload a PDF and let AI sort sentences by SDLC phase.")

# Upload button
pdf = st.file_uploader("Upload Requirements PDF", type="pdf")

if pdf:
    # Show a spinner while processing
    with st.spinner("Analyzing PDF..."):
        text = extract_text_from_pdf(pdf)

        prompt = f"""
You are an SDLC assistant.
Classify each sentence in this text into: Requirements, Design, Development, Testing, Deployment.
Group results under headings.

{text}
"""
        ai_output = ask_ai(prompt)

    st.success("Done! Here’s the result:")
    st.text_area("Classified Output", ai_output, height=400)