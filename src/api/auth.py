from fastapi import (
    APIRouter,
    Depends,
    status,
)
from fastapi.security import OAuth2PasswordRequestForm

from .. import models
from ..services.auth import (
    AuthService,
)
from ..services.users import UserService

router = APIRouter()


@router.post(
    '/sign-up/',
    response_model=models.Token,
    status_code=status.HTTP_201_CREATED,
)
def sign_up(
        user_data: models.UserCreate,
        auth_service: AuthService = Depends(),
        user_service: UserService = Depends(),
):
    _ = user_service.can_create(user_data.email, user_data.username)
    return auth_service.register_new_user(user_data)


@router.post(
    '/sign-in/',
    response_model=models.Token,
)
def sign_in(
        auth_data: OAuth2PasswordRequestForm = Depends(),
        auth_service: AuthService = Depends(),
):
    return auth_service.authenticate_user(
        auth_data.username,
        auth_data.password,
    )
