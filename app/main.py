"""Minimal TherapistFlow FastAPI scaffold."""

from fastapi import FastAPI

app = FastAPI(title="TherapistFlow")


@app.get("/health")
def health_check():
    """Return a lightweight signal that the API is responding."""
    return {"status": "ok"}
