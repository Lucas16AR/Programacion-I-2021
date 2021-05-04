from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModel

class Bolsones_Pendientes(Resource):
    
    def get(self):
        bolsones = db.session.query(BolsonModel).filter(BolsonModel.aprobado == 0)
        return jsonify({ 
        'BolsonesPendientes': [bolson.to_json() for bolson in bolsones]
        })

    def post(self):
        bolson_pendiente = BolsonModel.from_json(request.get_json())
        db.session.add(bolson_pendiente)
        db.session.commit()
        return bolson_pendiente.to_json(), 201

class Bolson_Pendiente(Resource):
    def get(self, id):
        bolson_pendiente = db.session.query(BolsonModel).get_or_404(id)
        if bolson_pendiente.aprobado == 0:
            return bolson_pendiente.to_json()
        else:
            return '', 404    


    def delete(self, id):
        bolson_pendiente = db.session.query(BolsonModel).get_or_404(id)
        if bolson_pendiente.aprobado == 0:
            db.session.delete(bolson_pendiente)
            db.session.commit()
            return '', 204
        else:
            return '', 404

    def put(self, id):
        bolson_pendiente = db.session.query(BolsonModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(bolson_pendiente, key, value)
        if bolson_pendiente.aprobado == 0:
            db.session.add(bolson_pendiente)
            db.session.commit()
            return bolson_pendiente.to_json(), 201
        else:
            return '', 404