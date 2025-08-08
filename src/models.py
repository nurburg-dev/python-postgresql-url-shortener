from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional

class URLCreate(BaseModel):
    long_url: HttpUrl

class CustomURLCreate(BaseModel):
    key: str
    long_url: HttpUrl

class URLResponse(BaseModel):
    key: str

class URLModel(BaseModel):
    id: Optional[int] = None
    key: str
    long_url: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None