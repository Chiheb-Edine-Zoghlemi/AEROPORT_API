from flask import Flask
from flask_restful import  Api
from resources.paths import initialize_routes
from flask_cors import CORS
from database.db import initialize_db
from dotenv import load_dotenv
import os


# ###################################################
# API CONFIG
load_dotenv()
app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = os.environ.get("api-token")
app.config['MONGODB_SETTINGS'] = {'host': 'mongodb://localhost/sample'}
CORS(app)
initialize_db(app)
initialize_routes(api)
# ###################################################



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)