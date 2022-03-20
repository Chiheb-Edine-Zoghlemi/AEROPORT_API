from .api import RoutesApi, RouteApi

def initialize_routes(api):
    api.add_resource(RoutesApi, '/routes')
    api.add_resource(RouteApi, '/route/<id>')