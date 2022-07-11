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
@required_validation.required_params({"id": str, "firstName": str, "lastName": str, "email": str, "phoneNumber": int})
def create():
    # try:
    id = request.json['id']
    user_ref.document(id).set(request.json)
    return jsonify({"status": True, "message": f"{id} created successully", }), 201
    # except ValidationError as e:
    #     return jsonify({"status": e.message}), 400


@userApi.route('/', methods=['GET'])
def read():
    try:
        id = request.args.get("id")
        if id:
            userData = user_ref.document(id).get()
            if userData.exists:
                return jsonify({'status': True, 'data': userData.to_dict(), 'message': 'Record fetched successfully'}), 200
            else:
                return jsonify({'status': False, 'data': [], 'message': 'No records found'}), 200
        else:
            userData = [doc.to_dict() for doc in user_ref.stream()]
            return jsonify({'status': True, 'data': userData, 'message': 'Records fetched successfully'}), 200
    except ValidationError as e:
        return jsonify({'status': e.message}), 400
