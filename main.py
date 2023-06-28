from fastapi import FastAPI
from fastapi.routing import APIRouter
from app.shortener import shorten_url, redirect_to_long_url
from app.analytics import get_url_analytics
from app.deletion import delete_short_url

app = FastAPI()

router = APIRouter()
router.include_router(shorten_url.router, tags=["URL Shortener "])
router.include_router(redirect_to_long_url.router, tags=["URL Redirection"])
router.include_router(get_url_analytics.router, tags=["URL Analytics"])
router.include_router(delete_short_url.router, tags=["URL Deletion"])

app.include_router(router)
