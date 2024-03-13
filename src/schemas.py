from datetime import datetime

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    id: str | None = Field(alias='_id', default=None)
    username: str
    email: str
    phone_number: str
    birth_date: datetime


class UserRead(UserBase):
    pass


class UserCreate(UserBase):
    pass


class GetUsersResponse(BaseModel):
    items: list[UserRead]


class PaginationSchema(BaseModel):
    total: int
    page: int
    page_size: int
    pages_count: int
    items: list[BaseModel]


class UsersPaginationSchema(PaginationSchema):
    items: list[UserRead]
