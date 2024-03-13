from settings import Settings
from src.user_repository import UserRepository


def get_settings():
    return Settings()


def create_user_repository(
        *,
        db_url: str = get_settings().mongo_db_url
):
    return UserRepository(db_url=db_url)
