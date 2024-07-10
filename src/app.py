"""
Este módulo se encarga de iniciar el servidor API, cargar la base de datos y añadir los endpoints.
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Users, Personajes, Vehiculos, Planetas, Favoritos_personajes, Favoritos_vehiculos, Favoritos_planetas

# Crea una instancia de la aplicación Flask
app = Flask(__name__)
app.url_map.strict_slashes = False  # Configura para que las rutas no tengan que terminar en "/" obligatoriamente

# Configuración de la base de datos según la URL especificada en la variable de entorno o usa una base de datos SQLite
db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Deshabilita el seguimiento de modificaciones de SQLAlchemy

# Configuración de Flask-Migrate para manejar las migraciones de la base de datos
MIGRATE = Migrate(app, db)
# Inicializa la instancia de la base de datos con la aplicación Flask
db.init_app(app)
CORS(app)  # Habilita CORS para permitir solicitudes desde cualquier origen
setup_admin(app)  # Configura el panel de administración Flask-Admin

# Manejo/serialización de errores como objetos JSON
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Genera un sitemap con todos los endpoints de la aplicación
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Definición de endpoints POST

@app.route('/users', methods=['POST'])
def create_user():
    body = request.json
    me = Users(name=body["name"], email=body["email"], password=body["password"], is_active=body["is_active"])
    db.session.add(me)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": me.id
    }
    return jsonify(response_body), 200


@app.route('/personajes', methods=['POST'])
def create_personaje():
    body = request.json
    me = Personajes(name=body["name"], eye_color=body["eye_color"], hair_color=body["hair_color"])
    db.session.add(me)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": me.id
    }
    return jsonify(response_body), 200


@app.route('/vehiculos', methods=['POST'])
def create_vehiculo():
    body = request.json
    me = Vehiculos(name=body["name"], model=body["model"])
    db.session.add(me)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": me.id
    }
    return jsonify(response_body), 200


@app.route('/planetas', methods=['POST'])
def create_planeta():
    body = request.json
    me = Planetas(name=body["name"], population=body["population"])
    db.session.add(me)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": me.id
    }
    return jsonify(response_body), 200


@app.route('/favoritos_personajes', methods=['POST'])
def create_favorito_personaje():
    body = request.json
    me = Favoritos_personajes(personajes_relacion=body["personajes_relacion"], usuarios_relacion=body["usuarios_relacion"])
    db.session.add(me)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": me.id
    }
    return jsonify(response_body), 200


@app.route('/favoritos_vehiculos', methods=['POST'])
def create_favorito_vehiculo():
    body = request.json
    me = Favoritos_vehiculos(vehiculos_relacion=body["vehiculos_relacion"], usuarios_relacion=body["usuarios_relacion"])
    db.session.add(me)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": me.id
    }
    return jsonify(response_body), 200


@app.route('/favoritos_planetas', methods=['POST'])
def create_favorito_planeta():
    body = request.json
    me = Favoritos_planetas(planetas_relacion=body["planetas_relacion"], usuarios_relacion=body["usuarios_relacion"])
    db.session.add(me)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": me.id
    }
    return jsonify(response_body), 200

# Definición de endpoints GET

@app.route('/users', methods=['GET'])
def get_all_users():
    users = Users.query.all()  # Consulta todos los usuarios en la base de datos
    users_serialized = list(map(lambda item:item.serialize(), users))  # Serializa la lista de usuarios

    response_body = {
        "msg": "OK",
        "data": users_serialized  # Retorna los usuarios serializados en la respuesta
    }

    return jsonify(response_body), 200  # Retorna la respuesta en formato JSON con el código de estado 200


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = Users.query.filter_by(id=user_id).first()  # Consulta un usuario por su ID en la base de datos
    user_serialize = user.serialize()  # Serializa el usuario encontrado

    response_body = {
        "msg": "Ok",
        "data": user_serialize  # Retorna el usuario serializado en la respuesta
    }

    return jsonify(response_body), 200  # Retorna la respuesta en formato JSON con el código de estado 200


@app.route('/users/favorites', methods=['GET'])
def get_users_favorites():
    users = Users.query.all()  # Consulta todos los usuarios en la base de datos
    users_serialized = list(map(lambda item:item.serialize(), users))  # Serializa la lista de usuarios

    response_body = {
        "msg": "OK",
        "data": users_serialized  # Retorna los usuarios serializados en la respuesta
    }

    return jsonify(response_body), 200  # Retorna la respuesta en formato JSON con el código de estado 200


@app.route('/personajes', methods=['GET'])
def handle_personajes():
    personajes = Personajes.query.all()  # Consulta todos los personajes en la base de datos
    personajes_serialized = list(map(lambda item:item.serialize(), personajes))  # Serializa la lista de personajes

    response_body = {
        "msg": "OK",
        "data": personajes_serialized  # Retorna los personajes serializados en la respuesta
    }

    return jsonify(response_body), 200  # Retorna la respuesta en formato JSON con el código de estado 200


@app.route('/personajes/<int:personaje_id>', methods=['GET'])
def get_personaje_by_id(personaje_id):
    personaje = Personajes.query.filter_by(id=personaje_id).first()  # Consulta un personaje por su ID en la base de datos
    personaje_serialize = personaje.serialize()  # Serializa el personaje encontrado

    response_body = {
        "msg": "Ok",
        "data": personaje_serialize  # Retorna el personaje serializado en la respuesta
    }

    return jsonify(response_body), 200  # Retorna la respuesta en formato JSON con el código de estado 200


@app.route('/vehiculos', methods=['GET'])
def handle_vehiculos():
    vehiculos = Vehiculos.query.all()  # Consulta todos los vehículos en la base de datos
    vehiculos_serialized = list(map(lambda item:item.serialize(), vehiculos))  # Serializa la lista de vehículos

    response_body = {
        "msg": "OK",
        "data": vehiculos_serialized  # Retorna los vehículos serializados en la respuesta
    }

    return jsonify(response_body), 200  # Retorna la respuesta en formato JSON con el código de estado 200


@app.route('/vehiculo/<int:vehiculo_id>', methods=['GET'])
def get_vehiculo_by_id(vehiculo_id):
    vehiculo = Vehiculos.query.filter_by(id=vehiculo_id).first()  # Consulta un vehículo por su ID en la base de datos
    vehiculo_serialize = vehiculo.serialize()  # Serializa el vehículo encontrado

    response_body = {
        "msg": "Ok",
        "data": vehiculo_serialize  # Retorna el vehículo serializado en la respuesta
    }

    return jsonify(response_body), 200  # Retorna la respuesta en formato JSON con el código de estado 200


@app.route('/planetas', methods=['GET'])
def handle_planetas():
    planetas = Planetas.query.all()  # Consulta todos los planetas en la base de datos
    planetas_serialized = list(map(lambda item:item.serialize(), planetas))  # Serializa la lista de planetas

    response_body = {
        "msg": "OK",
        "data": planetas_serialized  # Retorna los planetas serializados en la respuesta
    }

    return jsonify(response_body), 200  # Retorna la respuesta en formato JSON con el código de estado 200


@app.route('/planeta/<int:planeta_id>', methods=['GET'])
def get_planeta_by_id(planeta_id):
    planeta = Planetas.query.filter_by(id=planeta_id).first()  # Consulta un planeta por su ID en la base de datos
    planeta_serialize = planeta.serialize()  # Serializa el planeta encontrado

    response_body = {
        "msg": "Ok",
        "data": planeta_serialize  # Retorna el planeta serializado en la respuesta
    }

    return jsonify(response_body), 200  # Retorna la respuesta en formato JSON con el código de estado 200


# Definición de endpoints DELETE

@app.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = Users.query.get(user_id)  # Consulta un usuario por su ID en la base de datos
    if user is None:
        return "User not found", 404  # Retorna un mensaje de error si el usuario no se encuentra

    db.session.delete(user)  # Elimina el usuario de la sesión de la base de datos
    db.session.commit()  # Confirma la transacción en la base de datos
    return jsonify({'message': 'User deleted'}), 200  # Retorna la respuesta en formato JSON con el código de estado 200


@app.route('/favorite/personaje/<int:personaje_id>', methods=['DELETE'])
def delete_personaje_by_id(personaje_id):
    personaje = Personajes.query.get(personaje_id)  # Consulta un personaje por su ID en la base de datos
    if personaje is None:
        return "Personaje not found", 404  # Retorna un mensaje de error si el personaje no se encuentra

    db.session.delete(personaje)  # Elimina el personaje de la sesión de la base de datos
    db.session.commit()  # Confirma la transacción en la base de datos
    response_body = {
        "msg": "Personaje deleted",        
    }

    return jsonify(response_body), 200  # Retorna la respuesta en formato JSON con el código de estado 200


@app.route('/favorite/vehiculo/<int:vehiculo_id>', methods=['DELETE'])
def delete_vehiculo_by_id(vehiculo_id):
    vehiculo = Vehiculos.query.get(vehiculo_id)  # Consulta un vehículo por su ID en la base de datos
    if vehiculo is None:
        return "Vehiculo not found", 404  # Retorna un mensaje de error si el vehículo no se encuentra

    db.session.delete(vehiculo)  # Elimina el vehículo de la sesión de la base de datos
    db.session.commit()  # Confirma la transacción en la base de datos
    response_body = {
        "msg": "Vehiculo deleted",        
    }

    return jsonify(response_body), 200  # Retorna la respuesta en formato JSON con el código de estado 200


@app.route('/favorite/planeta/<int:planeta_id>', methods=['DELETE'])
def delete_planeta_by_id(planeta_id):
    planeta = Planetas.query.get(planeta_id)  # Consulta un planeta por su ID en la base de datos
    if planeta is None:
        return "Planeta not found", 404  # Retorna un mensaje de error si el planeta no se encuentra

    db.session.delete(planeta)  # Elimina el planeta de la sesión de la base de datos
    db.session.commit()  # Confirma la transacción en la base de datos
    response_body = {
        "msg": "Planeta deleted",        
    }

    return jsonify(response_body), 200  # Retorna la respuesta en formato JSON con el código de estado 200


# Este bloque solo se ejecuta si se ejecuta `$ python src/app.py`
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))  # Obtiene el puerto del sistema operativo o usa el puerto 3000 por defecto
    app.run(host='0.0.0.0', port=PORT, debug=False)  # Ejecuta la aplicación Flask en el puerto especificado
