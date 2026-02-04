from fastapi import APIRouter, Depends
from schemas.user import UserCreate, UserRead
from services.user import UserService
from dependencies import get_user_service


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserRead)
async def register_user(
    data: UserCreate,
    service: UserService = Depends(get_user_service),
):
    return await service.register(data.email)
