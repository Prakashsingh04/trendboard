from fastapi import APIRouter, HTTPException, Query

from app.services.fetch_news import fetch_finnhub_news
from app.services.summarize import summarize_article
from app.services.categorize import categorize_article
from app.services.firestore import save_news, get_latest_news


router = APIRouter(
	prefix="/news",
	tags=["News"],
)


@router.get("/")
def list_news(limit: int = Query(default=20, ge=1, le=100)):
	"""
	Return the latest saved news from Firestore.
	"""
	try:
		return get_latest_news(limit=limit)
	except Exception as e:
		raise HTTPException(status_code=500, detail=f"Failed to fetch news: {e}")


@router.post("/ingest")
def ingest_news(category: str = Query(default="general"), limit: int = Query(default=10, ge=1, le=50)):
	"""
	Fetch fresh news from Finnhub, summarize, categorize & persist.
	Returns the number of articles ingested.
	"""
	try:
		raw_articles = fetch_finnhub_news(category=category, limit=limit)

		processed = 0
		for article in raw_articles:
			base_text = article.get("summary") or article.get("title") or ""
			summary = summarize_article(base_text)
			cat = categorize_article(summary or base_text)

			save_news({
				"title": article.get("title"),
				"summary": summary,
				"category": cat.get("category"),
				"sentiment": cat.get("sentiment"),
				"source": article.get("source"),
				"url": article.get("url"),
				"image": article.get("image"),
			})
			processed += 1

		return {"processed": processed, "category": category}
	except Exception as e:
		raise HTTPException(status_code=500, detail=f"Ingestion failed: {e}")

