from flask_restful import fields, marshal_with, Resource
from BackEnd.resources.Producto.Producto import Producto


class ProductoEndpoint(Resource):

    def __init__(self, **kwargs):
        self.db = kwargs['database']
        self.post_parser = kwargs['reqparser']
        self.load_arguments()

    producto_fields = {
        'id_producto': fields.Integer,
        'id_tienda': fields.Integer,
        'nombre_producto': fields.String,
        'descripcion_producto': fields.String,
        'imagen_producto': fields.String,
        'precio_producto': fields.Integer,
    }

    @marshal_with(producto_fields)
    def get(self, id_tienda):
        return self.db.extraer_productos_tienda(id_tienda)

    @marshal_with(producto_fields)
    def post(self, id_tienda):
        args = self.post_parser.parse_args()

        producto = Producto(args['nombre_producto'],
                            args['descripcion_producto'],
                            args['imagen_producto'],
                            args['precio_producto'])

        self.db.agregar_producto(producto, id_tienda)
        return producto, 200

    def delete(self, id_tienda, id_producto):
        self.db.borrar_producto(id_producto, id_tienda)
        return '', 204

    def load_arguments(self):
        self.post_parser.add_argument(
            'nombre_producto', dest='nombre_producto',
            location='form', required=True
        )
        self.post_parser.add_argument(
            'descripcion_producto', dest='descripcion_producto',
            location='form', required=True
        )
        self.post_parser.add_argument(
            'imagen_producto', dest='imagen_producto',
            location='form', required=True
        )
        self.post_parser.add_argument(
            'precio_producto', dest='precio_producto',
            location='form', required=True
        )
