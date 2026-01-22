from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(result):
    styles = getSampleStyleSheet()
    file_name = "static/resume_report.pdf"
    
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    content = []

    # Title
    content.append(Paragraph("Resume Match Report", styles["Heading1"]))
    content.append(Spacer(1, 12))

    # Score
    content.append(Paragraph(f"Match Score: {result.get('score','N/A')}%", styles["Normal"]))
    content.append(Spacer(1, 12))

    # Skills Found
    content.append(Paragraph("Skills Found:", styles["Heading2"]))
    for s in result.get("resume_skills", []):
        content.append(Paragraph(f"- {s}", styles["Normal"]))
    content.append(Spacer(1, 12))

    # Missing Skills
    content.append(Paragraph("Missing Skills:", styles["Heading2"]))
    for s in result.get("missing_skills", []):
        content.append(Paragraph(f"- {s}", styles["Normal"]))
    content.append(Spacer(1, 12))

    # AI Tips
    content.append(Paragraph("Resume Improvement Tips:", styles["Heading2"]))
    for tip in result.get("tips", []):
        content.append(Paragraph(f"- {tip}", styles["Normal"]))
    content.append(Spacer(1, 12))

    # Recommended Job
    content.append(Paragraph(f"Recommended Job Role: {result.get('recommended_job','N/A')}", styles["Normal"]))
    content.append(Spacer(1, 12))

    # Skill Graph Image
    try:
        graph = Image("static/skill_graph.png", width=400, height=250)
        content.append(Paragraph("Skill Match Graph:", styles["Heading2"]))
        content.append(graph)
    except:
        content.append(Paragraph("Skill graph not available.", styles["Normal"]))

    # Build PDF
    doc.build(content)
    return file_name
