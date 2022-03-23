from .db import db
from marshmallow import Schema, fields


# ################################## Model ################################################
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


# ############################# SCHEMA'S ###############################################
# Path input schema 
class path_schema_input(Schema):
    src_airport = fields.String(required=True, description="Source airport")
    dest_airport = fields.String(required=True, description="Destination airport")


# Path output schema
class path_schema_output(Schema):
    src_airport = fields.String(required=True, description="Source airport")
    stop_airport = fields.String(required=True, description="Stop airport")
    dest_airport = fields.String(required=True, description="Destination airport")


# Airline input schema
class airline_schema(Schema):
    id = fields.Integer(description="Aireline ID ")
    name = fields.String(description="Name")
    alias = fields.String(description="Alias")
    iata = fields.String(description="Iata")


# Route input schema
class route_schema(Schema):
    airline = fields.Nested(airline_schema)
    src_airport = fields.String(required=True, description="Source airport")
    dst_airport = fields.String(required=True, description="Destination airport")
    codeshare = fields.String(description="Codeshare")
    stops = fields.Integer(description="Number of stops", default=0)
    airplane = fields.Integer(description="Airplane number ")


class message_schema(Schema):
    message = fields.String(description="Message with the status")


class routes_schema(Schema):
    limit = fields.Integer(description="Number of routes to return")
    page = fields.Integer(description="Page number to return")
