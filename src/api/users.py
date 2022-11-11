from fastapi import (
    APIRouter,
    Depends,
    status
)

from .. import models

from ..services.users import UserService

router = APIRouter()


@router.get(
    '',
    response_model=list[models.UserResp],
    status_code=status.HTTP_200_OK,
)
def users_list(
        user_service: UserService = Depends(),

):
    return user_service.get_many()


@router.get(
    '{user_id}',
    response_model=models.UserResp,
    status_code=status.HTTP_200_OK,
)
def get_user(
        user_id: int,
        user_service: UserService = Depends(),

):
    return user_service.get(user_id)


@router.patch(
    '{user_id}',
    response_model=models.UserResp,
    status_code=status.HTTP_200_OK,
)
def patch_user(
        user_id: int,
        user_data: models.UpdateUser,
        user_service: UserService = Depends(),

):
    return user_service.patch(user_id, user_data)
