from flask import Flask
from flask_restful import fields, marshal_with, reqparse, Resource, Api
from BackEnd.database.manager import Manager
from BackEnd.resources.Producto.Producto import Producto
from BackEnd.resources.Tienda.Tienda import Tienda


post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'nombre_tienda', dest='nombre_tienda',
    location='form', required=True
)
post_parser.add_argument(
    'direccion_tienda', dest='direccion_tienda',
    location='form',
    required=True
)
post_parser.add_argument(
    'categoria', dest='categoria',
    location='form',
    required=True
)
post_parser.add_argument(
    'imagen_portada_tienda', dest='imagen_portada_tienda',
    location='form',
    required=True
)
post_parser.add_argument(
    'contacto', dest='contacto',
    location='form',
    required=True
)

tienda_fields = {
    'id_tienda': fields.Integer,
    'nombre_tienda': fields.String,
    'direccion_tienda': fields.String,
    'categoria': fields.String,
    'imagen_portada_tienda': fields.String,
    'contacto': fields.String
}

db = Manager()
tiendas = db.extraer_todas_tiendas()

class TiendaEndpoint(Resource):

    @marshal_with(tienda_fields)
    def get(self, id_tienda):
        tienda = db.extraer_tienda(id_tienda)
        return tienda

    @marshal_with(tienda_fields)
    def get(self):
        tiendas = db.extraer_todas_tiendas()
        return tiendas

    @marshal_with(tienda_fields)
    def post(self):
        args = post_parser.parse_args()
        tienda = Tienda(args['nombre_tienda'], args['direccion_tienda'], args['categoria'],
                        args['imagen_portada_tienda'], args['contacto'])
        tiendas.append(tienda)
        db.agregar_tienda(tienda)
        return tienda, 200

    def delete(self, id_tienda):
        tienda = db.borrar_tienda(id_tienda)
        tiendas = db.extraer_todas_tiendas()
        return '', 204

app = Flask(__name__)
api = Api(app)
api.add_resource(TiendaEndpoint, '/api/tienda/<int:id_tienda>', '/api/tienda')

if __name__ == '__main__':
    app.run(debug=True)