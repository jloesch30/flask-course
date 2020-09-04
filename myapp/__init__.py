from flask import Flask
from mongoengine import connect
import pyrebase

import secrets

# config = {
#     "apiKey": "AIzaSyD7MhevIYaHPQJGfK7ou9Ny2pqWQhjhfBw",
#     "authDomain": "flaskcourse.firebaseapp.com",
#     "databaseURL": "https://flaskcourse.firebaseio.com",
#     "projectId": "flaskcourse",
#     "storageBucket": "flaskcourse.appspot.com",
#     "messagingSenderId": "694661421387",
#     "appId": "1:694661421387:web:9d6630557ff3401f5df0ce",
#     "measurementId": "G-4KFNC0M75M"
# }

# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()

def create_app():
    app = Flask(__name__)
    app.secret_key = secrets.token_urlsafe(16)

    # use mongoengine to connect with MongoAtlas server
    connect('fc', host='mongodb+srv://jloesch30:xmuki9sy2lfkeJoL@cluster0.ozs7j.mongodb.net/test?authSource=admin&replicaSet=atlas-ztemj6-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
    print('connection made')

    # pull in packages
    from myapp.main.routes import main
    from myapp.reports.routes import reports
    from myapp.users.routes import users
    from myapp.themes.routes import themes

    # register the blueprints here
    app.register_blueprint(users)
    app.register_blueprint(themes)
    app.register_blueprint(main)
    app.register_blueprint(reports)

    return app
