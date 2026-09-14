class ServicioProductos:
    """Gestiona las operaciones relacionadas con productos."""
    def __init__(self, base_datos):
        """Inicializa el servicio con una conexión a la base de datos."""
        self.base_datos = base_datos

    def registrar_producto(self, producto):
        """Registra un producto en la base de datos."""
        self.base_datos.raiz.productos[producto.codigo] = producto
        self.base_datos.guardar()

    def modificar_producto(
        self,
        codigo,
        nuevo_precio=None,
        nuevas_existencias=None
    ):
        """Modifica el precio o las existencias de un producto."""

        producto = self.base_datos.raiz.productos.get(codigo)

        if producto is None:
            return False

        if nuevo_precio is not None:
            producto.actualizar_precio(nuevo_precio)

        if nuevas_existencias is not None:
            producto.existencias = nuevas_existencias

        self.base_datos.guardar()

        return True

    def eliminar_producto(self, codigo):
        """Elimina un producto de la base de datos."""
        if codigo not in self.base_datos.raiz.productos:
            return False

        del self.base_datos.raiz.productos[codigo]
        self.base_datos.guardar()

        return True

    def actualizar_inventario(self, codigo, cantidad):
        """Actualiza las existencias de un producto."""
        producto = self.base_datos.raiz.productos.get(codigo)

        if producto is None:
            return False

        if cantidad > 0:
            producto.incrementar_existencias(cantidad)

        elif cantidad < 0:
            cantidad_a_disminuir = abs(cantidad)

            if not producto.disminuir_existencias(cantidad_a_disminuir):
                return False

        else:
            return False

        self.base_datos.guardar()

        return True