from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn
import os
from dotenv import load_dotenv

from routes.url_routes import router as url_router
from controllers.url_controller import get_redirect_url

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup - add your initialization code here
    yield
    # Shutdown - add your cleanup code here
    pass

app = FastAPI(title="URL Shortener API", version="1.0.0", lifespan=lifespan)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(url_router, prefix="/api")

@app.get("/health")
async def health_check():
    return {"status": "OK", "message": "URL Shortener API is running"}

@app.get("/{key}")
async def redirect_url(key: str):
    try:
        long_url = await get_redirect_url(key)
        return RedirectResponse(url=long_url, status_code=302)
    except HTTPException as e:
        raise e

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)