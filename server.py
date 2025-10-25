# cloudflared tunnel --url http://localhost:8000 
"""
Backup backend development build code:
    uvicorn backend:app --reload --host 0.0.0.0 --port 8000 
"""
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Hello from local FastAPI! New"}

if __name__ == "__main__":
    uvicorn.run("backend:app", host="0.0.0.0", port=8000, reload=True)