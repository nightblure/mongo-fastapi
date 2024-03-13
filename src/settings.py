from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mongo_db_url: str
    app_port: int
    items_count: int = 35

    class Config:
        env_file = '../.env'
