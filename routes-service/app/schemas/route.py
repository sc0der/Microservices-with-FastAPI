from typing import List, Optional
from .location import LocationBase
from pydantic import BaseModel


class RouteBase(BaseModel):
    name: Optional[str] = None
    is_active: Optional[bool] = True
    external_user_id: Optional[int] = None

    class Config:
        orm_mode = True

class RouteCreate(RouteBase):
    locations: List[int] = []
    

class RouteUpdate(RouteBase):
    pass

class RouteInDBBase(RouteBase):
    id: Optional[int] = None
    locations: List[LocationBase] = []

    class Config:
        orm_mode = True

class Route(RouteInDBBase):
    pass

class RouteInDB(RouteInDBBase):
    pass
