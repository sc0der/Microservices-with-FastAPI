from fastapi import APIRouter

from app.api.api_v1.endpoints import route, location

api_router = APIRouter()
api_router.include_router(location.router, prefix="/locations", tags=["locations"])
api_router.include_router(route.router, prefix="/routes", tags=["routes"])