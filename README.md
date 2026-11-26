# 💼 AI-Powered Smart Resume Screener & ATS Optimizer

An intelligent, web-based software application designed to parse candidate resumes, cross-reference them with target job descriptions, and generate accurate ATS matching scores alongside constructive resume upgrade suggestions.

## 🚀 Key Features
* **Automated PDF Parsing**: Extracts text cleanly from multi-page document layouts using PyPDF2.
* **AI Evaluation Engine**: Harnesses the `gemini-3.5-flash-lite` model via the official `google-genai` SDK to process contextual keyword matching.
* **Direct Insights**: Displays an overall matching score, identifies critical missing keywords, and outlines explicit layout improvements.

## 🛠️ Tech Stack
* **Language**: Python
* **Web UI Framework**: Streamlit
* **AI API Integration**: Google GenAI SDK (Gemini Core Ecosystem)
* **Document Processing**: PyPDF2

## 📦 How to Run Locally

1. **Clone this repository to your machine:**
   ```bash
   git clone https://github.com
   cd AI-Resume-Screener
   ```

2. **Install all project dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your API Key environment variable:**
   Create a `.env` file in the root directory and add your key:
   ```env
   GEMINI_API_KEY=your_key_here
   ```

4. **Launch the web application:**
   ```bash
   streamlit run app.py
   ```
