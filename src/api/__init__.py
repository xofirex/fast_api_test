from fastapi import APIRouter

from . import (
    auth,
    base,
    users
)

router = APIRouter()
router.include_router(auth.router, prefix='/login', tags=['login'])
router.include_router(base.router, prefix='/say_hello', tags=['welcome'])
router.include_router(users.router, prefix='/users', tags=['users'])
