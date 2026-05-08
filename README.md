# AI Resume Analyzer
A simple AI-based resume analyzer built using Python and Streamlit that scans resumes in PDF format and identifies important technical skills.

## Project Overview
This project helps users analyze resumes by extracting text from PDF files and matching skills with predefined keywords.
The application calculates a resume match score based on detected skills and displays the result visually

## Features
- Upload resume in PDF format
- Extract text from resumes
- Detect technical skills automatically
- Display matched skills
- Generate resume match score
- Interactive web interface using Streamlit

## Technologies Used
- Python 
- Streamlit
- PyPDF2
- Regular Expressions (re)
- NLP-based keyword matching

## Skills Detected 
The project currently checks for skills such as:
- Python
- SQL
- Machine Learning
- Data Analysis
- Excel
- Power BI
- Tableau
- AI
- Communication

## How to Run
1. Clone the repository
2. Open terminal in project folder
3. Install required libraries
```bash
pip install streamlit pandas PyPDF2 scikit-learn nltk
```
4. Run the application
```bash
streamlit run app.py
```
