from fastapi import (
    APIRouter,
    Depends,
)

from .. import models
from ..services.auth import (
    get_current_user,
)

router = APIRouter()


@router.get(
    '',
)
def hello(user: models.User = Depends(get_current_user)):
    return f"Hello {user.username}"
