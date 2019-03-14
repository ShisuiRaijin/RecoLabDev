from flask_restful import fields, marshal_with, Resource
from flask_restful import reqparse


class TiendaEndpoint(Resource):

    def __init__(self, **kwargs):
        self.db = kwargs['database']

    tienda_fields = {
        'id_tienda': fields.Integer,
        'nombre_tienda': fields.String,
        'direccion_tienda': fields.String,
        'categoria': fields.String,
        'imagen_portada_tienda': fields.String,
        'contacto': fields.String
    }

    @marshal_with(tienda_fields)
    def get(self, id_tienda):
        if type(id_tienda) is not int:
            return 404
        return self.db.extraer_tienda(id_tienda)

    def delete(self, id_tienda):
        if type(id_tienda) is not int:
            return 404

        status = self.db.borrar_tienda(id_tienda)
        if status is False:
            return 404

        return '', 204
