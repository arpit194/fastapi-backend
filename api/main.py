from fastapi import FastAPI, status
from api.configs.settings import get_app_settings
from api.constants import tags_metadata

settings = get_app_settings()

app = FastAPI(
    title="FastAPI Backend",
    version=settings.BACKEND_VER,
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOC_URL,
    openapi_tags=tags_metadata,
)


@app.get("/", status_code=status.HTTP_200_OK)
async def welcome():
    return "FastAPI backend is running"
