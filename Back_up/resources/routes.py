from .api import RoutesApi, RouteApi, PathApi

def initialize_routes(api):
    api.add_resource(RoutesApi, '/routes')
    api.add_resource(PathApi, '/path')
    api.add_resource(RouteApi, '/route/<id>')