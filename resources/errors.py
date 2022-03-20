class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class UpdatingRouteError(Exception):
    pass

class UpdatingRouteError(Exception):
    pass

class DeletingRouteError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "UpdatingRouteError": {
         "message": "Updating route added by other is forbidden",
         "status": 403
     },
     "DeletingRouteError": {
         "message": "Deleting route added by other is forbidden",
         "status": 403
     },
     "RouteNotExistsError": {
         "message": "Route with given id doesn't exists",
         "status": 400
     }
}