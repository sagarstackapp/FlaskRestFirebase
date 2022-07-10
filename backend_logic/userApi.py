import uuid
from flask import Blueprint, request, jsonify
from firebase_admin import firestore
from flask_expects_json import expects_json
from jsonschema import ValidationError

db = firestore.client()
user_ref = db.collection("pythonUser")

userApi = Blueprint('userAPi', __name__)

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string"}
    },
    "required": ["email"]
}


@userApi.route('/add', methods=['POST'])
@expects_json(schema)
def create():
    try:
        id = uuid.uuid4()
        user_ref.document(id.hex).set(request.json)
        return jsonify({"status": "{id} created successfully"}), 200
    except ValidationError as e:
        return jsonify({"status": e.message}), 400
