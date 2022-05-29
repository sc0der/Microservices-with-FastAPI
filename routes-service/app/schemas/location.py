from typing import Optional
from pydantic import BaseModel


class LocationBase(BaseModel):
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    is_navigate: Optional[bool] = None
    is_active: Optional[bool] = True

    class Config:
        orm_mode = True


class LocationCreate(LocationBase):
    pass

class LocationUpdate(LocationBase):
    pass

class LocationInDBBase(LocationBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class Location(LocationInDBBase):
    pass