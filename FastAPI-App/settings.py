from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://postgres:abc12345@localhost:5432/demo_db"

settings = Settings()
