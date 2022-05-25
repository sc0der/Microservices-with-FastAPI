from sqlalchemy.orm import Session
from .models import Route, Location
from fastapi import Header, HTTPException, Depends

from fastapi import APIRouter


router_api = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router_api.get("/users")
async def read_users():
    return [{"username": "Foo"}, {"username": "Bar"}]