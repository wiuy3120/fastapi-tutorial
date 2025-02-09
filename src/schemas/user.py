from pydantic import BaseModel, ConfigDict, EmailStr, Field


# properties required during user creation
class CreateUser(BaseModel):
    email: EmailStr
    password: str = Field(min_length=4)


class ShowUser(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
