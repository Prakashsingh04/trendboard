from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    FINNHUB_API_KEY: str
    GEMINI_API_KEY: str
    FIREBASE_PROJECT_ID: str

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
