from sqlalchemy import true
from sqlalchemy.orm import Session

from db.models.blog import Blog
from schemas.blog import CreateBlog, UpdateBlog


def create_new_blog(blog: CreateBlog, db: Session, author_id: int = 1):
    new_blog = Blog(**blog.model_dump(), author_id=author_id, is_active=True)
    db.add(instance=new_blog)
    db.commit()
    db.refresh(instance=new_blog)
    return new_blog


def update_blog(id: int, blog: UpdateBlog, author_id: int, db: Session):
    existing_blog = db.query(Blog).filter(Blog.id == id).first()
    if not existing_blog:
        return None
    for column, new_value in blog.model_dump().items():
        setattr(existing_blog, column, new_value)
    db.commit()
    return existing_blog


def retrieve_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog


def list_blog(db: Session):
    # blogs = db.query(Blog).filter(Blog.is_active.is_(True)).all()
    blogs = db.query(Blog).filter(Blog.is_active == true()).all()
    return blogs
