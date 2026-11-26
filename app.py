import streamlit as st
from google import genai
import PyPDF2 as pdf
from dotenv import load_dotenv
import os

# Securely load environmental keys
load_dotenv()

# Initialize the new official Google GenAI Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def extract_text_from_pdf(uploaded_file):
    """Extracts raw text data from multi-page PDF records cleanly."""
    reader = pdf.PdfReader(uploaded_file)
    extracted_text = ""
    for page in range(len(reader.pages)):
        current_page = reader.pages[page]
        extracted_text += str(current_page.extract_text())
    return extracted_text

def get_gemini_analysis(resume_text, job_description):
    """Queries active Gemini endpoints using structured contextual matching."""
    
    prompt = f"""
    You are an expert HR Manager and Application Tracking System (ATS) evaluator. 
    Analyze the candidate's Resume against the provided Job Description.
    
    Resume Text:
    {resume_text}
    
    Job Description:
    {job_description}
    
    Provide your evaluation in this strict layout structure:
    ### 📊 ATS Match Score
    [Give a clear percentage out of 100%]
    
    ### 🔍 Summary Analysis
    [Brief summary of overall profile alignment]
    
    ### ❌ Missing Critical Keywords
    * [Keyword 1]
    * [Keyword 2]
    
    ### 🚀 Actionable Recommendations
    * [Tips to upgrade the resume phrasing or content]
    """
    
    # We target gemini-2.5-flash via the active contents generation service layer
    response = client.models.generate_content(
        model='gemini-3.5-flash',
        contents=prompt,
    )
    return response.text

# --- Presentation User Interface UI Layer ---
st.set_page_config(page_title="AI Resume Screener", page_icon="💼")
st.title("💼 AI Smart Resume Screener & ATS Optimizer")

job_desc_input = st.text_area("📋 Paste the Job Description here:", height=200)
uploaded_resume = st.file_uploader("📤 Upload Resume (PDF only):", type=["pdf"])

if st.button("🚀 Analyze Resume & Calculate Score"):
    if not job_desc_input:
        st.warning("Please paste a job description first!")
    elif not uploaded_resume:
        st.warning("Please upload your resume PDF!")
    else:
        with st.spinner("Analyzing profile requirements against AI endpoints..."):
            try:
                text_data = extract_text_from_pdf(uploaded_resume)
                ai_result = get_gemini_analysis(text_data, job_desc_input)
                st.success("Analysis Complete!")
                st.markdown(ai_result)
            except Exception as e:
                st.error(f"Error processing application: {e}")
