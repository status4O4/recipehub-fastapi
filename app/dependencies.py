from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_session
from uow.unit_of_work import UnitOfWork
from services.user import UserService


async def get_uow(
    session: AsyncSession = Depends(get_session),
) -> UnitOfWork:
    return UnitOfWork(session)


async def get_user_service(
    uow: UnitOfWork = Depends(get_uow),
) -> UserService:
    return UserService(uow)
