from BackEnd.database.manager import Manager
from BackEnd.resources.Producto.Producto import Producto
from BackEnd.resources.Tienda.Tienda import Tienda

tienda=Tienda('primer tienda','avenda siempre viav 1234','cosas vaeias','no hay','correo@falso')
producto =Producto('primer producto','soy buen producto','no image',2323)
producto= Producto('segundo produco','soy un mal producto','ruta imagen',3334)
mg=Manager()
mg.agregar_tienda(tienda)
mg.agregar_producto(producto, tienda)
p=mg.extraer_productos_coinciden(3,'buen')

tienda2=Tienda('segunda teinda','otra calle 2','ropa','ruta imagen 2','correo@2')
tienda3=Tienda('tercer tienda','en calle 3','cosmeticos','ruta imagen 3','correo@3')
producto= Producto('segundo produco','soy un mal producto','ruta imagen',3334)

mg.agregar_producto(producto,tienda3)
tienda4=Tienda('cuata tienda','callenumero4', 'pet shop','ruta imagen 4','correo@cuatro')
mg.agregar_tienda(tienda2)
mg.agregar_tienda(tienda3)
mg.agregar_tienda(tienda4)

for el in p:
    print(el)
ts=mg.extraer_todas_tiendas()

print('todas las tiendas.id')
for t in ts:
    print (t.id_tienda)
	
print('todas las tiendas.nombre')
for t in ts:
    print (t.nombre_tienda)
	
print('tienda id=3')
tienda_recuperada=mg.extraer_tienda(3)
print (tienda_recuperada)

tienda_recuperada=mg.extraer_tienda(5)
print('tienda id 5')
print (tienda_recuperada)

print('productos tienda id :3')
pr=mg.extraer_productos_tienda(3)
for el in pr:
	print(el)
	
print('productos que coinciden con -mal producto-')	
pr=mg.extraer_productos_coinciden(4,'mal producto')
for p in pr:
	print(p)