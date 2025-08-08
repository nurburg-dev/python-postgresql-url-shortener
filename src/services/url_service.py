from fastapi import HTTPException
from models import URLCreate, CustomURLCreate, URLResponse

class URLService:
    async def create_short_url(self, url_data: URLCreate) -> URLResponse:
        pass
    
    async def create_custom_short_url(self, url_data: CustomURLCreate) -> URLResponse:
        pass
    
    async def get_long_url(self, key: str) -> str:
        pass

# Global service instance
url_service = URLService()