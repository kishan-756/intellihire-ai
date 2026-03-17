import ollama
import json
import re

def generate_interview_questions(missing_skills):

    skills = ", ".join(missing_skills)

    prompt = f"""
Generate a mock interview in JSON format.

Structure:

{{
"aptitude": [{{"question": "", "options": [], "answer": ""}}],
"dsa": [{{"question": "", "reference_answer": ""}}],
"technical": [{{"question": "", "reference_answer": ""}}],
"hr": [{{"question": "", "reference_answer": ""}}]
}}

Rules:
- 5 aptitude MCQ
- 1 DSA coding question
- 2 technical questions about {skills}
- 1 HR question

Return ONLY JSON.
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role":"user","content":prompt}]
    )

    content = response["message"]["content"]

    json_text = re.search(r'\{.*\}', content, re.S).group()

    return json.loads(json_text)