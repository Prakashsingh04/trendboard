import google.generativeai as genai
from app.utils.config import settings

# Configure Gemini
genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def summarize_article(text: str) -> str:

    if not text or len(text.strip()) == 0:
        return ""

    prompt = f"""
    Summarize the following financial news in 3 to 4 clear lines.
    Keep it neutral, concise, and informative with simple wordings.

    News:
    {text}
    """

    response = model.generate_content(prompt)

    return response.text.strip()
