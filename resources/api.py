from flask_restful import Resource
from flask import Response, request, jsonify
from database.models import routes, route_schema, path_schema_input , path_schema_output, message_schema
from mongoengine.queryset.visitor import Q
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource

# Path endpoint 

class PathApi(MethodResource, Resource):
    @marshal_with(path_schema_output) 
    @doc(description='Path Endpoint returns first 10 routes betwenn two destinations with one stop' , tags=['path'])
    @use_kwargs(path_schema_input, location=('json'))
    def post(self,**body):
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
class RoutesApi(MethodResource, Resource):
    # Retrive List of all routes
    @marshal_with(route_schema) 
    @doc(description='Get routes Endpoint returns list of routes, default size is 10' , tags=['routes'])
    def get(self):
        page = int(request.args.get('page',1))
        limit = int(request.args.get('limit',10))
        routes_data = routes.objects().paginate(page=page, per_page=limit)
        return Response([route.to_json() for route in routes_data.items], mimetype="application/json", status=200)
    # Add new route
    @marshal_with(route_schema) 
    @doc(description='Post routes Endpoint returns adds a new route to routes list' , tags=['routes'])
    @use_kwargs(route_schema, location=('json'))
    def post(self,**body):
        print(body)
        route = routes(**body).save()
        return Response(route.to_json(), mimetype="application/json", status=200) 

# Route endpoint 
class RouteApi(MethodResource, Resource):
    # Update route
    @marshal_with(message_schema) 
    @doc(description='Put route Endpoint updates a route based on the provided id' , tags=['route'])
    @use_kwargs(route_schema, location=('json'))
    def put(self, id,**body):
        route = routes.objects.get_or_404(id=id)
        route.update(**body)
        return {'message':'sucess'}, 200
    # Delete route
    @marshal_with(message_schema) 
    @doc(description='Delete route Endpoint delete a specific route based on the provided id' , tags=['route'])
    def delete(self, id):
        route = routes.objects.get_or_404(id=id)
        route.delete()
        return  {'message':'sucess'}, 200
    # Retrive route
    @marshal_with(route_schema) 
    @doc(description='Get route Endpoint returns a specific route informations based on the provided id ' , tags=['route'])
    def get(self, id):
        route = routes.objects.get_or_404(id=id)
        return Response(route.to_json(), mimetype="application/json", status=200)
