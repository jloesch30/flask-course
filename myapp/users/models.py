from mongoengine import *
from mongoengine.fields import BooleanField, DateTimeField, EmailField, ListField, StringField
from datetime import datetime

class User(Document):
    email = EmailField()
    fname = StringField(max_length=30)
    # last_name = StringField(max_length=30)
    # admin = BooleanField(default=False)
    # registered = BooleanField(default=True)
    # fav_themes = ListField()
    # signed_in = BooleanField(default=True)
    date_created = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'User'
    }