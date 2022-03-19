from mongoengine import MongoEngine

db = MongoEngine()

def initialize_db(app):
    db.init_app(app)