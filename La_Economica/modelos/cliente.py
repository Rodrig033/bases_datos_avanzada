from persistent import Persistent
from persistent.list import PersistentList

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