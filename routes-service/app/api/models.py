from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, ForeignKey, Float, Date, UniqueConstraint
from sqlalchemy.orm import relationship
from .db import Base

route_locations = Table('route_locations', Base.metadata,
    Column('route_id', ForeignKey('route.id'), primary_key=True),
    Column('location_id', ForeignKey('location.id'), primary_key=True)
)

class Route(Base):
    __tablename__ = "route"

    __table_args__ = (
        UniqueConstraint('external_user_id', name='user_id'),
    )
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    is_active = Column(Boolean, default=True)
    external_user_id = Column(Integer)
    locations = relationship("Location", secondary="route_location", back_populates='route')
    created_id = Column(Date)


class Location(Base):
    __tablename__ = "location"

    id = Column(Integer, primary_key=True, index=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    is_navigate = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True)
    routes = relationship("Route", secondary="route_location", back_populates='location')
    created_id = Column(Date)
