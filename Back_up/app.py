from flask import Flask
from flask_restful import  Api
from resources.routes import initialize_routes
from flask_cors import CORS
from database.db import initialize_db


# API CONFIG
app = Flask(__name__)
api = Api(app)



# Database connection
app.config['MONGODB_SETTINGS'] = {'host': 'mongodb://localhost:27017/sample'}

# Enbale crossheader 
CORS(app)

# Initialize the database
initialize_db(app)

# Initialize the endpoints 
initialize_routes(api)


# Run the server 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)