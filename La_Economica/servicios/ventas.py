class ServicioVentas:
    def __init__(self, base_datos):
        """Inicializa el servicio con una conexión a la base de datos."""

        self.base_datos = base_datos

    def registrar_venta(self, venta):
        """Registra una venta en la base de datos."""
        self.base_datos.raiz.ventas[venta.id_venta] = venta

        if venta.cliente is not None:
            venta.cliente.registrar_venta(venta)

        self.base_datos.guardar()

    def agregar_producto_a_venta(self, id_venta, producto, cantidad):
        """Agrega un producto a una venta existente."""
        venta = self.base_datos.raiz.ventas.get(id_venta)

        if venta is None:
            return False

        resultado = venta.agregar_producto(producto, cantidad)

        if not resultado:
            return False

        self.base_datos.guardar()

        return True

    def calcular_total(self, id_venta):
        """Calcula el total de una venta existente."""
        venta = self.base_datos.raiz.ventas.get(id_venta)

        if venta is None:
            return None

        total = venta.calcular_total()

        self.base_datos.guardar()

        return total