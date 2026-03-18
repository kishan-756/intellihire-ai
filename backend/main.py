from fastapi import FastAPI, UploadFile, File, Form, Request, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from typing import List
from pydantic import BaseModel

from database import engine, SessionLocal
from models import Base, InterviewResult

import subprocess
import tempfile
import random
import json
import ollama
import pypdf
import docx
import io

from auth import create_token, verify_token
from ai_feedback import analyze_performance

from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware

from dotenv import load_dotenv
import os

from fastapi.staticfiles import StaticFiles


load_dotenv()

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")


app = FastAPI()
import os
from fastapi.responses import RedirectResponse

@app.get("/")
def root():
    return RedirectResponse(url="/frontend/login.html")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app.mount(
    "/frontend",
    StaticFiles(directory=os.path.join(BASE_DIR, "frontend")),
    name="frontend"
)
#from starlette.middleware.sessions import SessionMiddleware

app.add_middleware(
    SessionMiddleware,
    secret_key="super_secret_session_key",
    same_site="lax",
    https_only=False
)

Base.metadata.create_all(bind=engine)


# ---------------- Middleware ----------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# REQUIRED for Google OAuth
#app.add_middleware(SessionMiddleware, secret_key="intellihire_secret")


# ---------------- Google OAuth ----------------

oauth = OAuth()

oauth.register(
    name="google",
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

# ---------------- Resume Skill DB ----------------

skills_db = [
    "python",
    "java",
    "sql",
    "docker",
    "kubernetes",
    "react",
    "node",
    "data structures",
    "algorithms"
]


def extract_skills(text):

    text = text.lower()

    found = []

    for s in skills_db:
        if s in text:
            found.append(s)

    return found


# ---------------- Resume Upload ----------------

@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...), job_description: str = Form(...)):

    content = await file.read()
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        pdf_reader = pypdf.PdfReader(io.BytesIO(content))
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        text = text.lower()
    elif filename.endswith(".docx"):
        doc = docx.Document(io.BytesIO(content))
        text = "\n".join([para.text for para in doc.paragraphs]).lower()
    else:
        text = content.decode(errors="ignore").lower()

    resume_skills = extract_skills(text)

    job_skills_raw = job_description.split(",")

    strong = []
    missing = []

    for s in job_skills_raw:

        s = s.strip()
        if not s:
            continue

        if s.lower() in text:
            strong.append(s)

        else:
            missing.append(s)

    return {
        "resume_skills": resume_skills,
        "strong_skills": strong,
        "missing_skills": missing
    }


# ---------------- Interview Generator ----------------

def generate_interview(missing_skills, job_role):

    prompt = f"""
Generate interview questions for a {job_role} role.

Weak skills: {missing_skills}

Return JSON with:

aptitude: 20 MCQ
dsa: 3 coding questions (easy, medium, hard)
technical: 5 questions
hr: 3 questions
"""

    try:

        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )

        text = response["message"]["content"]

        interview = json.loads(text)

        return interview

    except Exception as e:
        print(f"Ollama generation failed: {e}. Using intelligent fallback.")
        
        try:
            db_path = os.path.join(BASE_DIR, "backend", "questions.json")
            with open(db_path, "r") as f:
                q_db = json.load(f)

            apt_pool = q_db.get("aptitude", [])
            aptitude = random.sample(apt_pool, min(20, len(apt_pool)))

            dsa_pool = q_db.get("dsa", [])
            dsa = []
            for diff in ["easy", "medium", "hard"]:
                items = [q for q in dsa_pool if q.get("difficulty") == diff]
                if items:
                    dsa.append(random.choice(items))

            tech_pool = q_db.get("technical", {})
            technical = []
            
            # Use missing skills if any, else fallback to some base skills
            skills_to_test = missing_skills[:5] if missing_skills else ["python", "sql", "data structures"]
            
            for s in skills_to_test:
                s_key = s.lower().strip()
                if s_key in tech_pool and tech_pool[s_key]:
                    technical.append(random.choice(tech_pool[s_key]))
                else:
                    technical.append({
                        "question": f"Could you explain your experience and understanding of {s}?",
                        "reference_answer": f"Candidate needs to explain {s} clearly with examples."
                    })

            hr_pool = q_db.get("hr", [])
            hr = random.sample(hr_pool, min(3, len(hr_pool)))

            return {
                "aptitude": aptitude,
                "dsa": dsa,
                "technical": technical,
                "hr": hr
            }

        except Exception as db_err:
            print(f"Failed to load fallback db: {db_err}")
            return {
                "aptitude": [],
                "dsa": [],
                "technical": [],
                "hr": []
            }

# ---------------- Start Interview ----------------

@app.post("/start_interview")
def start_interview(data: dict):

    missing_skills = data["missing_skills"]
    job_role = data["job_role"]

    interview = generate_interview(missing_skills, job_role)

    return {"interview": interview}


# ---------------- Answer Evaluation ----------------

class Answer(BaseModel):

    question: str
    user_answer: str
    reference_answer: str


@app.post("/submit_answer")
def submit_answer(data: Answer):

    if len(data.user_answer) > 20:
        score = 1
    else:
        score = 0.5

    return {"score": score}


# ---------------- Save Interview Result ----------------

@app.post("/save_result")
def save_result(data: dict):

    db = SessionLocal()

    result = InterviewResult(
        email=data["email"],
        aptitude_score=data["aptitude"],
        dsa_score=data["dsa"],
        technical_score=data["technical"]
    )

    db.add(result)

    db.commit()

    db.close()

    return {"status": "saved"}


