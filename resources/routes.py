from .api import RoutesApi, RouteApi, PathApi

def initialize_routes(api, docs):
    api.add_resource(RoutesApi, '/routes')
    docs.register(RoutesApi)
    api.add_resource(PathApi, '/path')
    docs.register(PathApi)
    api.add_resource(RouteApi, '/route/<id>')
    docs.register(RouteApi)
    