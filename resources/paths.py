from .routes import Routes

def initialize_routes(api):
    api.add_resource(Routes, '/routes')