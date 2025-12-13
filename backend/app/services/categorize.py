def categorize_article(text: str) -> dict:
    """
    Categorize financial news using simple keyword rules
    Returns category and sentiment
    """

    if not text:
        return {"category": "General", "sentiment": "Neutral"}

    text_lower = text.lower()

    # Category rules
    if any(word in text_lower for word in ["ipo", "public offering", "listed", "listing"]):
        category = "IPO"
    elif any(word in text_lower for word in ["earnings", "revenue", "profit", "loss", "quarter"]):
        category = "Earnings"
    elif any(word in text_lower for word in ["bitcoin", "crypto", "ethereum", "blockchain"]):
        category = "Crypto"
    elif any(word in text_lower for word in ["regulation", "policy", "government", "rbi", "sec"]):
        category = "Regulation"
    elif any(word in text_lower for word in ["market", "stocks", "shares", "index", "sensex", "nifty"]):
        category = "Stock Market"
    else:
        category = "General"

    # Sentiment rules
    if any(word in text_lower for word in ["growth", "profit", "gain", "surge", "rise", "beat"]):
        sentiment = "Positive"
    elif any(word in text_lower for word in ["loss", "decline", "drop", "fall", "miss", "weak"]):
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "category": category,
        "sentiment": sentiment
    }
