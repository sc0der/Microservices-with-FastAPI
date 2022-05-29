from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from typing import List

from app.crud.base import CRUDBase
from app.models.routes_locations import Location
from app.schemas.location import LocationCreate, LocationUpdate

class CRUDLocation(CRUDBase[Location, LocationCreate, LocationUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: LocationCreate
    ) -> Location:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Location]:
        return (
            db.query(self.model)
            .filter(Location.is_active == True)
            .offset(skip)
            .limit(limit)
            .all()
        )


location = CRUDLocation(Location)