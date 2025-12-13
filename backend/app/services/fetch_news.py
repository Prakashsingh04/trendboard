import requests
from app.utils.config import settings

FINNHUB_NEWS_URL = "https://finnhub.io/api/v1/news"


def fetch_finnhub_news(category: str = "general", limit: int = 10):
    """
    Fetch latest financial news from Finnhub
    """
    params = {
        "category": category,
        "token": settings.FINNHUB_API_KEY
    }

    response = requests.get(FINNHUB_NEWS_URL, params=params, timeout=10)
    response.raise_for_status()

    news_data = response.json()

    cleaned_news = []

    for article in news_data[:limit]:
        cleaned_news.append({
            "title": article.get("headline"),
            "summary": article.get("summary"),
            "source": article.get("source"),
            "url": article.get("url"),
            "image": article.get("image"),
            "published_at": article.get("datetime")
        })

    return cleaned_news
