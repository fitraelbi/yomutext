from sqlmodel import Field, SQLModel

from app.utils import generate_id

class User(SQLModel, table=True):
    id: str = Field(default_factory=generate_id.generate_id, primary_key=True) # type: ignore
    fullname: str = Field(default="")
    email: str = Field(default="", unique=True)
    password: str

    