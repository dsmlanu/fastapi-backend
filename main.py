from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
import json

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI working!"}

class LLMRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate(req: LLMRequest):
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=req.prompt,
            text=True,
            capture_output=True,
            encoding="utf-8"
        )
        return {"response": result.stdout}
    except Exception as e:
        return {"error": str(e)}
