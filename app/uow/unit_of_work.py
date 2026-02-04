from sqlalchemy.ext.asyncio import AsyncSession
from repositories.user import UserRepository


class UnitOfWork:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.users = UserRepository(session)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, *_):
        if exc_type:
            await self.session.rollback()
        else:
            await self.session.commit()
