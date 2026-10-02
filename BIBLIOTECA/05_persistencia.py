from ZODB import DB
from ZODB.FileStorage import FileStorage
import transaction


class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio


# CONEXIÓN A LA BASE DE DATOS

storage = FileStorage("biblioteca.fs")


db = DB(storage)
connection = db.open()
root = connection.root()


# CREAR LIBRO

if "libro" in root:
    anterior = root["libro"]
    print("Libro recuperado de una ejecución anterior:", anterior.titulo)

libro = Libro(
    "La sombra del viento",
    "Carlos Ruiz Zafón",
    2001
)


# Guardar el libro dentro de root
root["libro"] = libro

# Confirmar la transacción
transaction.commit()


print("Libro almacenado correctamente.")


# CERRAR CONEXIONES

connection.close()
db.close()