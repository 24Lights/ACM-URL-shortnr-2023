from fastapi import APIRouter, HTTPException
from app.main import analytics_db

router = APIRouter()


@router.get('/analytics/{short_alias}')
def get_url_analytics(short_alias: str):
    if short_alias in short_urls_db and short_alias in analytics_db:
        return analytics_db[short_alias]

    raise HTTPException(status_code=400, detail='Invalid URL')
