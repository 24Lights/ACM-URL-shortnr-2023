from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import string
import random
from datetime import datetime, timedelta
import qrcode
from io import BytesIO

router = APIRouter()


class URLShortenRequest(BaseModel):
    long_url: str
    custom_alias: str = ''
    expiration_days: int = 30


def generate_short_alias():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))


def is_expired(expiration_date):
    return expiration_date < datetime.now()


@router.post('/shorten_url')
def shorten_url(url_request: URLShortenRequest):
    long_url = url_request.long_url
    custom_alias = url_request.custom_alias
    expiration_days = url_request.expiration_days

    if custom_alias:
        if custom_alias in short_urls_db:
            raise HTTPException(status_code=400, detail='Custom alias already exists.')

    short_alias = custom_alias if custom_alias else generate_short_alias()

    expiration_date = datetime.now() + timedelta(days=expiration_days)
    short_url = f"{request.base_url}/{short_alias}"

    short_urls_db[short_alias] = {
        'long_url': long_url,
        'expiration_date': expiration_date
    }
    analytics_db[short_alias] = {
        'click_count': 0,
        'click_timestamps': {}
    }

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(short_url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img_io = BytesIO()
    qr_img.save(qr_img_io, 'PNG')
    qr_img_io.seek(0)

    return {
        'short_url': short_url,
        'qr_code': qr_img_io.getvalue()
    }
