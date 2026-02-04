from models.user import User
from uow.unit_of_work import UnitOfWork


class UserService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def register(self, email: str) -> User:
        async with self.uow:
            if await self.uow.users.get_by_email(email):
                raise ValueError("User already exists")

            user = User(email=email)
            await self.uow.users.create(user)
            return user
