from .db import db
from marshmallow import Schema, fields

# Airline Model
class airline(db.EmbeddedDocument):
    id = db.IntField(primary_key=True)
    name = db.StringField(required=True)
    alias = db.StringField(required=True)
    iata = db.StringField(required=True)


# Route Model
class routes(db.Document):
    airline = db.EmbeddedDocumentField(airline)
    src_airport = db.StringField(required=True)
    dst_airport = db.StringField(required=True)
    codeshare = db.StringField()
    stops = db.IntField(default=0)
    airplane = db.IntField()
    