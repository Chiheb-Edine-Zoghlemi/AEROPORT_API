from flask_restful import Resource
from flask import Response, request
from database.models import routes


# Routes endpoint
class RoutesApi(Resource):
    # Retrive List of all routes
    def get(self):
        page = int(request.args.get('page',1))
        limit = int(request.args.get('limit',10))
        routes_data = routes.objects().paginate(page=page, per_page=limit)
        return Response([route.to_json() for route in routes_data.items], mimetype="application/json", status=200)
    # Add new route
    def post(self):
        body = request.get_json()
        route = routes(**body).save()
        return Response(route.to_json(), mimetype="application/json", status=200) 

# Route endpoint 
class RouteApi(Resource):
    # Update route
    def put(self, id):
        body = request.get_json()
        route = routes.objects.get_or_404(id=id)
        route.update(**body)
        return '', 200
    # Delete route
    def delete(self, id):
        route = routes.objects.get_or_404(id=id)
        route.delete()
        return '', 200
    # Retrive route
    def get(self, id):
        route = routes.objects.get_or_404(id=id)
        return Response(route.to_json(), mimetype="application/json", status=200)
