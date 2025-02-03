from fastapi import APIRouter

from apis.v1 import route_blog, route_user

api_router = APIRouter()
api_router.include_router(route_user.router, prefix="", tags=["user"])
api_router.include_router(route_blog.router, prefix="", tags=["blog"])
