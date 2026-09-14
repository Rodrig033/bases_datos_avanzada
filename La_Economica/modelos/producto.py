from persistent import Persistent
from persistent.list import PersistentList


class Producto(Persistent):
    """Representa un producto disponible en la tienda."""

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
        """Incrementa la cantidad disponible del producto."""
        self.existencias += cantidad

    def disminuir_existencias(self, cantidad: int):
        """Disminuye las existencias si hay suficiente inventario."""
        if cantidad > self.existencias:
            return False

        self.existencias -= cantidad
        return True

    def esta_disponible(self) -> bool:
        """Indica si el producto tiene existencias disponibles."""
        return self.existencias > 0

    def actualizar_precio(self, nuevo_precio: float):
        """Actualiza el precio del producto."""
        self.precio = nuevo_precio


class Categoria(Persistent):
    """Representa una categoría de productos."""

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
        """Agrega un producto a la categoría."""
        self.productos.append(producto)

    def consultar_productos(self):
        """Devuelve los productos asociados a la categoría."""
        return self.productos


class Proveedor(Persistent):
    """Representa un proveedor de productos de la tienda."""

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
        """Asocia un producto con el proveedor."""
        self.productos.append(producto)

    def consultar_productos(self):
        """Devuelve los productos asociados al proveedor."""
        return self.productos