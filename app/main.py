from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference # type: ignore

from app.routes.v1.users import users_router
from app.core.settings import settings



app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)


@app.get("/")
async def root():
    return {"message": f"API YomuText {settings.VERSION}"}


app.include_router(users_router, prefix="/v1")

@app.get("/scalar", include_in_schema=False)
async def scalar():
    if app.openapi_url is None:
        raise ValueError("openapi_url is None")
    return get_scalar_api_reference(openapi_url=app.openapi_url, title=app.title)
