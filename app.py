import os
from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import shutil

from resume_parser import extract_text_from_pdf
from skill_matcher import match_resume_job
from skill_graph import plot_skill_gap
from ai_tips import generate_tips
from job_recommender import recommend_job
from report_generator import generate_pdf_report


app = FastAPI()

# Create uploads folder automatically
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")

# Home Page
@app.get("/", response_class=HTMLResponse)
async def home():
    with open("templates/index.html") as f:
        return f.read()

# Analyze Resume
@app.post("/analyze")
async def analyze_resume(file: UploadFile, job_description: str = Form(...)):

    # Save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract resume text
    resume_text = extract_text_from_pdf(file_path)

    # Match resume with job description
    result = match_resume_job(resume_text, job_description)

    # Skill Graph
    plot_skill_gap(result["resume_skills"], result["job_skills"])

    # AI Tips
    result["tips"] = generate_tips(result["missing_skills"])


    # Job Recommendation
    result["recommended_job"] = recommend_job(result["resume_skills"])

    pdf_path = generate_pdf_report(result)
    result["pdf_report"] = pdf_path

    return result
