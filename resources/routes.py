from .api import RoutesApi, RouteApi, PathApi, DocsApi

def initialize_routes(api):
    api.add_resource(RoutesApi, '/routes')
    api.add_resource(PathApi, '/path')
    api.add_resource(RouteApi, '/route/<id>')
    api.add_resource(DocsApi, '/docs/<path>')