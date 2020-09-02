from flask import Flask
from mongoengine import connect

import secrets

def create_app():
    app = Flask(__name__)
    app.secret_key = secrets.token_urlsafe(16)

    # use mongoengine to connect with MongoAtlas server
    connect('fc', host='mongodb+srv://jloesch30:xmuki9sy2lfkeJoL@cluster0.ozs7j.mongodb.net/test?authSource=admin&replicaSet=atlas-ztemj6-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
    print('connection made')

    # register blueprints
    

