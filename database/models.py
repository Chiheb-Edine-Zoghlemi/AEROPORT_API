from email.policy import default
from .db import db
import mongoengine_goodjson as gj


class Airline(gj.Document):
    id = db.IntField(primary_key=True)
    name = db.StringField(required=True)
    alias = db.StringField(required=True)
    iata = db.StringField(required=True)



class Route(gj.Document):
    id = db.IntField(primary_key=True)
    airline = db.EmbeddedDocumentField(Airline)
    src_airport = db.StringField(required=True)
    dst_airport = db.StringField(required=True)
    codeshare = db.StringField()
    stops = db.IntField(default=0)
    airplane = db.IntField()
    