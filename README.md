# AI-powered Career Readiness and Skill Gap Intelligence Platform — Advanced Starter

A more advanced student-placement web prototype built with Python and Flask.

## Features
- Modern responsive dashboard
- Skill checklist and target career selection
- Explainable readiness score with four progress levels
- Skills matched and missing-skill breakdown
- Interest-based career suggestions with a small, explainable bonus
- Week-by-week learning plan
- Role-specific project ideas and curated learning links
- Optional `.txt` resume skill extraction helper
- Basic health endpoint at `/api/health`

## Run in VS Code (Windows)
1. Extract the ZIP.
2. Open the extracted folder in Visual Studio Code.
3. In the terminal run:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   python app.py
   ```
4. Open `http://127.0.0.1:5000`.

If `python` is not recognized, install Python 3 from python.org and enable **Add Python to PATH** during installation.

## How to demo
1. Enter a student name and select a target role.
2. Select skills and interests.
3. Submit to see the readiness match, skill gaps, role suggestions, and weekly plan.
4. Open `/api/health` to show a simple backend health endpoint.

## Project structure
- `app.py` — Flask routes and page handling
- `career_data.py` — role profiles, skill requirements, learning links
- `recommender.py` — transparent scoring and recommendation logic
- `resume_parser.py` — optional plain-text resume skill extraction helper
- `templates/index.html` — website interface
- `static/style.css` — styling

## Honest limitations
This starter does not call an external AI model or train a machine-learning model. It uses rule-based, explainable matching so it works offline after installing Flask. The included resume helper only extracts text from `.txt` files and is not connected to the main page yet. Do not upload private or sensitive resumes to a public deployment. To make this production-ready, add authentication, persistent storage, validated PDF/DOCX parsing, privacy controls, tests, and an AI service only if you have a suitable API key and consent flow.
