from fastapi import FastAPI
from pydantic import BaseModel
from backend.prompt_rewriter import rewrite_prompt, clean_input
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class PromptRequest(BaseModel):
    prompt: str

@app.post("/optimize")

def optimize_prompt(data: dict):
    user_input = data.get("prompt", "")
    user_input = clean_input(user_input)
    improved = rewrite_prompt(user_input)
    return (improved)