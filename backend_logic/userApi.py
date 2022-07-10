import uuid
from flask import Blueprint, request, jsonify
from firebase_admin import firestore
from flask_expects_json import expects_json
from jsonschema import ValidationError
from res_validation import required_validation

db = firestore.client()
user_ref = db.collection("pythonUser")

userApi = Blueprint('userAPi', __name__)


@userApi.route('/createUser', methods=['POST'])
@required_validation.required_params({"firstName": str, "lastName": str, "email": str, "phoneNumber": int})
def create():
    try:
        id = uuid.uuid4()
        user_ref.document(id.hex).set(request.json)
        return jsonify({"status": True, "message": f"{id} created successully", }), 201
    except ValidationError as e:
        return jsonify({"status": e.message}), 400
