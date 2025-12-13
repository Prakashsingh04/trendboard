import time
from app.services.fetch_news import fetch_finnhub_news
from app.services.firestore import save_news
from app.services.summarize import summarize_article

INTERVAL = 1800  # 30 minutes


def run_worker():
    print("Trendboard worker started")

    while True:
        try:
            news_list = fetch_finnhub_news(limit=10)

            for article in news_list:
                summary = summarize_article(article["summary"] or article["title"])

                save_news({
                    "title": article["title"],
                    "summary": summary,
                    "category": "Finance",
                    "sentiment": "Neutral",
                    "source": article["source"],
                    "url": article["url"],
                    "image": article.get("image")
                })

            print("News cycle completed")

        except Exception as e:
            print("Worker error:", e)

        time.sleep(INTERVAL)


if __name__ == "__main__":
    run_worker()
