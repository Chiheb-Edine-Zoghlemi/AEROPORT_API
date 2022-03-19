from flask_restful import Resource
from flask import Response
from database.models import Routes

class Routes(Resource):
    def get(self):
        routes = Routes.objects().to_json()
        return Response(routes, mimetype="application/json", status=200)