# ---------------- Interview History ----------------

@app.get("/history/{email}")
def history(email: str, authorization: str = Header(None)):

    user = verify_token(authorization)

    if user != email:
        return {"error": "Unauthorized"}

    db = SessionLocal()

    results = db.query(InterviewResult).filter(
        InterviewResult.email == email
    ).all()

    db.close()

    return results


# ---------------- AI Feedback ----------------

@app.post("/ai_feedback")
def ai_feedback(data: dict):

    aptitude = data["aptitude"]
    dsa = data["dsa"]
    technical = data["technical"]

    return analyze_performance(aptitude, dsa, technical)


# ---------------- Practice Questions ----------------

@app.post("/practice_questions")
def practice_questions(data: dict):
    weaknesses = data.get("weaknesses", [])
    practice = []
    
    try:
        db_path = os.path.join(BASE_DIR, "backend", "questions.json")
        with open(db_path, "r") as f:
            q_db = json.load(f)
            
        if "Aptitude" in weaknesses:
            apt = q_db.get("aptitude", [])
            for q in random.sample(apt, min(2, len(apt))):
                practice.append({"topic": "Aptitude", "type": "mcq", "question": q["question"], "options": q.get("options", []), "answer": q.get("answer", "")})
                
        if "Data Structures" in weaknesses:
            dsa = q_db.get("dsa", [])
            for q in random.sample(dsa, min(2, len(dsa))):
                practice.append({"topic": "Data Structures", "type": "text", "question": q["question"], "reference_answer": q.get("reference_answer", "")})
                
        if "Technical Concepts" in weaknesses:
            tech_pool = q_db.get("technical", {})
            techs = list(tech_pool.values())
            if techs:
                flat_techs = [q for sublist in techs for q in sublist]
                for q in random.sample(flat_techs, min(2, len(flat_techs))):
                    practice.append({"topic": "Technical Concepts", "type": "text", "question": q["question"], "reference_answer": q.get("reference_answer", "")})
                    
    except Exception as e:
        print(f"Failed to load practice questions: {e}")

    return {"practice": practice}


@app.post("/evaluate_practice")
def evaluate_practice(data: dict):
    answers = data.get("answers", [])
    remarks = []
    
    for item in answers:
        q_text = item.get("question", "")
        u_ans = item.get("user_answer", "")
        topic = item.get("topic", "")
        q_type = item.get("type", "text")
        
        if q_type == "mcq":
            correct_ans = item.get("answer", "")
            if u_ans == correct_ans:
                remarks.append({"question": q_text, "remark": "Correct! Good job."})
            else:
                remarks.append({"question": q_text, "remark": f"Incorrect. The correct answer is {correct_ans}."})
        else:
            ref_ans = item.get("reference_answer", "")
            prompt = f"Evaluate this candidate's practice answer.\nQuestion: {q_text}\nReference Answer: {ref_ans}\nCandidate Answer: {u_ans}\n\nProvide a very short, 1-2 sentence remark on how they did and what they can improve."
            try:
                response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
                remark = response["message"]["content"].strip()
                remarks.append({"question": q_text, "remark": remark})
            except Exception as e:
                remarks.append({"question": q_text, "remark": f"Good effort. Reference answer to compare against: {ref_ans}"})
                
    return {"remarks": remarks}


# ---------------- Run DSA Code ----------------

@app.post("/run_dsa")
def run_dsa(data: dict):

    code = data["code"]

    test_input = "5"
    expected_output = "120"

    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
        f.write(code.encode())
        filename = f.name

    try:

        result = subprocess.run(
            ["python3", filename],
            input=test_input,
            text=True,
            capture_output=True,
            timeout=5
        )

        output = result.stdout.strip()

        score = 1 if output == expected_output else 0

        return {
            "output": output,
            "expected": expected_output,
            "score": score
        }

    except Exception as e:
        return {"error": str(e)}


# ---------------- Resume Feedback ----------------

@app.post("/resume_feedback")
def resume_feedback(data: dict):

    missing = data["missing_skills"]

    suggestions = []

    for skill in missing:
        suggestions.append(
            f"Consider adding projects or experience related to {skill}"
        )

    return {
        "missing_skills": missing,
        "suggestions": suggestions
    }


# ---------------- Skill Trend ----------------

@app.get("/trend/{email}")
def trend(email: str):

    db = SessionLocal()

    results = db.query(InterviewResult).filter(
        InterviewResult.email == email
    ).all()

    db.close()

    trend = []

    for r in results:

        trend.append({
            "aptitude": r.aptitude_score,
            "dsa": r.dsa_score,
            "technical": r.technical_score
        })

    return {"trend": trend}


# ---------------- Login ----------------

@app.post("/login")
def login(data: dict):

    email = data["email"]

    token = create_token(email)

    return {"token": token}


# ---------------- Google Login ----------------

@app.get("/auth/google")
async def google_login(request: Request):

    redirect_uri = request.url_for("google_callback")

    return await oauth.google.authorize_redirect(request, redirect_uri)




@app.get("/auth/google/callback")
async def google_callback(request: Request):

    # exchange code for access token
    token = await oauth.google.authorize_access_token(request)

    # fetch user profile
    resp = await oauth.google.get(
        "https://www.googleapis.com/oauth2/v3/userinfo",
        token=token
    )

    user = resp.json()

    email = user["email"]

    jwt_token = create_token(email)

    return RedirectResponse(
        url=f"http://127.0.0.1:8000/frontend/dashboard.html?token={jwt_token}&email={email}",
        status_code=302
    )