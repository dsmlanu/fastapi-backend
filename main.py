from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
import json
import os

from app.rag_pipeline import call_llm

app = FastAPI()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

@app.get("/")
def home():
    return {"message": "FastAPI working!"}

class Prompt(BaseModel):
    prompt: str

@app.post("/generate")
def generate(data: Prompt):
    try:
        response = call_llm(data.prompt)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}
