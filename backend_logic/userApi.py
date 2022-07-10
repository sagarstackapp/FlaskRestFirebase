import uuid
from flask import Blueprint, request, jsonify
from firebase_admin import firestore

db = firestore.client()
user_ref = db.collection("pythonUser")

userApi = Blueprint('userAPi', __name__)


@userApi.route('/add', methods=['POST'])
def create():
    try:
        id = uuid.uuid4()
        user_ref.document(id.hex).set(request.json)
        return jsonify({"status": "{id} created successfully"}), 200
    except Exception as e:
        return f"An error : {e}"
