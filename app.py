from flask import Flask, render_template, request, session, redirect, url_for
from career_data import SKILLS, CAREERS, LEARNING_RESOURCES
from recommender import analyze_profile, build_learning_plan, recommend_roles
from resume_parser import extract_resume_text, extract_resume_skills

app = Flask(__name__)
app.secret_key = "change-this-development-secret-key"

@app.route("/", methods=["GET", "POST"])
def index():
    report = None
    chosen_skills = []
    target_role = "Data Analyst"
    student_name = ""
    if request.method == "POST":
        student_name = request.form.get("student_name", "").strip() or "Student"
        target_role = request.form.get("target_role", "Data Analyst")
        chosen_skills = request.form.getlist("skills")
        experience = request.form.get("experience", "Beginner")
        interests = request.form.getlist("interests")
        report = analyze_profile(
            name=student_name, selected_skills=chosen_skills,
            target_role=target_role, experience=experience, interests=interests
        )
        report["learning_plan"] = build_learning_plan(report["missing"], target_role)
        report["resources"] = LEARNING_RESOURCES.get(target_role, [])
        report["roles"] = recommend_roles(chosen_skills, interests)
    return render_template("index.html", skills=SKILLS, careers=CAREERS,
                           report=report, chosen_skills=chosen_skills,
                           target_role=target_role, student_name=student_name)

@app.route("/api/health")
def health():
    return {"status": "ok", "app": "Career Readiness Platform"}

if __name__ == "__main__":
    app.run(debug=True)
