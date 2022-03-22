from flask import Flask
from flask_restful import  Api
from resources.routes import initialize_routes
from flask_cors import CORS
from database.db import initialize_db
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec


# API CONFIG
app = Flask(__name__ )
api = Api(app)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Awesome Project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON 
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)

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