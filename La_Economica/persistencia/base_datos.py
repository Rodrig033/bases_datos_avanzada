from ZODB import DB
from ZODB.FileStorage import FileStorage
from persistent.mapping import PersistentMapping
import transaction

class BaseDatos:
    """Administra la conexión y la persistencia de la base de datos."""
    def __init__(self, ruta="base_datos/tienda.fs"):
        """Inicializa la conexión con la base de datos."""

        self.storage = FileStorage(ruta)
        self.db = DB(self.storage)
        self.conexion = self.db.open()
        self.raiz = self.conexion.root()

        self._inicializar_colecciones()
        self.guardar()

    def _inicializar_colecciones(self):
        """Crea las colecciones persistentes necesarias si no existen."""

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

    def guardar(self):
        """Confirma los cambios realizados en la base de datos."""
        transaction.commit()

    def cerrar(self):
        """Cierra la conexión, la base de datos y el almacenamiento."""
        self.conexion.close()
        self.db.close()
        self.storage.close()