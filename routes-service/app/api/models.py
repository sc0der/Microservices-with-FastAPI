from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from .db import Base

route_coordinates = Table('route_coordinates', Base.metadata,
    Column('route_id', ForeignKey('route.id'), primary_key=True),
    Column('coordinate_id', ForeignKey('coordinate.id'), primary_key=True)
)

class Route(Base):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    is_active = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True)
    created_id = Column(Date)
    coordinates = relationship("Coordinate", secondary="route_coordinates", back_populates='routes')


class Coordinate(Base):
    __tablename__ = "coordinates"

    id = Column(Integer, primary_key=True, index=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    is_navigate = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True)
    created_id = Column(Date)
    routes = relationship("Route", secondary="route_coordinates", back_populates='coordinates')