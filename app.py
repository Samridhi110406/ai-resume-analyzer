import streamlit as st
import PyPDF2
import re

st.title("AI Resume Analyzer")

st.write("Upload your resume in PDF format")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

skills = [
    "python",
    "sql",
    "machine learning",
    "data analysis",
    "excel",
    "power bi",
    "tableau",
    "ai",
    "communication"
]

if uploaded_file is not None:

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    text = text.lower()

    st.subheader("Extracted Resume Text")
    st.write(text[:2000])

    st.subheader("Detected Skills")

    found_skills = []

    for skill in skills:
        if re.search(skill, text):
            found_skills.append(skill)

    if found_skills:
        for skill in found_skills:
            st.success(skill)

    else:
        st.error("No matching skills found")

    score = len(found_skills) / len(skills) * 100

    st.subheader("Resume Score")

    st.progress(int(score))
    
    st.write(f"Resume Match Score: {score:.2f}%")