from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(80), nullable=False)
    first_name: Mapped[str] = mapped_column(String(80))
    last_name: Mapped[str] = mapped_column(String(80))

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            'first_name': self.first_name,
            'last_name': self.last_name
        }


class Planets(db.Model):
    __tablename__ = 'planets'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    population: Mapped[int] = mapped_column(nullable=True)
    climate: Mapped[str] = mapped_column(String(80))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'population': self.population,
            'climate': self.climate
        }


class Characters(db.Model):
    __tablename__ = 'characters'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    gender: Mapped[str] = mapped_column(String(20))
    birth_date: Mapped[str] = mapped_column(String(15))


    def serialize(self):
        return{
            'id':self.id,
            'name':self.name,
            'gender':self.gender,
            'birth_date':self.birth_date
        }
    

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(100),unique=True, nullable=False)
    model:Mapped[str] = mapped_column(String(100),nullable=False)
    capacity:Mapped[int] = mapped_column(nullable=False)

    def serialize(self):
        return{
            'id':self.id,
            'name':self.name,
            'model':self.model,
            'capacity':self.capacity
        }


class Favorites(db.Model):
    __tablename__ = 'favorites'
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(db.ForeignKey('user.id'),nullable=False)
    planet_id:Mapped[int] = mapped_column(db.ForeignKey('planets.id'),nullable=True)
    vehicle_id:Mapped[int] = mapped_column(db.ForeignKey('vehicles.id'),nullable=True)
    character_id:Mapped[int] = mapped_column(db.ForeignKey('characters.id'),nullable=True)


    def serialize(self):
        return{
            'id':self.id,
            'user_id':self.user_id,
            'planet_id':self.planet_id,
            'vehicle_id':self.vehicle_id,
            'character_id':self.character_id
      }