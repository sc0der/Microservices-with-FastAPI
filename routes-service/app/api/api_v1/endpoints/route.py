
from pyexpat import model
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app import crud, schemas, models

router = APIRouter()

@router.get("/", response_model=List[schemas.Route])
def read_routes(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve users.
    """
    routes = crud.route.get_multi(db, skip=skip, limit=limit)
    return routes


@router.post("/", response_model=schemas.Route)
def create_route(
    *,
    db: Session = Depends(deps.get_db),
    route_in: schemas.RouteCreate,
) -> Any:
    """
    Create new route.
    """
    if (editors := db.query(models.Location).filter(models.Location.id.in_(route_in.locations))):
        route_in.locations.extend(editors)
        print("editors")
        print(editors)
        print("editors")
    route = crud.route.create_with_owner(db=db, obj_in=route_in)
    return route


@router.put("/{id}", response_model=schemas.Route)
def update_route(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    route_in: schemas.RouteUpdate,
) -> Any:
    """
    Update an route.
    """
    route = crud.route.get(db=db, id=id)
    if not route:
        raise HTTPException(status_code=404, detail="route not found")
    route = crud.route.update(db=db, db_obj=route, obj_in=route_in)
    return route


@router.get("/{id}", response_model=schemas.Route)
def read_route(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get route by ID.
    """
    route = crud.route.get(db=db, id=id)
    if not route:
        raise HTTPException(status_code=404, detail="route not found")
    return route


@router.delete("/{id}", response_model=schemas.Route)
def delete_route(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete an route.
    """
    route = crud.route.get(db=db, id=id)
    if not route:
        raise HTTPException(status_code=404, detail="route not found")
   
    route = crud.route.remove(db=db, id=id)
    return route