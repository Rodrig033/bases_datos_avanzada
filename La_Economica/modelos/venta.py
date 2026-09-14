from persistent import Persistent
from persistent.list import PersistentList

class DetalleVenta(Persistent):
    """Representa un producto específico dentro de una venta."""
    def __init__(self, id_detalle: str, producto, cantidad: int):
        self.id_detalle = id_detalle
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = producto.precio
        self.subtotal = 0.0

        self.calcular_subtotal()

    def calcular_subtotal(self):
        """Calcula el subtotal del producto según su cantidad y precio."""
        self.subtotal = self.cantidad * self.precio_unitario
        return self.subtotal


class Venta(Persistent):
    def __init__(self, id_venta: str, fecha, cliente):
        self.id_venta = id_venta
        self.fecha = fecha
        self.cliente = cliente
        self.detalles = PersistentList()
        self.total = 0.0

    def agregar_producto(self, producto, cantidad):
        """Agrega un producto a la venta y actualiza el inventario."""

        if cantidad <= 0:
            return False

        if not producto.disminuir_existencias(cantidad):
            return False

        id_detalle = f"{self.id_venta}-D{len(self.detalles) + 1}"

        detalle = DetalleVenta(
            id_detalle,
            producto,
            cantidad
        )

        self.detalles.append(detalle)
        self.calcular_total()

        return True

    def calcular_subtotal(self):
        """Calcula la suma de los subtotales de los productos vendidos."""

        subtotal = 0.0

        for detalle in self.detalles:
            subtotal += detalle.subtotal

        return subtotal

    def calcular_total(self):
        """Calcula y actualiza el total de la venta."""

        self.total = self.calcular_subtotal()
        return self.total

    def consultar_productos(self):
        """Devuelve los productos incluidos en la venta."""

        productos = []

        for detalle in self.detalles:
            productos.append(detalle.producto)

        return productos