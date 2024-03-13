from typing import Any

from pymongo import MongoClient

from src.schemas import UserRead, PaginationSchema


class UserRepository:
    collection_name = 'users'
    db_name = 'commondb'

    def __init__(self, *, db_url: str):
        client = MongoClient(db_url)
        db = client[self.db_name]
        self.collection = db[self.collection_name]

    def create_one(self, data: dict[str, Any]) -> str:
        object_id = self.collection.insert_one(data)
        return str(object_id)

    def bulk_create(self, data: list[dict[str, Any]]) -> list[str]:
        result = self.collection.insert_many(data)
        ids = [str(id) for id in result.inserted_ids]
        return ids

    def get_all(self) -> list[UserRead]:
        cursor = self.collection.find()
        users = []

        for user in cursor:
            user['_id'] = str(user['_id'])
            users.append(UserRead.model_validate(user))

        return users

    def get_all_with_pagination(self, *, page: int, page_size: int) -> PaginationSchema:
        total = self.collection.count_documents(filter={})

        limit = page_size
        offset = (page - 1) * limit

        if total % page_size > 0:
            pages_count = total // page_size + 1
        else:
            pages_count = total // page_size

        cursor = self.collection.find().limit(limit).skip(offset)

        items = []

        for user in cursor:
            user['_id'] = str(user['_id'])
            items.append(UserRead.model_validate(user))

        return PaginationSchema(
            total=total,
            page=page,
            page_size=page_size,
            pages_count=pages_count,
            items=items
        )

    def drop_all(self):
        self.collection.delete_many(filter={})
