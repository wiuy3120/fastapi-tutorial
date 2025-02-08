from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.repository.blog import create_new_blog, retrieve_blog
from db.session import get_db
from schemas.blog import BlogCreate, ShowBlog

router = APIRouter()


@router.get("/blog/{id}", response_model=ShowBlog)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = retrieve_blog(id=id, db=db)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} is not found",
        )
    return blog


@router.post(
    "/blogs", response_model=ShowBlog, status_code=status.HTTP_201_CREATED
)
def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    new_blog = create_new_blog(blog=blog, db=db)
    return new_blog
