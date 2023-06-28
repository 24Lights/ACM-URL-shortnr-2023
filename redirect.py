from fastapi import APIRouter, HTTPException
from datetime import datetime
from app.main import short_urls_db, analytics_db

router = APIRouter()


@router.get('/{short_alias}')
def redirect_to_long_url(short_alias: str):
    if short_alias in short_urls_db:
        url_info = short_urls_db[short_alias]
        if not is_expired(url_info['expiration_date']):
            # Update analytics data
            analytics_db[short_alias]['click_count'] += 1
            timestamp = datetime.now().isoformat()
            analytics_db[short_alias]['click_timestamps'][timestamp] = timestamp

            return HTTPException(status_code=302, headers={'Location': url_info['long_url']})
        else:
            raise HTTPException(status_code=400, detail='Short URL has expired.')

    raise HTTPException(status_code=400, detail='Invalid URL')
