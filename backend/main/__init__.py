import os 

from flask import Flask

from dotenv import load_dotenv

from flask_restful import Api

from flask_sqlalchemy import SQLAlchemy

api = Api()

db = SQLAlchemy()

def create_app():
    
    app = Flask(__name__)
    
    load_dotenv()

    PATH = os.getenv("DATABASE_PATH")
    DB_NAME = os.getenv("DATABASE_NAME")
    if not os.path.exists(f'{PATH}{DB_NAME}'):
        os.mknod(f'{PATH}{DB_NAME}')

    app.config['SQLALCHEMY_TRUCK_MODIFICATIONS'] = False

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{PATH}{DB_NAME}'
    
    db.init_app(app)

    import main.resources as resources

    api.add_resource(resources.BolsonesResources, '/bolsones')
    api.add_resource(resources.BolsonResources, '/bolson/<id>')
    api.add_resource(resources.BolsonesVentaResources, '/bolsones-venta')
    api.add_resource(resources.BolsonVentaResources, '/bolson-venta/<id>')
    api.add_resource(resources.BolsonesPendientesResources, '/bolsones-pendientes')
    api.add_resource(resources.BolsonPendienteResources, '/bolson-pendiente/<id>')
    api.add_resource(resources.BolsonesPreviosResources, '/bolsones-previos')
    api.add_resource(resources.BolsonPrevioResources, '/bolson-previo/<id>')
    api.add_resource(resources.ProductosResources, '/productos')
    api.add_resource(resources.ProductoResources, '/producto/<id>')
    api.add_resource(resources.ComprasResources, '/compras')
    api.add_resource(resources.CompraResources, '/compra/<id>')
    api.add_resource(resources.ClientesResources, '/clientes')
    api.add_resource(resources.ClienteResources, '/cliente/<id>')
    api.add_resource(resources.ProveedoresResources, '/proveedores')
    api.add_resource(resources.ProveedorResources, '/proveedor/<id>')

    api.init_app(app)

    return app