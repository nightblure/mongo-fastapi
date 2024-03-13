from fastapi import APIRouter

from src.deps import create_user_repository
from src.schemas import UsersPaginationSchema

api_router = APIRouter()


@api_router.get('/users', response_model=UsersPaginationSchema)
def get_users(page: int = 1, page_size: int = 10):
    # http://0.0.0.0:8028/users?page=1&page_size=3
    repo = create_user_repository()
    result = repo.get_all_with_pagination(page=page, page_size=page_size)
    return result
