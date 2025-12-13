from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import health, news

app = FastAPI(
    title="Trendboard Backend",
    description="Backend API for trending financial news dashboard",
    version="1.0.0"
)

# Allow frontend (React) to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health.router)
app.include_router(news.router)
