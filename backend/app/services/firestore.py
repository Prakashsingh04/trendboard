from google.cloud import firestore
from datetime import datetime

# Initialize Firestore client
db = firestore.Client()


def save_news(article: dict):
    """
    Save a single news article to Firestore
    """
    article["created_at"] = datetime.utcnow()
    db.collection("news").add(article)


def get_latest_news(limit: int = 20):
    """
    Fetch latest news articles from Firestore
    """
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
