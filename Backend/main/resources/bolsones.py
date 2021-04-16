from flask_restful import Resource
from flask import request

BOLSONES = {
    0: {'nombreBolson': 'bolsonTipo1'},
    1: {'nombreBolson': 'bolsonTipo2'},
    2: {'nombreBolson': 'bolsonTipo3'}
}

class Bolsones(Resource):
    def get(self):
        return BOLSONES

class Bolson(Resource):
    def get(self, id):
        if int(id) in BOLSONES:
            return BOLSONES[int(id)]
        return '', 404