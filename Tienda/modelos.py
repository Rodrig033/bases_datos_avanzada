from persistent import Persistent
from persistent.list import PersistentList


class Producto(Persistent):

    def __init__(
        self,
        codigo: str,
        nombre: str,
        descripcion: str,
        precio: float,
        existencias: int,
        categoria,
        fecha_caducidad=None,
        garantia_meses=0
    ):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.existencias = existencias
        self.categoria = categoria
        self.fecha_caducidad = fecha_caducidad
        self.garantia_meses = garantia_meses

    def incrementar_existencias(self, cantidad: int):
        self.existencias += cantidad

    def disminuir_existencias(self, cantidad: int):
        if cantidad > self.existencias:
            return False

        self.existencias -= cantidad
        return True

    def esta_disponible(self) -> bool:
        return self.existencias > 0

    def actualizar_precio(self, nuevo_precio: float):
        self.precio = nuevo_precio

class Categoria(Persistent):

    def __init__(
        self,
        id_categoria: str,
        nombre: str,
        descripcion: str
    ):
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.descripcion = descripcion
        self.productos = PersistentList()

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def consultar_productos(self):
        return self.productos

class Proveedor(Persistent):

    def __init__(
        self,
        id_proveedor: str,
        nombre: str,
        telefono: str,
        correo: str,
        direccion: str
    ):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.productos = PersistentList()

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def consultar_productos(self):
        return self.productos

class Cliente(Persistent):

    def __init__(
        self,
        id_cliente: str,
        nombre: str,
        telefono: str,
        correo: str
    ):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.ventas = PersistentList()

    def registrar_venta(self, venta):
        self.ventas.append(venta)

    def consultar_ventas(self):
        return self.ventas

class DetalleVenta(Persistent):

    def __init__(
        self,
        id_detalle: str,
        producto,
        cantidad: int
    ):
        self.id_detalle = id_detalle
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = producto.precio
        self.subtotal = 0.0

        self.calcular_subtotal()

    def calcular_subtotal(self):
        self.subtotal = self.cantidad * self.precio_unitario
        return self.subtotal

class Venta(Persistent):

    def __init__(
        self,
        id_venta: str,
        fecha,
        cliente
    ):
        self.id_venta = id_venta
        self.fecha = fecha
        self.cliente = cliente
        self.detalles = PersistentList()
        self.total = 0.0

    def agregar_producto(self, producto, cantidad):

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
        subtotal = 0.0

        for detalle in self.detalles:
            subtotal += detalle.subtotal

        return subtotal

    def calcular_total(self):
        self.total = self.calcular_subtotal()
        return self.total

    def consultar_productos(self):
        productos = []

        for detalle in self.detalles:
            productos.append(detalle.producto)

        return productos