from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Yomutext"
    DOCS_URL: str | None = None
    REDOC_URL: str | None = None
    OPENAPI_URL: str = "/openapi.json"
    SCALAR_URL: str = "/scalar"
    DATABASE_URL: str = "sqlite:///./core.db"
    VERSION: str = "0.1.0"


    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()