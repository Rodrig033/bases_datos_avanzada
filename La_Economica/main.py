from modelos.producto import Producto, Categoria, Proveedor
from modelos.cliente import Cliente
from modelos.venta import Venta
from persistencia.base_datos import BaseDatos
from servicios.productos import ServicioProductos
from servicios.ventas import ServicioVentas
from consultas.consultas import Consultas

def main():
 """Ejecuta las operaciones principales de la tienda."""
# Inicialización

base_datos = BaseDatos()

servicio_productos = ServicioProductos(base_datos)
servicio_ventas = ServicioVentas(base_datos)
consultas = Consultas(base_datos)

# Creación de productos

producto1 = Producto(
    "P001",
    "Arroz",
    "Arroz blanco de 1 kg",
    35.0,
    20,
    None
)

producto2 = Producto(
    "P002",
    "Frijol",
    "Frijol negro de 1 kg",
    42.0,
    15,
    None
)

producto3 = Producto(
    "P003",
    "Lentejas",
    "Lentejas de 500 g",
    30.0,
    10,
    None
)

# Registrar productos

servicio_productos.registrar_producto(producto1)
servicio_productos.registrar_producto(producto2)
servicio_productos.registrar_producto(producto3)

# Actualización inicial del inventario

servicio_productos.actualizar_inventario("P001", 10)
servicio_productos.actualizar_inventario("P001", -5)

# Crear categoría

categoria = Categoria(
    "CAT001",
    "Granos",
    "Productos alimenticios de grano"
)

categoria.agregar_producto(producto1)
categoria.agregar_producto(producto2)
categoria.agregar_producto(producto3)

base_datos.raiz.categorias[categoria.id_categoria] = categoria
base_datos.guardar()

# Crear proveedor

proveedor = Proveedor(
    "PROV001",
    "Distribuidora Central",
    "2281234567",
    "contacto@distribuidoracentral.com",
    "Xalapa, Veracruz"
)

# Cerrar y reabrir para trabajar con
# objetos persistentes de la conexión actual

base_datos.cerrar()

base_datos = BaseDatos()

servicio_productos = ServicioProductos(base_datos)
servicio_ventas = ServicioVentas(base_datos)
consultas = Consultas(base_datos)

producto1_bd = base_datos.raiz.productos.get("P001")
producto2_bd = base_datos.raiz.productos.get("P002")
producto3_bd = base_datos.raiz.productos.get("P003")

proveedor.agregar_producto(producto1_bd)
proveedor.agregar_producto(producto2_bd)
proveedor.agregar_producto(producto3_bd)

base_datos.raiz.proveedores[proveedor.id_proveedor] = proveedor
base_datos.guardar()

# Consulta de producto

producto_consultado = base_datos.raiz.productos.get("P001")

if producto_consultado:
    print("\nProducto consultado:")
    print(producto_consultado.nombre)
    print(producto_consultado.precio)
    print(producto_consultado.existencias)

# Modificar producto

servicio_productos.modificar_producto(
    "P001",
    nuevo_precio=38.0,
    nuevas_existencias=30
)

# Eliminar producto

servicio_productos.eliminar_producto("P003")

# Crear cliente

cliente = Cliente(
    "CLI001",
    "Rodrigo Farid",
    "2287654321",
    "rodrigo@example.com"
)

base_datos.raiz.clientes[cliente.id_cliente] = cliente
base_datos.guardar()

# Crear venta

cliente_bd = base_datos.raiz.clientes.get("CLI001")
producto1_bd = base_datos.raiz.productos.get("P001")
producto2_bd = base_datos.raiz.productos.get("P002")

venta = Venta(
    "V001",
    "2026-09-08",
    cliente_bd
)

# base_datos.raiz.ventas[venta.id_venta] = venta
# base_datos.guardar()
servicio_ventas.registrar_venta(venta)

# Agregar productos a la venta

servicio_ventas.agregar_producto_a_venta(
    "V001",
    producto1_bd,
    3
)

servicio_ventas.agregar_producto_a_venta(
    "V001",
    producto2_bd,
    2
)

# Calcular tota

total = servicio_ventas.calcular_total("V001")

print("\nTotal de la venta:")
print(total)

# Registrar la venta

# La venta ya existe en ZODB; ahora usamos
# el servicio para asociarla correctamente
# con el cliente.

venta_bd = base_datos.raiz.ventas.get("V001")

if venta_bd:
    cliente_bd.registrar_venta(venta_bd)
    base_datos.guardar()

# Recuperación de datos

base_datos.cerrar()

base_datos = BaseDatos()

servicio_productos = ServicioProductos(base_datos)
servicio_ventas = ServicioVentas(base_datos)
consultas = Consultas(base_datos)

cliente_recuperado = base_datos.raiz.clientes.get("CLI001")
venta_recuperada = base_datos.raiz.ventas.get("V001")

print("\nVentas del cliente:")

for venta_cliente in cliente_recuperado.consultar_ventas():
    print(
        venta_cliente.id_venta,
        venta_cliente.fecha,
        venta_cliente.total
    )

print("\nDetalle de la venta:")

for detalle in venta_recuperada.detalles:
    print(
        detalle.producto.nombre,
        detalle.cantidad,
        detalle.precio_unitario,
        detalle.subtotal
    )

# Inventario después de la venta


print("\nInventario después de la venta:")

producto1_recuperado = base_datos.raiz.productos.get("P001")
producto2_recuperado = base_datos.raiz.productos.get("P002")

print(
    producto1_recuperado.codigo,
    producto1_recuperado.nombre,
    producto1_recuperado.existencias
)

print(
    producto2_recuperado.codigo,
    producto2_recuperado.nombre,
    producto2_recuperado.existencias
)


# CONSULTAS

print("\n========================================")
print("CONSULTAS")
print("========================================")

# 1. Todos los productos

print("\n1. Todos los productos:")

for producto in consultas.todos_los_productos():
    print(
        producto.codigo,
        producto.nombre,
        producto.precio,
        producto.existencias
    )

# 2. Productos con precio superior a $35

print("\n2. Productos con precio superior a $35:")

for producto in consultas.productos_por_precio(35.0):
    print(
        producto.codigo,
        producto.nombre,
        producto.precio
    )

# 3. Productos bajo stock

print("\n3. Productos bajo stock:")

for producto in consultas.productos_bajo_stock(15):
    print(
        producto.codigo,
        producto.nombre,
        producto.existencias
    )

# 4. Productos de un proveedor

print("\n4. Productos del proveedor PROV001:")

for producto in consultas.productos_por_proveedor("PROV001"):
    print(
        producto.codigo,
        producto.nombre
    )

# 5. Total de ventas

print("\n5. Total de ventas:")

print(consultas.total_ventas())

# 6. Ventas del cliente

print("\n6. Ventas del cliente CLI001:")

for venta_cliente in consultas.ventas_cliente("CLI001"):
    print(
        venta_cliente.id_venta,
        venta_cliente.fecha,
        venta_cliente.total
    )

# 7. Productos más vendidos

print("\n7. Productos más vendidos:")

for producto in consultas.productos_mas_vendidos():
    print(
        producto["producto"].nombre,
        producto["cantidad"]
    )

# Cierre

base_datos.cerrar()