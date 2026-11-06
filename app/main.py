"""Minimal TherapistFlow FastAPI scaffold."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="TherapistFlow")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["GET"],
)

@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI!"}