from flask_restful import Resource
from flask import Response, request, jsonify
from database.models import routes
from mongoengine.queryset.visitor import Q
# Path endpoint 
class PathApi(Resource):
    def post(self):
        body = request.get_json()
        if body.get('src_airport') and body.get('dest_airport'):
            src = body.get('src_airport')
            dest = body.get('dest_airport')
            # get all the routes which shares the same source as the source input
            routres_src = routes.objects(src_airport=src).values_list('dst_airport')
            # get all the routes which have the same destination as the request destination and also have a source from the previous query
            routres_src = routes.objects(Q(src_airport__in=routres_src) & Q(dst_airport=dest))[:10].values_list('src_airport')
            # creating the output json
            result = []
            for x in  routres_src:
                body['stop_airport']=x
                result.append(body)
            response = jsonify(result)
            response.status_code = 200
            return response
        else:
            return Response({'message':'Unvalid Request Body'}, status=401) 
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
        route = routes.objects.first_or_404(id=id)
        return Response(route.to_json(), mimetype="application/json", status=200)
