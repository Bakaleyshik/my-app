import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Hello from FastAPI in Kubernetes! 🚀",
        "env": os.getenv("APP_ENV", "unknown"),
    }

@app.get("/health")
def health():
    return {"status": "ok"}