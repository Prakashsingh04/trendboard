from pydantic import BaseSettings


class Settings(BaseSettings):
    FINNHUB_API_KEY: str
    GEMINI_API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
