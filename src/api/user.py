from fastapi import Depends, HTTPException, Body, APIRouter

from database.orm import User
from database.repository import UserRepository
from schema.request import SignUpRequest
from schema.response import UserSchema
from service.user import UserService

router = APIRouter(prefix="/users")


@router.post("/sign-up", status_code=201)
async def user_sign_up_handler(
        request: SignUpRequest,
        user_service: UserService = Depends(),
        user_repo: UserRepository = Depends(),
) -> UserSchema:
    hashed_password: str = user_service.hash_password(
        plain_password=request.password
    )
    user: User = User.create(
        username=request.username, hashed_password=hashed_password
    )
    user: User = user_repo.save_user(user=user)
    return UserSchema.from_orm(user)
