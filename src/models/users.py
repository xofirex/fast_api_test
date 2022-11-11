from pydantic import BaseModel, EmailStr


class BaseUser(BaseModel):
    email: EmailStr
    username: str


class UserCreate(BaseUser):
    password: str


class User(BaseUser):
    id: int
    username: str

    class Config:
        orm_mode = True


class UserResp(User):
    first_name: str | None
    last_name: str | None

    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    email: EmailStr | None
    username: str | None
    first_name: str | None
    last_name: str | None


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
