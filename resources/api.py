from flask_restful import Resource
from flask import Response, request
from database.models import routes

# Routes endpoint
class RoutesApi(Resource):
    # Retrive List of all routes
    def get(self):
        routes_data = routes.objects().to_json()
        return Response(routes_data, mimetype="application/json", status=200)
    # Add new route
    def post(self):
        body = request.get_json()
        route = routes(**body).save()
        id = route.id
        return Response({'id': str(id)}, mimetype="application/json", status=200) 

# Route endpoint 
class RouteApi(Resource):
    # Update route
    def put(self, id):
        body = request.get_json()
        routes.objects.get(id=id).update(**body)
        return '', 200
    # Delete route
    def delete(self, id):
        route = routes.objects.get(id=id).delete()
        return Response('', status=200) 
    # Retrive route
    def get(self, id):
        route = routes.objects.get(id=id).to_json()
        return Response(route, mimetype="application/json", status=200)
