"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Personajes, Vehicles, Planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    users = User.query.all()
    users_serialized = list(map(lambda item:item.serialize(), users))
    print(users_serialized)
    

    response_body = {
        "msg": "ok",
        "data": users_serialized,
    }

    return jsonify(response_body), 200



@app.route('/personajes', methods=['GET'])
def get_personajes():

    personajes = Personajes.query.all()
    personajes_serialized = list(map(lambda item:item.serialize(), personajes))
    print(personajes_serialized)
    
    response_body = {
        "msg": "ok",
        "data": personajes_serialized,
    }

    return jsonify(response_body), 200


@app.route('/vehicles', methods=['GET'])
def get_vehicles():

    vehicles = Vehicles.query.all()
    vehicles_serialized = list(map(lambda item:item.serialize(), vehicles))
    print(vehicles_serialized)
    

    response_body = {
        "msg": "ok",
        "data": vehicles_serialized,
    }

    return jsonify(response_body), 200






@app.route('/planets', methods=['GET'])
def get_planets():

    planets = Planets.query.all()
    planets_serialized = list(map(lambda item:item.serialize(), planets))
    print(planets_serialized)
    

    response_body = {
        "msg": "ok",
        "data": planets_serialized,
    }

    return jsonify(response_body), 200









# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
