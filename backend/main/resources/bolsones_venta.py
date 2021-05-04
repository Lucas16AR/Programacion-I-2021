from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModel


class Bolsones_Venta(Resource):

    def get (self, id):
        
        page = 1
        per_page = 10
        bolsones = db.session.query(BolsonModel)

        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == "page":
                    page = int(value)
                elif key == "per_page":
                    per_page = int(value)

        bolsones = bolsones.paginate(page, per_page, True, 30)
        return jsonify({
            "bolsones_venta": [bolson.to_json() for bolson in bolsones.items if bolson.aprobado == 1],
            "total": bolsones.total,
            "pages": bolsones.pages,
            "page": page
        })
        
    

class Bolson_Venta(Resource):

    def get(self, id):
        bolson_venta = db.session.query(BolsonModel).get_or_404(id)
        if bolson_venta.aprobado == 1:
            return bolson_venta.to_json()
        else:
            return "", 404