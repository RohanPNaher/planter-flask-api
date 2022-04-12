import profile
from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.garden import Garden

gardens = Blueprint('gardens', 'gardens')

# Make Garden
@gardens.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]
  garden = Garden(**data)
  db.session.add(garden)
  db.session.commit()
  return jsonify(garden.serialize()), 201

# All Gardens
@gardens.route('/', methods=["GET"])
def index():
  gardens = Garden.query.all()
  return jsonify([garden.serialize() for garden in gardens]), 200

# Single Specific Garden
@gardens.route('/<id>', methods=["GET"])
def show(id):
  garden = Garden.query.filter_by(id=id).first()
  garden_data = garden.serialize()
  return jsonify(garden=garden_data), 200

# Update Specific Garden
@gardens.route('/<id>', methods=["PUT"]) 
@login_required
def update(id):
  data = request.get_json()
  profile = read_token(request)
  garden = Garden.query.filter_by(id=id).first()

  if garden.profile_id != profile["id"]:
    return 'Forbidden', 403

  for key in data:
    setattr(garden, key, data[key])

  db.session.commit()
  return jsonify(garden.serialize()), 200

# Delete a specific Garden
@gardens.route('/<id>', methods=["DELETE"]) 
@login_required
def delete(id):
  profile = read_token(request)
  garden = Garden.query.filter_by(id=id).first()

  if garden.profile_id != profile["id"]:
    return 'Forbidden', 403

  db.session.delete(garden)
  db.session.commit()
  return jsonify(message="Success"), 200