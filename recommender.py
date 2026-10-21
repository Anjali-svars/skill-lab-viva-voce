from career_data import CAREERS

def analyze_profile(name, selected_skills, target_role, experience="Beginner", interests=None):
    interests = interests or []
    target = CAREERS.get(target_role, CAREERS["Data Analyst"])
    selected = {s.lower() for s in selected_skills}
    required = {s.lower() for s in target["skills"]}
    matched = sorted(required & selected)
    missing = sorted(required - selected)
    score = round(len(matched) / len(required) * 100) if required else 0

    if score >= 80:
        level = "Placement-ready foundation"
        message = "You have a strong checklist match. Focus on projects, interview practice, and explaining your decisions."
    elif score >= 50:
        level = "Progressing well"
        message = "You have a useful base. Prioritize the highest-impact gaps and demonstrate them in one portfolio project."
    elif score >= 25:
        level = "Building foundations"
        message = "Choose two missing skills to learn first, then apply them in a small project."
    else:
        level = "Getting started"
        message = "Start with the fundamentals and build confidence through short, practical exercises."

    return {
        "name": name, "role": target_role, "career": target,
        "matched": matched, "missing": missing, "score": score,
        "level": level, "message": message, "experience": experience,
        "selected_count": len(selected_skills), "required_count": len(required),
        "confidence_note": "This is a transparent checklist match, not a validated hiring prediction."
    }

def build_learning_plan(missing, target_role):
    # Simple, explainable priority: recommend the first three gaps, plus a role-specific practice task.
    priorities = missing[:3]
    if not priorities:
        priorities = ["Portfolio project", "Interview practice", "Resume evidence"]
    plan = []
    for index, skill in enumerate(priorities, start=1):
        plan.append({
            "week": index,
            "title": f"Build {skill}" if skill not in ["Portfolio project", "Interview practice", "Resume evidence"] else skill,
            "task": f"Spend 3 short sessions learning and practising {skill.lower()}." if skill not in ["Portfolio project", "Interview practice", "Resume evidence"] else f"Create a small, demonstrable {skill.lower()} for {target_role}."
        })
    plan.append({"week": len(plan) + 1, "title": "Show your work", "task": "Publish your project, write a short README, and practise explaining what you built."})
    return plan

def recommend_roles(selected_skills, interests):
    selected = {s.lower() for s in selected_skills}
    interests = {s.lower() for s in interests}
    results = []
    for role, data in CAREERS.items():
        role_skills = {s.lower() for s in data["skills"]}
        skill_match = len(selected & role_skills) / len(role_skills) if role_skills else 0
        interest_match = len(interests & {i.lower() for i in data.get("interests", [])})
        # Interest match is a small bonus; skills remain the main factor.
        score = min(100, round(skill_match * 85 + interest_match * 5))
        results.append({"role": role, "percent": score, "matched": len(selected & role_skills), "total": len(role_skills), "summary": data["summary"]})
    results.sort(key=lambda item: item["percent"], reverse=True)
    return results[:3]
