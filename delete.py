from fastapi import APIRouter, HTTPException
from app.main import short_urls_db, analytics_db

router = APIRouter()


@router.delete('/{short_alias}')
def delete_short_url(short_alias: str):
    if short_alias in short_urls_db and short_alias in analytics_db:
        del short_urls_db[short_alias]
        del analytics_db[short_alias]
        return {'message': 'Short URL deleted successfully'}

    raise HTTPException(status_code=400, detail='Invalid URL')
