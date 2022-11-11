from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from ..db.session import get_db

from .. import (
    db, models
)


class UserService:

    def __init__(self, session: Session = Depends(get_db)):
        self.session = session

    def get(self,
            user_id: int
            ) -> db.User:
        return self._get_by_id(user_id)

    def get_many(self,
                 ) -> list[db.User]:
        users = self.session.query(db.User).order_by(db.User.id.desc()).all()
        return users

    def patch(self,
              user_id: id,
              user_data: models.UpdateUser
              ) -> db.User:
        user = self._get_by_id(user_id)
        if user_data.username and user_data.username != user.username and self._username_is_unique(user_data.username):
            user.username = user_data.username
        if user_data.email and user_data.email != user.email and self._email_is_unique(user_data.email):
            user.email = user_data.email
        if user_data.first_name is not None:
            user.first_name = user_data.first_name
        if user_data.last_name is not None:
            user.last_name = user_data.last_name

        self.session.commit()
        return user

    def _get_by_id(
            self,
            id: int,
    ) -> db.User:
        exception = HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='user with following id -> {} - not found'.format(id),
        )
        user = (self.session
                .query(db.User)
                .filter(db.User.id == id)
                .first())
        if not user:
            raise exception
        return user

    def can_create(
            self,
            email: str,
            username: str,
    ):
        return self._email_is_unique(email) and self._username_is_unique(username)

    def _username_is_unique(
            self,
            username: str
    ) -> bool:
        if self._get_by_username(username):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='user with current username already exist',
            )
        return True

    def _get_by_username(
            self,
            username: str,
    ) -> db.User:
        user = (self.session
                .query(db.User)
                .filter(db.User.username == username)
                .first())
        return user

    def _email_is_unique(
            self,
            email: str
    ) -> bool:
        if self._get_by_email(email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='user with current email already exist',
            )

        return True

    def _get_by_email(
            self,
            email: str,
    ) -> db.User:
        user = (self.session
                .query(db.User)
                .filter(db.User.email == email)
                .first())
        return user
