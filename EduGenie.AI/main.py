import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

os.environ.setdefault("GEMINI_MODEL", "gemini-2.5-flash")


# ---------------------------------------------------------
# FastAPI Application
# ---------------------------------------------------------

app = FastAPI(
    title="EduGenie",
    description="AI-powered educational learning assistant",
    version="1.0.0",
)


# ---------------------------------------------------------
# Project Paths
# ---------------------------------------------------------

TEMPLATE_DIR = BASE_DIR / "templetes"
STATIC_DIR = TEMPLATE_DIR / "static"

app.mount(
    "/static",
    StaticFiles(directory=str(STATIC_DIR)),
    name="static",
)

templates = Jinja2Templates(
    directory=str(TEMPLATE_DIR)
)


# ---------------------------------------------------------
# Request Models
# ---------------------------------------------------------

class QuestionRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        max_length=10000
    )


class TextRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=20000
    )


class QuizRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=20000
    )


class LearningPathRequest(BaseModel):
    topic: str = Field(
        ...,
        min_length=1,
        max_length=500
    )

    level: str = Field(
        default="beginner",
        max_length=50
    )


# ---------------------------------------------------------
# Frontend
# ---------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {}
    )


# ---------------------------------------------------------
# Health Check
# ---------------------------------------------------------

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "EduGenie"
    }


# ---------------------------------------------------------
# Q&A API
# ---------------------------------------------------------

@app.post("/qa")
async def qa(payload: QuestionRequest):

    answer = answer_question(
        payload.question
    )

    return {
        "answer": answer
    }


# ---------------------------------------------------------
# Explanation API
# ---------------------------------------------------------

@app.post("/explain")
async def explain(payload: TextRequest):

    explanation = explain_concept(
        payload.text
    )

    return {
        "explanation": explanation
    }


# ---------------------------------------------------------
# Quiz API
# ---------------------------------------------------------

@app.post("/quiz")
async def quiz(payload: QuizRequest):

    quiz_data = generate_quiz(
        payload.text
    )

    return {
        "quiz": quiz_data
    }


# ---------------------------------------------------------
# Summary API
# ---------------------------------------------------------

@app.post("/summarize")
async def summarize(payload: TextRequest):

    summary = summarize_text(
        payload.text
    )

    return {
        "summary": summary
    }


# ---------------------------------------------------------
# Learning Path API
# ---------------------------------------------------------

@app.post("/learn/recommendations")
async def recommendations(
    payload: LearningPathRequest
):

    recommendations = get_learning_recommendations(
        payload.topic,
        payload.level
    )

    return {
        "recommendations": recommendations
    }