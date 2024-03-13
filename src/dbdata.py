from datetime import datetime

from faker import Faker

from src.deps import create_user_repository
from src.schemas import UserCreate


def generate_users(items_count: int):
    faker = Faker('en')

    users = [
        UserCreate(
            username=faker.name(),
            email=faker.email(),
            phone_number=faker.phone_number(),
            birth_date=faker.date_between_dates(
                date_start=datetime(1997, 3, 16),
                date_end=datetime(2024, 3, 13)
            )
        )
        for _ in range(items_count)
    ]

    return users


def fill_data(items_count: int):
    r = create_user_repository()
    r.drop_all()
    users_data = generate_users(items_count)
    r.bulk_create([u.dict() for u in users_data])
