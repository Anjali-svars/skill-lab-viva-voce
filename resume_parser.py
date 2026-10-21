import re

def extract_resume_text(file_storage):
    """Read a text-based .txt resume. PDF/DOCX parsing is intentionally not enabled in this starter."""
    if not file_storage or not file_storage.filename:
        return ""
    if not file_storage.filename.lower().endswith(".txt"):
        return ""
    try:
        return file_storage.read().decode("utf-8", errors="ignore")[:100000]
    except Exception:
        return ""

def extract_resume_skills(text, skill_catalog):
    text_lower = re.sub(r"[^a-z0-9+#. ]", " ", (text or "").lower())
    found = []
    for skill in skill_catalog:
        pattern = r"(?<![a-z0-9])" + re.escape(skill.lower()) + r"(?![a-z0-9])"
        if re.search(pattern, text_lower):
            found.append(skill)
    return found
