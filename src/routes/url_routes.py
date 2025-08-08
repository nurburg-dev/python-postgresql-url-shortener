from fastapi import APIRouter, status
from models import URLCreate, CustomURLCreate, URLResponse
from controllers.url_controller import create_short_url, create_custom_short_url

router = APIRouter()

@router.post("/short_url", response_model=URLResponse, status_code=status.HTTP_201_CREATED)
async def create_short_url_endpoint(url_data: URLCreate):
    return await create_short_url(url_data)

@router.post("/short_url/custom", response_model=URLResponse, status_code=status.HTTP_201_CREATED)
async def create_custom_short_url_endpoint(url_data: CustomURLCreate):
    return await create_custom_short_url(url_data)