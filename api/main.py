from os import stat
from fastapi import FastAPI, Request, status
from api.configs.settings import get_app_settings
from api.constants.tags_metadata import tags_metadata
from api.databases.session import get_db
from api.models.user_management.user import User

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


@app.get("/user", status_code=status.HTTP_200_OK)
async def create_user(request: Request):
    db = get_db()
    user = User(
        first_name="arpit",
        last_name="patel",
        email="arpit.patel@gmail.com",
        password="password",
    )
    db.add(user)
    db.commit()
    db.close()
    return {"message": "added successfully"}
