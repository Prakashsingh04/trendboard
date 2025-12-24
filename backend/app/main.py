import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import health, news


def _default_allowed_origins() -> list[str]:
    # Common local dev origins for Vite/React
    return [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]


def _get_allowed_origins() -> list[str]:
    origins_env = os.getenv("ALLOWED_ORIGINS")
    if origins_env:
        return [o.strip() for o in origins_env.split(",") if o.strip()]
    return _default_allowed_origins()


def _ensure_firestore_credentials():
    # Respect existing env; otherwise point to bundled serviceAccountKey.json
    if os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
        return

    root = Path(__file__).resolve().parents[1]  # backend/
    cred_path = root / "serviceAccountKey.json"
    if cred_path.exists():
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(cred_path)


app = FastAPI(
    title="Trendboard Backend",
    description="Backend API for trending financial news dashboard",
    version="1.0.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=_get_allowed_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    _ensure_firestore_credentials()


@app.get("/")
def root():
    return {"service": "trendboard", "status": "ok"}


# Routers
app.include_router(health.router)
app.include_router(news.router)
