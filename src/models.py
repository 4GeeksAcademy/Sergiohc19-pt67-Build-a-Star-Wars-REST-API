from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

# Modelo para la tabla de Usuarios
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Clave primaria de tipo entero
    email = db.Column(db.String(120), unique=True, nullable=False)  # Columna para el email, único y obligatorio
    password = db.Column(db.String(80), unique=False, nullable=False)  # Columna para la contraseña, obligatoria
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)  # Columna para indicar si el usuario está activo

    def __repr__(self):
        return '<Users %r>' % self.username  # Representación textual del objeto Users

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # no serializamos la contraseña por motivos de seguridad
        }

# Modelo para la tabla de Personajes
class Personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)  # Clave primaria de tipo entero
    name = db.Column(db.String(250), nullable=False)  # Columna para el nombre del personaje, obligatoria
    eye_color = db.Column(db.String(250), nullable=False)  # Columna para el color de ojos del personaje, obligatoria
    hair_color = db.Column(db.String(250), nullable=False)  # Columna para el color de cabello del personaje, obligatoria

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye_color": self.eye_color,
            "hair_color": self.hair_color,
        }

# Modelo para la tabla de Vehículos
class Vehiculos(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)  # Clave primaria de tipo entero
    name = db.Column(db.String(250), nullable=False)  # Columna para el nombre del vehículo, obligatoria
    model = db.Column(db.String(250), nullable=False)  # Columna para el modelo del vehículo, obligatoria

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
        }

# Modelo para la tabla de Planetas
class Planetas(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)  # Clave primaria de tipo entero
    name = db.Column(db.String(250), nullable=False)  # Columna para el nombre del planeta, obligatoria
    population = db.Column(db.String(250), nullable=False)  # Columna para la población del planeta, obligatoria

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
        }

# Modelo para la tabla de Favoritos de Personajes (relación muchos a muchos entre Usuarios y Personajes)
class Favoritos_personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)  # Clave primaria de tipo entero
    personajes_relacion = db.Column(db.Integer, db.ForeignKey(Personajes.id, ondelete='CASCADE'), nullable=False)  # Clave foránea a Personajes
    usuarios_relacion = db.Column(db.Integer, db.ForeignKey(Users.id, ondelete='CASCADE'), nullable=False)  # Clave foránea a Usuarios

    def serialize(self):
        return {
            "id": self.id,
            "personajes_relacion": self.personajes_relacion,
            "usuarios_relacion": self.usuarios_relacion
        }

# Modelo para la tabla de Favoritos de Vehículos (relación muchos a muchos entre Usuarios y Vehículos)
class Favoritos_vehiculos(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)  # Clave primaria de tipo entero
    vehiculos_relacion = db.Column(db.Integer, db.ForeignKey(Vehiculos.id, ondelete='CASCADE'), nullable=False)  # Clave foránea a Vehiculos
    usuarios_relacion = db.Column(db.Integer, db.ForeignKey(Users.id, ondelete='CASCADE'), nullable=False)  # Clave foránea a Usuarios

    def serialize(self):
        return {
            "id": self.id,
            "vehiculos_relacion": self.vehiculos_relacion,
            "usuarios_relacion": self.usuarios_relacion
        }

# Modelo para la tabla de Favoritos de Planetas (relación muchos a muchos entre Usuarios y Planetas)
class Favoritos_planetas(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)  # Clave primaria de tipo entero
    planetas_relacion = db.Column(db.Integer, db.ForeignKey(Planetas.id, ondelete='CASCADE'), nullable=False)  # Clave foránea a Planetas
    usuarios_relacion = db.Column(db.Integer, db.ForeignKey(Users.id, ondelete='CASCADE'), nullable=False)  # Clave foránea a Usuarios

    def serialize(self):
        return {
            "id": self.id,
            "planetas_relacion": self.planetas_relacion,
            "usuarios_relacion": self.usuarios_relacion
        }
