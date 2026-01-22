import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

try:
    nlp = spacy.load("en_core_web_sm")
except:
    nlp = spacy.blank("en")

# Simple skill database (you can expand)
SKILL_DB = [
    "python","java","c++","sql","excel","power bi","tableau",
    "machine learning","deep learning","nlp","tensorflow","pytorch",
    "html","css","javascript","react","fastapi","flask","git","docker"
]

def extract_skills(text):
    text = text.lower()
    found_skills = [skill for skill in SKILL_DB if skill in text]
    return list(set(found_skills))

def match_resume_job(resume_text, job_text):
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume_text, job_text])
    
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    missing_skills = list(set(job_skills) - set(resume_skills))

    return {
        "score": round(similarity * 100, 2),
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "missing_skills": missing_skills
    }