
from app.db.base_class import Base
from app.db.session import engine
from sqlalchemy import Boolean, Column, Integer, String, Date, Table, ForeignKey, UniqueConstraint, Float
from sqlalchemy.orm import relationship

route_locations = Table(
    "route_locations", Base.metadata,
    Column("location_id", ForeignKey("locations.id")),
    Column("route_id", ForeignKey("routes.id")),
)

class Route(Base):
    __tablename__ = "routes"
    __table_args__ = {'extend_existing': True},
    __table_args__ = (
        UniqueConstraint('external_user_id', name='owner_id'),
    )
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    is_active = Column(Boolean, default=True)
    external_user_id = Column(Integer)
    locations = relationship("Location", secondary=route_locations, back_populates="routes")
    created_id = Column(Date)
    
    def __repr__(self) -> str:
        return super().__repr__()


class Location(Base):
    __tablename__ = "locations"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    is_navigate = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True)
    created_id = Column(Date)
    routes = relationship("Route", secondary=route_locations, back_populates="locations")

Base.metadata.create_all(engine)