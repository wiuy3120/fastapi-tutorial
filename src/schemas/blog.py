from pydantic import BaseModel, model_validator


class BlogCreate(BaseModel):
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


class ShowBlog(BaseModel):
    id: int
    title: str
    content: str | None
    author_id: int
    is_active: bool

    class Config:
        from_attributes = True
