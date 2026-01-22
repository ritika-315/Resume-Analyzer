JOBS = {
"Software Engineer": ["python", "sql", "fastapi"],
"Data Analyst": ["python", "excel", "power bi"],
"ML Engineer": ["python", "ml", "pytorch"],
}


def recommend_job(resume_skills):
    scores = {}
    for job, skills in JOBS.items():
        match = len(set(skills) & set(resume_skills))
        scores[job] = match
    
    return max(scores, key=scores.get)
