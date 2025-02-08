from sqlalchemy.orm import Session

from db.models.blog import Blog
from schemas.blog import BlogCreate


def create_new_blog(blog: BlogCreate, db: Session, author_id: int = 1):
    new_blog = Blog(**blog.model_dump(), author_id=author_id, is_active=True)
    db.add(instance=new_blog)
    db.commit()
    db.refresh(instance=new_blog)
    return new_blog


def retrieve_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog
