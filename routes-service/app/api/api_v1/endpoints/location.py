
from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app.core.config import settings
from app import crud, models, schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.Location])
def read_locations(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve users.
    """
    routes = crud.location.get_multi(db, skip=skip, limit=limit)
    return routes

@router.post("/", response_model=schemas.Location)
def create_location(
    *,
    db: Session = Depends(deps.get_db),
    location_in: schemas.LocationCreate,
) -> Any:
    """
    Create new location.
    """
    location = crud.location.create_with_owner(db=db, obj_in=location_in)
    return location


@router.put("/{id}", response_model=schemas.Location)
def update_location(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    location_in: schemas.LocationUpdate,
) -> Any:
    """
    Update an location.
    """
    location = crud.location.get(db=db, id=id)
    if not location:
        raise HTTPException(status_code=404, detail="location not found")
    location = crud.location.update(db=db, db_obj=location, obj_in=location_in)
    return location


@router.get("/{id}", response_model=schemas.Location)
def read_location(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get location by ID.
    """
    location = crud.location.get(db=db, id=id)
    if not location:
        raise HTTPException(status_code=404, detail="location not found")
    return location


@router.delete("/{id}", response_model=schemas.Location)
def delete_location(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete an location.
    """
    location = crud.location.get(db=db, id=id)
    if not location:
        raise HTTPException(status_code=404, detail="location not found")
   
    location = crud.location.remove(db=db, id=id)
    return location