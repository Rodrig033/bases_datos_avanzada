from datetime import date
from ZODB import DB
from ZODB.FileStorage import FileStorage
from persistent.mapping import PersistentMapping
from persistent.list import PersistentList
import transaction
from modelos import Autor, Libro, Usuario, Prestamos


def registrar_prestamo(root, usuario, libro, fecha):
    """Crea el préstamo y establece las relaciones entre los objetos."""
    if not libro.prestar():
        print(f"No se pudo prestar '{libro.titulo}': no está disponible.")
        return None
    prestamo = Prestamos(usuario, libro, fecha)
    usuario.prestamos.append(prestamo)
    root["prestamos"].append(prestamo)
    return prestamo

# Conexión de la base datos
storage = FileStorage("biblioteca.fs")
db = DB(storage)
connection = db.open()
root = connection.root()

# Se reinicia el contenido para poder ejecutar el programa varias veces
root.clear()
root["autores"] = PersistentMapping()
root["libros"] = PersistentMapping()
root["usuarios"] = PersistentMapping()
root["prestamos"] = PersistentList()


# 3 AUTORES
orwell = Autor("George Orwell")
garcia_marquez = Autor("Gabriel García Márquez")
ruiz_zafon = Autor("Carlos Ruiz Zafón")

for autor in (orwell, garcia_marquez, ruiz_zafon):
    root["autores"][autor.nombre] = autor


# 5 LIBROS (cada uno asociado a un autor)
libros = [
    Libro("1984", "9780451524935", orwell, 1949),
    Libro("Rebelión en la granja", "9780451526342", orwell, 1945),
    Libro("Cien años de soledad", "9780060883287", garcia_marquez, 1967),
    Libro("La sombra del viento", "9788408172178", ruiz_zafon, 2001),
    Libro("El juego del ángel", "9788408079989", ruiz_zafon, 2008),
]

for libro in libros:
    root["libros"][libro.isbn] = libro


# 3 USUARIOS
noam = Usuario("Noam Chomsky", "A001")
rodrigo = Usuario("Rodrigo Farid", "A002")
fiodor = Usuario("Dostoyevky", "A003")

for usuario in (noam, rodrigo, fiodor):
    root["usuarios"][usuario.matricula] = usuario


# PRÉSTAMOS
registrar_prestamo(root, noam, libros[0], date(2026, 9, 1))     # 1984
registrar_prestamo(root, noam, libros[3], date(2026, 9, 5))     # La sombra del viento
registrar_prestamo(root, rodrigo, libros[2], date(2026, 9, 10))   # Cien años de soledad
registrar_prestamo(root, fiodor, libros[0], date(2026, 9, 12))  # 1984 (ya prestado: se rechaza)


transaction.commit()


# VERIFICACIÓN DE RELACIONES
print("\n--- PRÉSTAMOS POR USUARIO ---")
for usuario in root["usuarios"].values():
    titulos = [p.libro.titulo for p in usuario.prestamos]
    print(f"{usuario.nombre}: {titulos}")

print("\n--- LIBROS POR AUTOR ---")
for autor in root["autores"].values():
    print(f"{autor.nombre}: {[l.titulo for l in autor.libros]}")

print("\nBase de datos creada correctamente.")

connection.close()
db.close()