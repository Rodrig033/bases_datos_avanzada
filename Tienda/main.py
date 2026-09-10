from modelos import Producto, Categoria, Proveedor, Cliente, Venta
from base_datos import BaseDatos


if __name__ == "__main__":

    # CREACIÓN DE PRODUCTOS

    producto = Producto(
        "P001",
        "Arroz",
        "Arroz blanco de 1 kg",
        35.0,
        20,
        "Granos"
    )

    producto2 = Producto(
        "P002",
        "Frijol",
        "Frijol negro de 1 kg",
        42.0,
        15,
        "Granos"
    )

    producto3 = Producto(
        "P003",
        "Lentejas",
        "Lentejas de 1 kg",
        30.0,
        10,
        "Granos"
    )

    print(producto.nombre)
    print(producto.precio)
    print(producto.existencias)

    # MODIFICACIÓN DE EXISTENCIAS

    producto.incrementar_existencias(10)

    print(
        "Existencias después de incrementar:",
        producto.existencias
    )

    producto.disminuir_existencias(5)

    print(
        "Existencias después de disminuir:",
        producto.existencias
    )

    print(
        "¿Está disponible?",
        producto.esta_disponible()
    )

    # CATEGORÍA

    categoria = Categoria(
        "CAT001",
        "Granos",
        "Productos alimenticios como arroz, frijol y lentejas"
    )

    categoria.agregar_producto(producto)
    categoria.agregar_producto(producto2)
    categoria.agregar_producto(producto3)

    print("\nCategoría:", categoria.nombre)

    for producto_categoria in categoria.consultar_productos():
        print(
            "Producto:",
            producto_categoria.nombre
        )

    # PROVEEDOR

    # Abro la base de datos

    bd = BaseDatos()

    proveedor = Proveedor(
        "PROV001",
        "Distribuidora Central",
        "2281234567",
        "contacto@distribuidora.com",
        "Xalapa, Veracruz"
    )

    print("\nProveedor:", proveedor.nombre)

    for producto_proveedor in proveedor.consultar_productos():
        print(
            "Producto proporcionado:",
            producto_proveedor.nombre
        )

    # Cierro la base de datos
    bd.cerrar()

    # PERSISTENCIA DE PRODUCTOS EN ZODB

    bd = BaseDatos()

    bd.agregar_producto(producto)
    bd.agregar_producto(producto2)
    bd.agregar_producto(producto3)

    producto_bd = bd.consultar_producto("P001")
    producto2_bd = bd.consultar_producto("P002")
    producto3_bd = bd.consultar_producto("P003")

    proveedor.agregar_producto(producto_bd)
    proveedor.agregar_producto(producto2_bd)
    proveedor.agregar_producto(producto3_bd)

    bd.agregar_proveedor(proveedor)

    print(
        "\nProducto guardado en ZODB:",
        producto.nombre
    )

    # CONSULTA

    producto_consultado = bd.consultar_producto("P001")

    print("\n========== CONSULTA ==========")
    print("Código:", producto_consultado.codigo)
    print("Nombre:", producto_consultado.nombre)
    print("Precio:", producto_consultado.precio)
    print("Existencias:", producto_consultado.existencias)

    bd.cerrar()

    # MODIFICACIÓN

    bd = BaseDatos()

    resultado = bd.modificar_producto(
        "P001",
        nuevo_precio=38.0,
        nuevas_existencias=30
    )

    if resultado:
        print("\nProducto modificado correctamente.")

    producto_modificado = bd.consultar_producto("P001")

    print(
        "Nuevo precio:",
        producto_modificado.precio
    )

    print(
        "Nuevas existencias:",
        producto_modificado.existencias
    )

    bd.cerrar()

    # ELIMINACIÓN

    # P003 se utiliza únicamente para demostrar
    # la operación de eliminación.

    bd = BaseDatos()

    resultado = bd.eliminar_producto("P003")

    if resultado:
        print("\nProducto eliminado correctamente.")

    producto_eliminado = bd.consultar_producto("P003")

    print(
        "Consulta después de eliminar:",
        producto_eliminado
    )

    bd.cerrar()

    # CLIENTE

    cliente = Cliente(
        "CLI001",
        "Rodrigo Farid",
        "2289876543",
        "rodrigo@example.com"
    )

    print("\nCliente:", cliente.nombre)
    print("ID:", cliente.id_cliente)
    print("Correo:", cliente.correo)

    # PERSISTENCIA DEL CLIENTE

    bd = BaseDatos()

    bd.agregar_cliente(cliente)

    cliente_recuperado = bd.consultar_cliente("CLI001")

    print("\n========== CLIENTE PERSISTIDO ==========")
    print("ID:", cliente_recuperado.id_cliente)
    print("Nombre:", cliente_recuperado.nombre)
    print("Correo:", cliente_recuperado.correo)

    bd.cerrar()

    # VENTA

    bd = BaseDatos()

    producto_bd = bd.consultar_producto("P001")
    producto2_bd = bd.consultar_producto("P002")
    cliente_bd = bd.consultar_cliente("CLI001")

    venta = Venta(
        "V001",
        "2026-09-08",
        cliente_bd
    )

    resultado1 = venta.agregar_producto(
        producto_bd,
        3
    )

    resultado2 = venta.agregar_producto(
        producto2_bd,
        2
    )

    if resultado1 and resultado2:
        print("\nVenta registrada correctamente.")
    else:
        print("\nNo fue posible registrar todos los productos.")

    # Asociar la venta con el cliente
    cliente_bd.registrar_venta(venta)

    # Guardar la venta en ZODB
    bd.registrar_venta(venta)

    # Cerramos la conexión para comprobar la persistencia
    bd.cerrar()

    # Volvemos abrir la base de datos
    bd = BaseDatos()

    # Recuperar nuevamente al cliente
    cliente_recuperado = bd.consultar_cliente("CLI001")

    print("\n---------- VENTAS DEL CLIENTE RECUPERADAS ----------")

    for venta_cliente in cliente_recuperado.consultar_ventas():
        print("-", venta_cliente.id_venta, "| Total:", venta_cliente.total)

    # INFORMACIÓN DE LA VENTA

    print("\n========== VENTA ==========")

    print(
        "ID de venta:",
        venta.id_venta
    )

    print(
        "Cliente:",
        venta.cliente.nombre
    )

    print("\nProductos vendidos:")

    for detalle in venta.detalles:

        print(
            "-",
            detalle.producto.nombre,
            "| Cantidad:",
            detalle.cantidad,
            "| Precio unitario:",
            detalle.precio_unitario,
            "| Subtotal:",
            detalle.subtotal
        )

    print(
        "\nTotal de la venta:",
        venta.total
    )

    # VENTAS DEL CLIENTE

    print("\nVentas del cliente:")

    for venta_cliente in cliente_bd.consultar_ventas():

        print("-", venta_cliente.id_venta, "| Total:", venta_cliente.total)

    # INVENTARIO DESPUÉS DE LA VENTA

    print("\nInventario después de la venta:")

    print("Arroz:",producto_bd.existencias)
    print("Frijol:", producto2_bd.existencias)

    bd.cerrar()

    # RECUPERAR LA VENTA DESDE ZODB

    bd = BaseDatos()

    venta_recuperada = bd.consultar_venta("V001")

    print("\n========== VENTA RECUPERADA ==========")

    print("ID:", venta_recuperada.id_venta)
    print("Cliente:", venta_recuperada.cliente.nombre)
    print("Total:", venta_recuperada.total)

    bd.cerrar()

    # RECUPERAR INVENTARIO DESDE ZODB

    bd = BaseDatos()

    producto_recuperado = bd.consultar_producto("P001")
    producto2_recuperado = bd.consultar_producto("P002")

    print("\n========== INVENTARIO RECUPERADO ==========")

    print("Arroz:", producto_recuperado.existencias)

    print("Frijol:", producto2_recuperado.existencias)

    bd.cerrar()

    # CONSULTAS REQUERIDAS
    print("\n<<<<<<<<< CONSULTAS REQUERIDAS >>>>>>>>>>")

    bd = BaseDatos()

    # Todos los productos

    print("\n---------- TODOS LOS PRODUCTOS ----------")

    productos = bd.consultar_todos_productos()

    for producto in productos:
        print("-", producto.nombre, "| Código: ", producto.codigo, "| Precio: ", producto.precio, "| Existencias: ", producto.existencias)

    # Productos con precio mayor a un monto

    precio_consulta = 35.0

    print(f"\n---------- PRODUCTOS CON PRECIO MAYOR A {precio_consulta} ----------")
    productos_precio = bd.consultar_productos_por_precio(precio_consulta)

    for producto in productos_precio:
        print("-", producto.nombre, "| Precio: ", producto.precio)

    # Productos con un stock menor a un límite
    limite_stock = 15
    print(f"\n---------- PRODUCTOS CON STOCK MENOR A {limite_stock} ----------")

    productos_stock = bd.consultar_productos_por_stock(limite_stock)

    for producto in productos_stock:
        print("-", producto.nombre, "| Existencias: ", producto.existencias)

    # Consulta de productos por proveedor:

    productos_proveedor = bd.consultar_productos_por_proveedor("PROV001")

    print("\n---------- PRODUCTOS POR PROVEEDOR ----------")

    for producto in productos_proveedor:
        print("-", producto.nombre, "| Codigo: ", producto.codigo, "| Proveedor: ", proveedor.nombre)


    # Consulta total de ventas:

    total_ventas = bd.calcular_total_ventas()
    print("\n---------- CALCULAR TOTAL DE VENTAS ----------")
    print("Total de ventas: ", total_ventas)

    bd.cerrar()