

from fastapi import FastAPI, HTTPException
from fastapi.routing import APIRouter
from pydantic import BaseModel
import string
import random
from datetime import datetime, timedelta
import qrcode
from io import BytesIO
from typing import Dict
