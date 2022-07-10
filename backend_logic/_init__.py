from flask import Flask
from firebase_admin import credentials, initialize_app

cred = credentials.Certificate("backend_logic/secret_key.json")
default_app = initialize_app(
    cred, {'databaseURL': 'https://console.firebase.google.com/project/userintegration-f8858/database/userintegration-f8858-default-rtdb/data/~2F'})


def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '12345rtfescdvf'

    from .userApi import userApi

    app.register_blueprint(userApi, url_prefix="/users")

    return app


