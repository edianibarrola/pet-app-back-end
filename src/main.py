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
from models import db, User, Pet

from flask_jwt_simple import (JWTManager, jwt_required, create_jwt, get_jwt_identity)
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,get_jwt_identity)
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/signup', methods=['POST']) #Adds a user to the list when the user signs up
def sign_up():
    body = request.get_json() 
    info = User(username=body['username'], email=body['email'], password=body['password'], is_active=False) 
    db.session.add(info) 
    db.session.commit() 
    updated_user = User.query.filter_by(email=body['email']).first() 
    updated_user = updated_user.serialize()
    return jsonify(updated_user), 200 

@app.route('/user/<int:id>', methods=['DELETE']) #Deletes a user at the specific ID
def delete_user(id):
    body = request.get_json()
    to_be_deleted = User.query.get(id)
    db.session.delete(to_be_deleted)
    db.session.commit()
    response_body = {
        "msg": "The user has been deleted."
    }
    return jsonify(response_body), 200

@app.route('/users', methods=['GET']) #Returns all of the users in a list
def get_all_users():
    all_users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), all_users))
    response_body = {
        "msg": "Here are all of the users."
    }
    return jsonify(all_users), 200

@app.route('/user/<int:id>', methods=['PUT']) #Updates the user's information at their ID
def update_user(id):
    body = request.get_json()
    to_be_updated = User.query.get(id)
    if to_be_updated is None:
        raise APIException('User does not exist', status_code=404)
    if 'email' in body:
        to_be_updated.username = body['username']
        to_be_updated.email = body['email']
        to_be_updated.password = body['password']
    db.session.commit()
    to_be_updated = User.query.get(id)
    to_be_updated = to_be_updated.serialize()
    response_body = {
        "msg": "The user has been updated.",
        "update": to_be_updated
    }
    return jsonify(response_body), 200

@app.route('/user/<int:id>', methods=['GET']) #Gets the user's information at their ID
def get_one_user(id):
    grab_info = User.query.get(id)
    grab_info = grab_info.serialize()
    return jsonify(grab_info), 200


@app.route('/login', methods=['POST']) #Sets the is_active to true when the user logs in
def login_user():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    params = request.get_json()
    email = params.get('email', None)
    password = params.get('password', None)
    if not email:
        return jsonify({"msg": "Missing email parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400
    user = User.query.filter_by(email=email, password=password).first()
    if user is None:
        return jsonify({"msg": "Bad email or password"}), 401
    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=email)
    user.is_active = True
    db.session.commit()
    return jsonify(access_token=access_token, id=user.id), 200

@app.route('/logout', methods=['PUT']) #Sets the is_active to false when the user logs out
def logout_user():
    body = request.get_json()
    to_be_updated = User.query.filter_by(email=body['email']).first()
    if to_be_updated is None:
        raise APIException('User does not exist', status_code=404)
    if 'email' in body:
        to_be_updated.is_active = False
    db.session.commit()
    response_body = {
        "msg": "The user has logged out.",
    }
    return jsonify(response_body), 200


@app.route('/pet', methods=['GET']) #Returns all of the pets in a list
def get_all_pets():
    all_pets = Pet.query.all()
    all_pets = list(map(lambda x: x.serialize(), all_pets))
    response_body = {
        "Pets": all_pets
    }
    return jsonify(all_pets), 200

@app.route('/pet', methods=['POST']) #Adds a new pet to the list 
def add_pet():
    pet_info = request.get_json() 
    new_pet= Pet(name=pet_info['name'], pet_type= pet_info['pet_type'], sex=pet_info['sex'], color=pet_info['color'], dob=pet_info['dob'], habitat_id=pet_info['habitat_id'], note=pet_info['note']) 
    db.session.add(new_pet) 
    db.session.commit() 
    response = Pet.query.all()
    response = list(map(lambda x: x.serialize(), response))
    
    return jsonify(response), 200 
#For the posts

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
