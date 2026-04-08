from fastapi import FastAPI
from pydantic import BaseModel
from prompt_rewriter import rewrite_prompt, clean_input

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/optimize")

def optimize_prompt(data: dict):
    user_input = data.get("prompt", "")
    user_input = clean_input(user_input)
    improved = rewrite_prompt(user_input)
    return (improved)