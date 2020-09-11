from mongoengine import Document
from datetime import datetime

from myapp.users.models import User
from myapp.themes.models import Theme
from mongoengine.fields import DateTimeField, GeoPointField, ImageField, IntField, ListField, ReferenceField, StringField

class Report(Document):
    title = StringField(max_length=50, required=True)
    author = ReferenceField(User)
    theme = ReferenceField(Theme)
    # image_name = StringField(max_length=100)
    # image = ImageField(thumbnail_size=(150, 150, False))
    # location = GeoPointField() 
    summary = StringField(max_length=200, required=True)
    report_tags = ListField()
    # rating = IntField(min_value=0, max_value=5)
    date_posted = DateTimeField(default=datetime.utcnow)