import matplotlib.pyplot as plt


def plot_skill_gap(resume_skills, job_skills):
    labels = list(set(job_skills))
    values = [1 if skill in resume_skills else 0 for skill in labels]
    
    plt.figure(figsize=(12,10))
    plt.bar(labels, values)
    plt.xticks(rotation=45)
    plt.title("Skill Match Graph")
    plt.savefig("static/skill_graph.png")