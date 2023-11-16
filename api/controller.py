from json import dumps
from bson import json_util
from bottle import Bottle, request, response, template
from jwt_bottle import auth_required
from data.database import insert_admeasurement, get_admeasurement_interval
from pprint import pprint

def create_controllers(app: Bottle):

    @auth_required
    @app.post("/admeasurement")
    def insert_admeasurement_route(user):
        json = dict(request.json)
        try:
            inserted_id = insert_admeasurement(**json)
            if str(inserted_id) != None and str(inserted_id) != "":
                response_data = {
                    'message': 'Medição inserida com sucesso.',
                    '_id': str(inserted_id)
                }
                response.status = 200
                response.content_type = "application/json"
                return dumps(response_data)
        except Exception as e:
            response_data = {
                'message': str(e),
                '_id': 0,
            }
            response.status = 500
            return dumps(response_data)
        

    @app.get("/admeasurement")
    def get_admeasurement():
        params = dict(request.query)
        variable_id = params['variable_id'] if 'variable_id' in params else 0
        start = params['start'] if 'start' in params else None
        end = params['end'] if 'end' in params else None
        list_admeasurement = get_admeasurement_interval(variable_id, start, end)
        response.status = 200
        response.content_type = "application/json"
        return json_util.dumps(list_admeasurement)

