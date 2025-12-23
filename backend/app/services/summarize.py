import google.generativeai as genai
from app.utils.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

# Use a supported model for this API key
model = genai.GenerativeModel("gemini-2.5-flash")


def summarize_article(text: str) -> str:
    if not text or len(text.strip()) == 0:
        return ""

    prompt = f"""
Summarize the following financial news in 3–4 clear lines.
Keep it neutral, concise, and informative.

News:
{text}
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("Summarization error:", e)
        return ""
