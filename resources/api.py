from flask_restful import Resource
from flask import Response, request, jsonify
from database.models import routes, route_schema, path_schema_input, path_schema_output, message_schema, routes_schema
from mongoengine.queryset.visitor import Q
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource


# Path endpoint 

class PathApi(MethodResource, Resource):
    @marshal_with(path_schema_output, description='Everything is fine!', code=200)
    @marshal_with(message_schema, description='Wrong  body request ', code=401)
    @doc(description='Path Endpoint returns first 10 routes between two destinations with one stop', tags=['path'])
    @use_kwargs(path_schema_input, location='json')
    def post(self, **body):
        if body.get('src_airport') and body.get('dest_airport'):
            src = body.get('src_airport')
            dest = body.get('dest_airport')
            # get all the routes which shares the same source as the source input
            route_src = routes.objects(src_airport=src).values_list('dst_airport')
            # get all the routes which have the same destination as the request destination and also have a source 
            # from the previous query 
            route_src = routes.objects(Q(src_airport__in=route_src) & Q(dst_airport=dest))[:10].values_list(
                'src_airport')
            # creating the output json
            result = []
            for x in route_src:
                body['stop_airport'] = x
                result.append(body)
            response = jsonify(result)
            response.status_code = 200
            return response
        else:
            return Response({'message': 'Invalid Request Body'}, status=401)


# Routes endpoint

class RoutesApi(MethodResource, Resource):
    # Retrieve List of all routes
    @marshal_with(route_schema, description='Routes are fetched  successfully ', code=200)
    @marshal_with(message_schema, description='Error while fetching the data', code=500)
    @use_kwargs(routes_schema, location='headers')
    @doc(description='Get routes Endpoint returns list of routes, default size is 10', tags=['routes'])
    def get(self, **args):
        try:
            page = int(args.get('page', 1))
            limit = int(args.get('limit', 10))
            routes_data = routes.objects().paginate(page=page, per_page=limit)
            return Response([route.to_json() for route in routes_data.items], mimetype="application/json", status=200)
        except Exception as e:
            return {'message': e}, 500

    # Add new route
    @marshal_with(route_schema, description='Route has been added successfully ', code=200)
    @marshal_with(message_schema, description='Error while adding the new route ', code=500)
    @doc(description='Post routes Endpoint returns adds a new route to routes list', tags=['routes'])
    @use_kwargs(route_schema, location='json')
    def post(self, **body):
        try:
            route = routes(**body).save()
            return Response(route.to_json(), mimetype="application/json", status=200)
        except Exception as e:
            return {'message': e}, 500


# Route endpoint


class RouteApi(MethodResource, Resource):
    # Update route
    @marshal_with(message_schema, description='Everything is perfect :)', code=200)
    @marshal_with(message_schema, description='Route Not found', code=404)
    @marshal_with(message_schema, description='Error while Updating existing  route ', code=500)
    @doc(description='Put route Endpoint updates a route based on the provided id', tags=['route'])
    @use_kwargs(route_schema, location='json')
    def put(self,**body):
        id_route = body.pop('id')
        try:
            route = routes.objects.get_or_404(id=id_route)
            route.update(**body)
           
            return {'message': 'success'}, 200

        except Exception as e:
            return {'message': e}, 500

    # Delete route
    @marshal_with(message_schema, description='Everything is perfect :)', code=200)
    @marshal_with(message_schema, description='Route Not found', code=404)
    @marshal_with(message_schema, description='Error while Deleting   route ', code=500)
    @doc(description='Delete route Endpoint delete a specific route based on the provided id', tags=['route'])
    def delete(self, **args):
        try:
            route = routes.objects.get_or_404(id=args.get('id'))
            route.delete()
            return {'message': 'success'}, 200
        except Exception as e:
            return {'message': e}, 500

    # Retrieve route
    @marshal_with(route_schema, description='Everything is perfect :)', code=200)
    @marshal_with(message_schema, description='Route Not found', code=404)
    @marshal_with(message_schema, description='Error while fetching   route data ', code=500)
    @doc(description='Get route Endpoint returns a specific route information\'s based on the provided id ',
         tags=['route'])
    def get(self, **args):
        try:
            route = routes.objects.get_or_404(id=args.get('id'))
            return Response(route.to_json(), mimetype="application/json", status=200)
        except Exception as e:
            return {'message': e}, 500
