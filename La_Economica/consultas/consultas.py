class Consultas:
    def __init__(self, base_datos):
        """Inicializa las consultas con una conexión a la base de datos."""
        self.base_datos = base_datos

    def todos_los_productos(self):
        """Devuelve todos los productos registrados."""
        return list(self.base_datos.raiz.productos.values())

    def productos_disponibles(self):
        """Devuelve los productos que tienen existencias disponibles."""
        productos_disponibles = []

        for producto in self.base_datos.raiz.productos.values():
            if producto.esta_disponible():
                productos_disponibles.append(producto)

        return productos_disponibles

    def productos_bajo_stock(self, limite):
        """Devuelve los productos cuyo stock está por debajo del límite."""
        productos_bajo_stock = []

        for producto in self.base_datos.raiz.productos.values():
            if producto.existencias < limite:
                productos_bajo_stock.append(producto)

        return productos_bajo_stock

    def productos_por_precio(self, precio):
        """Devuelve los productos cuyo precio supera el valor indicado."""
        productos_por_precio = []

        for producto in self.base_datos.raiz.productos.values():
            if producto.precio > precio:
                productos_por_precio.append(producto)

        return productos_por_precio

    def productos_por_proveedor(self, id_proveedor):
        """Devuelve los productos asociados a un proveedor."""
        proveedor = self.base_datos.raiz.proveedores.get(id_proveedor)

        if proveedor is None:
            return []

        return proveedor.consultar_productos()

    def ventas_cliente(self, id_cliente):
        """Deuelve las ventas registradas para un cliente."""
        cliente = self.base_datos.raiz.clientes.get(id_cliente)

        if cliente is None:
            return []

        return cliente.consultar_ventas()

    def productos_mas_vendidos(self):
        """Devuelve los productos ordenados por cantidad vendida."""
        cantidades_vendidas = {}

        for venta in self.base_datos.raiz.ventas.values():

            for detalle in venta.detalles:

                codigo = detalle.producto.codigo

                if codigo not in cantidades_vendidas:
                    cantidades_vendidas[codigo] = {
                        "producto": detalle.producto,
                        "cantidad": 0
                    }

                cantidades_vendidas[codigo]["cantidad"] += detalle.cantidad

        productos_ordenados = sorted(
            cantidades_vendidas.values(),
            key=lambda producto: producto["cantidad"],
            reverse=True
        )

        return productos_ordenados

    def total_ventas(self):
        """Calcula el total acumulado de todas las ventas."""
        total = 0.0

        for venta in self.base_datos.raiz.ventas.values():
            total += venta.total

        return total