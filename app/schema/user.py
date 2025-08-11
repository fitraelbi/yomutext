from pydantic import BaseModel

class UserCreate(BaseModel):
    fullname: str
    email: str
    password: str

class UserRead(BaseModel):
    id: str
    fullname: str
    email: str

class UserUpdate(BaseModel):
    fullname: str | None = None
    email: str | None = None
    password: str | None = None

class UserDelete(BaseModel):
    id: str