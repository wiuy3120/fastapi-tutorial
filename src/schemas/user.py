from pydantic import BaseModel, EmailStr, Field


# properties required during user creation
class CreateUser(BaseModel):
    email: EmailStr
    password: str = Field(min_length=4)


class ShowUser(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:  # tells pydantic to convert even non dict obj to json
        from_attributes = True
