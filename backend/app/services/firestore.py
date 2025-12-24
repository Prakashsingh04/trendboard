import os
from pathlib import Path
from datetime import datetime
from google.cloud import firestore
from app.utils.config import settings


def _ensure_firestore_credentials():
    # If GOOGLE_APPLICATION_CREDENTIALS is not set, try local serviceAccountKey.json
    if os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
        return
    root = Path(__file__).resolve().parents[2]  # backend/
    cred_path = root / "serviceAccountKey.json"
    if cred_path.exists():
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(cred_path)


def _get_client() -> firestore.Client:
    _ensure_firestore_credentials()
    # Use explicit project if provided; otherwise let ADC infer
    project_id = getattr(settings, "FIREBASE_PROJECT_ID", None)
    if project_id:
        return firestore.Client(project=project_id)
    return firestore.Client()


def save_news(article: dict):
    """Save a single news article to Firestore."""
    db = _get_client()
    article["created_at"] = datetime.utcnow()
    db.collection("news").add(article)


def get_latest_news(limit: int = 20):
    """Fetch latest news articles from Firestore."""
    db = _get_client()
    docs = (
        db.collection("news")
        .order_by("created_at", direction=firestore.Query.DESCENDING)
        .limit(limit)
        .stream()
    )

    news_list = []
    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        news_list.append(data)

    return news_list
