from fastapi import HTTPException
from models import URLCreate, CustomURLCreate, URLResponse
from services.url_service import url_service

async def create_short_url(url_data: URLCreate) -> URLResponse:
    pass

async def create_custom_short_url(url_data: CustomURLCreate) -> URLResponse:
    pass

async def get_redirect_url(key: str) -> str:
    pass