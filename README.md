# IntelliHire AI

IntelliHire is an AI-powered interview preparation platform that analyzes resumes, generates mock interviews, evaluates performance, and provides personalized improvement suggestions.

## Features

- Resume skill analysis
- Resume improvement suggestions
- AI-generated interview questions
- Aptitude MCQ round
- DSA coding round
- Technical interview simulation
- HR interview simulation
- AI performance feedback
- Weak skill detection
- Practice question generator
- Interview dashboard
- Skill trend tracking

## Tech Stack

Frontend:
- HTML
- JavaScript

Backend:
- FastAPI
- Python

Database:
- SQLite
- SQLAlchemy

AI Integration:
- Ollama (LLM)

## System Workflow

Resume Upload
↓
Skill Extraction
↓
AI Interview Generation
↓
Aptitude Round
↓
DSA Coding Round
↓
Technical Interview
↓
HR Interview
↓
Performance Analysis
↓
Practice Recommendations

## Running the Project

### Install dependencies

```
pip install -r requirements.txt
```

### Start backend

```
cd backend
uvicorn main:app --reload
```

### Open frontend

Open:

```
frontend/login.html
```

in a browser.

## Project Structure

```
backend/
frontend/
data/
README.md
```
