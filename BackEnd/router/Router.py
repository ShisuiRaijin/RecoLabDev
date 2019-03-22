from BackEnd.database.manager import Manager
from BackEnd.api.Producto.Productos import ProductosEndpoint
from BackEnd.api.Tienda.Tienda import TiendaEndpoint
from BackEnd.api.Producto.Producto import ProductoEndpoint
from BackEnd.api.Tienda.Tiendas import TiendasEndpoint


class Router:

    def __init__(self, api):
        self.api = api
        self.db = {'database': Manager()}
        self.setResources()

    def setResources(self):
        self.api.add_resource(TiendasEndpoint,
                         '/api/tiendas',
                         resource_class_kwargs=self.db)

        self.api.add_resource(TiendaEndpoint,
                         '/api/tiendas/<int:id_tienda>',
                         resource_class_kwargs=self.db)

        self.api.add_resource(ProductosEndpoint,
                         '/api/tiendas/<int:id_tienda>/productos',
                         resource_class_kwargs=self.db)

        self.api.add_resource(ProductoEndpoint,
                         '/api/tiendas/<int:id_tienda>/productos/<int:id_producto>',
                         resource_class_kwargs=self.db)
