from flask_mongoengine import MongoEngine
# Initialize the mongoDB engine
db = MongoEngine()
# Initialize the database connection
def initialize_db(app):
    db.init_app(app)