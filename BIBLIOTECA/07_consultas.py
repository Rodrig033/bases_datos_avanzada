from ZODB import DB
from ZODB.FileStorage import FileStorage

import modelos


storage = FileStorage("biblioteca.fs")

# COMPLETAR
db = DB(storage)

# COMPLETAR
connection = db.open()

# COMPLETAR
root = connection.root()


# CONSULTA 1
# Mostrar todos los libros
libros = root["libros"].values()


print("\n--- LIBROS ---")

for libro in libros:
    print(f"{libro.titulo} - {libro.autor.nombre} {libro.anio}")



# CONSULTA 2
# Buscar un libro por título

titulo_buscar = "1984"
encontrado = None

for libro in libros:
    if libro.titulo == titulo_buscar:
        encontrado = libro
        break

if encontrado:
    print(f"Encontrado: {encontrado.titulo} - {encontrado.autor.nombre}"
          f" (ISBN {encontrado.isbn})")
else:
    print("Libro no encontrado.")
 

# COMPLETAR

# CONSULTA 3
# Mostrar únicamente libros disponibles


print("\n--- LIBROS DISPONIBLES ---")

# COMPLETAR

for libro in libros:
    if libro.disponible == True:
        print(f"{libro.titulo} - {libro.autor.nombre}")


# CONSULTA 4
# Buscar libros publicados después del año 2000


print("\n--- LIBROS DESPUÉS DEL AÑO 2000 ---")

# COMPLETAR

for libro in libros:
    if libro.anio > 2000:
        print(f"{libro.titulo} - {libro.anio}")


connection.close()
db.close()