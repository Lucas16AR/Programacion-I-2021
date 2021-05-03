from flask_restful import Resource
from flask import request
from .. import db
from main.models import BolsonModel

class Bolsones(Resource):
    def get(self,):
        bolsones = db.session.query(BolsonModel).all()
        return jsonify([bolson.to_json() for bolson in bolsones])

class Bolson(Resource):
    def get(self, id):
        bolson = db.session.query(BolsonModel).get_or_404(id)
        return bolson.to_json()