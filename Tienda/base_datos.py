from ZODB.FileStorage import FileStorage
from ZODB import DB
from persistent.mapping import PersistentMapping
import transaction


class BaseDatos:

    def __init__(self, ruta="base_datos/tienda.fs"):
        self.storage = FileStorage(ruta)
        self.db = DB(self.storage)
        self.conexion = self.db.open()
        self.raiz = self.conexion.root()

        if not hasattr(self.raiz, "productos"):
            self.raiz.productos = PersistentMapping()

        if not hasattr(self.raiz, "categorias"):
            self.raiz.categorias = PersistentMapping()

        if not hasattr(self.raiz, "proveedores"):
            self.raiz.proveedores = PersistentMapping()

        if not hasattr(self.raiz, "clientes"):
            self.raiz.clientes = PersistentMapping()

        if not hasattr(self.raiz, "ventas"):
            self.raiz.ventas = PersistentMapping()

        self.guardar()

    def guardar(self):
        transaction.commit()

    def cerrar(self):
        self.conexion.close()
        self.db.close()
        self.storage.close()

    # CRUD DE PRODUCTOS

    def agregar_producto(self, producto):
        self.raiz.productos[producto.codigo] = producto
        self.guardar()

    def consultar_producto(self, codigo):
        return self.raiz.productos.get(codigo)

    def modificar_producto(
        self,
        codigo,
        nuevo_precio=None,
        nuevas_existencias=None
    ):
        producto = self.consultar_producto(codigo)

        if producto is None:
            return False

        if nuevo_precio is not None:
            producto.actualizar_precio(nuevo_precio)

        if nuevas_existencias is not None:
            producto.existencias = nuevas_existencias

        self.guardar()
        return True

    def eliminar_producto(self, codigo):
        if codigo not in self.raiz.productos:
            return False

        del self.raiz.productos[codigo]
        self.guardar()
        return True

    # CRUD de clientes

    def agregar_cliente(self, cliente):
        self.raiz.clientes[cliente.id_cliente] = cliente
        self.guardar()

    def consultar_cliente(self, id_cliente):
        return self.raiz.clientes.get(id_cliente)

    def eliminar_cliente(self, id_cliente):
        if id_cliente not in self.raiz.clientes:
            return False

        del self.raiz.clientes[id_cliente]
        self.guardar()
        return True

    # CRUD de proveedores
    def agregar_proveedor(self, proveedor):
        self.raiz.proveedores[proveedor.id_proveedor] = proveedor
        self.guardar()

    def consultar_proveedor(self, id_proveedor):
        return self.raiz.proveedores.get(id_proveedor)

    def consultar_proveedores(self):
        return list(self.raiz.proveedores.values())


    # VENTAS

    def registrar_venta(self, venta):
        self.raiz.ventas[venta.id_venta] = venta
        self.guardar()

    def consultar_venta(self, id_venta):
        return self.raiz.ventas.get(id_venta)

    def consultar_ventas(self):
        return list(self.raiz.ventas.values())


    # Consultas requeridas 

    def consultar_todos_productos(self):
        return list(self.raiz.productos.values())

    def consultar_productos_por_precio(self, precio):
        productos = []

        for producto in self.raiz.productos.values():
            if producto.precio > precio:
                productos.append(producto)

        return productos        

    def consultar_productos_por_stock(self, limite):
        productos = []

        for producto in self.raiz.productos.values():
            if producto.existencias < limite:
                productos.append(producto)

        return productos

    def calcular_total_ventas(self):
        total = 0.0

        for venta in self.raiz.ventas.values():
            total += venta.total

        return total

    def consultar_productos_por_proveedor(self, id_proveedor):
        proveedor = self.consultar_proveedor(id_proveedor)

        if proveedor is None:
            return []

        return proveedor.consultar_productos()

    