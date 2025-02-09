from datetime import datetime

from pydantic import BaseModel, ConfigDict, model_validator


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: str | None = None
    # author_id: int

    @model_validator(mode="before")
    def generate_slug(cls, data):
        if "title" not in data:
            return data
        if not isinstance(data, dict):
            return data
        if data.get("slug", None) is None:
            data["slug"] = data["title"].replace(" ", "-").lower()
        return data


class UpdateBlog(CreateBlog):
    pass


class ShowBlog(BaseModel):
    id: int
    title: str
    content: str | None
    author_id: int
    created_at: datetime
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
