from sqlalchemy.orm import Session

from db.models.blog import Blog
from schemas.blog import BlogCreate


def create_new_blog(blog: BlogCreate, db: Session, author_id: int = 1):
    blog = Blog(**blog.model_dump(), author_id=author_id, is_active=True)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog
