from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.repository.blog import (
    create_new_blog,
    delete_blog,
    list_blog,
    retrieve_blog,
    update_blog,
)
from db.session import get_db
from schemas.blog import CreateBlog, ShowBlog, UpdateBlog

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


@router.get("/blogs", response_model=List[ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = list_blog(db=db)
    return blogs


@router.post(
    "/blogs", response_model=ShowBlog, status_code=status.HTTP_201_CREATED
)
def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):

    new_blog = create_new_blog(blog=blog, db=db, author_id=1)
    return new_blog


@router.put("/blog/{id}", response_model=ShowBlog)
def update_a_blog(id: int, blog: UpdateBlog, db: Session = Depends(get_db)):
    updated_blog = update_blog(id=id, blog=blog, author_id=1, db=db)
    if not updated_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} does not exist",
        )
    return updated_blog


@router.delete("/blog/{id}")
def delete_a_blog(id: int, db: Session = Depends(get_db)):
    deleted = delete_blog(id=id, db=db)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} does not exist",
        )
    return f"Deleted blog with id {id}"
