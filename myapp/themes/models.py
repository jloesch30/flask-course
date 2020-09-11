from mongoengine import *
from datetime import datetime
from mongoengine.fields import DateTimeField, ImageField, StringField

class Theme(Document):
    theme_name = StringField(max_length=50, required=True)
    theme_desc = StringField(max_length=200, required=True)
    # image = ImageField()
    date_posted = DateTimeField(default=datetime.utcnow)