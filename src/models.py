import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    password = Column(String(120))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True)
    url = Column(String(240), unique=True)
    diameter_in_km = Column(Float)
    rotation_period_in_days = Column(Float)
    orbital_period_in_days = Column(Float)
    gravity_in_g = Column(Float)
    population = Column(Integer)
    climate = Column(String(240)) 
    terrain = Column(String(240)) 
    surface_water_percent = Column(Float)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True)
    url = Column(String(240), unique=True)
    model = Column(String(150))
    vehicle_class = Column(String(150))
    manufacturer = Column(String(150))
    cost_in_credits = Column(Float)
    length_in_m = Column(Float)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed_in_kmh = Column(Float)
    cargo_capacity_in_kg = Column(Float)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True)
    url = Column(String(240), unique=True)
    height_in_cm = Column(Float)
    mass_in_kg = Column(Float)
    hair_color = Column(String(30))
    skin_color = Column(String(30))
    eye_color = Column(String(30))
    birthyear = Column(String(30))
    gender = Column(String(30))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

class Character_X_Vehicle(Base):
    __tablename__ = 'character_x_vehicle'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship(Vehicle)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship(Vehicle)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
