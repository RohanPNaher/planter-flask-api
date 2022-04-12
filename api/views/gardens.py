import profile
from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.garden import Garden

gardens = Blueprint('gardens', 'gardens')

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