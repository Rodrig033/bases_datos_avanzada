import transaction
from BTrees.OOBTree import OOBTree

from database import abrir_base_datos
from models import (
    Autor,
    Libro,
    Estudiante,
    Prestamo
)


def inicializar(root):

    if not hasattr(root, "autores"):
        root.autores = OOBTree()

    if not hasattr(root, "libros"):
        root.libros = OOBTree()

    if not hasattr(root, "estudiantes"):
        root.estudiantes = OOBTree()

    if not hasattr(root, "prestamos"):
        root.prestamos = OOBTree()

    transaction.commit()


def registrar_autor(root):

    print("\n--- REGISTRAR AUTOR ---")

    id_autor = input("ID del autor: ").strip()

    if id_autor in root.autores:
        print("El autor ya existe.")
        return

    nombre = input("Nombre: ").strip()
    nacionalidad = input("Nacionalidad: ").strip()

    autor = Autor(
        id_autor,
        nombre,
        nacionalidad
    )

    root.autores[id_autor] = autor

    transaction.commit()

    print("Autor registrado correctamente.")


def registrar_libro(root):

    print("\n--- REGISTRAR LIBRO ---")

    isbn = input("ISBN: ").strip()

    if isbn in root.libros:
        print("El libro ya existe.")
        return

    titulo = input("Título: ").strip()

    try:
        anio = int(
            input("Año de publicación: ")
        )

        ejemplares = int(
            input("Número de ejemplares: ")
        )

    except ValueError:
        print("Los valores deben ser numéricos.")
        return

    categoria = input("Categoría: ").strip()

    libro = Libro(
        isbn,
        titulo,
        anio,
        categoria,
        ejemplares
    )

    root.libros[isbn] = libro

    transaction.commit()

    print("Libro registrado correctamente.")


def agregar_autor_a_libro(root):

    isbn = input("ISBN del libro: ").strip()

    libro = root.libros.get(isbn)

    if libro is None:
        print("Libro no encontrado.")
        return

    id_autor = input("ID del autor: ").strip()

    autor = root.autores.get(id_autor)

    if autor is None:
        print("Autor no encontrado.")
        return

    libro.agregar_autor(autor)

    transaction.commit()

    print("Autor agregado al libro.")


def registrar_estudiante(root):

    print("\n--- REGISTRAR ESTUDIANTE ---")

    matricula = input("Matrícula: ").strip()

    if matricula in root.estudiantes:
        print("El estudiante ya existe.")
        return

    nombre = input("Nombre: ").strip()
    carrera = input("Carrera: ").strip()
    correo = input("Correo electrónico: ").strip()

    estudiante = Estudiante(
        matricula,
        nombre,
        carrera,
        correo
    )

    root.estudiantes[matricula] = estudiante

    transaction.commit()

    print("Estudiante registrado correctamente.")


def consultar_libros(root):

    print("\n--- LIBROS ---")

    if not root.libros:
        print("No hay libros registrados.")
        return

    for libro in root.libros.values():

        print("-" * 50)
        print(libro.mostrar_informacion())


def buscar_libro(root):

    isbn = input("ISBN: ").strip()

    libro = root.libros.get(isbn)

    if libro is None:
        print("Libro no encontrado.")
        return

    print("\n--- LIBRO ENCONTRADO ---")
    print(libro.mostrar_informacion())


def consultar_disponibilidad(root):

    isbn = input("ISBN: ").strip()

    libro = root.libros.get(isbn)

    if libro is None:
        print("Libro no encontrado.")
        return

    if libro.esta_disponible():

        print(
            f"Disponible. "
            f"Ejemplares disponibles: "
            f"{libro.ejemplares_disponibles}"
        )

    else:
        print("El libro no tiene ejemplares disponibles.")


def registrar_prestamo(root):

    print("\n--- REGISTRAR PRÉSTAMO ---")

    matricula = input(
        "Matrícula del estudiante: "
    ).strip()

    estudiante = root.estudiantes.get(
        matricula
    )

    if estudiante is None:
        print("Estudiante no encontrado.")
        return

    isbn = input("ISBN del libro: ").strip()

    libro = root.libros.get(isbn)

    if libro is None:
        print("Libro no encontrado.")
        return

    if not libro.esta_disponible():

        print(
            "No se puede realizar el préstamo."
        )

        print(
            "No existen ejemplares disponibles."
        )

        return

    id_prestamo = input(
        "ID del préstamo: "
    ).strip()

    if id_prestamo in root.prestamos:

        print("El préstamo ya existe.")
        return

    fecha_prestamo = input(
        "Fecha de préstamo (YYYY-MM-DD): "
    ).strip()

    fecha_limite = input(
        "Fecha límite (YYYY-MM-DD): "
    ).strip()

    prestamo = Prestamo(
        id_prestamo,
        estudiante,
        libro,
        fecha_prestamo,
        fecha_limite
    )

    libro.prestar_ejemplar()

    root.prestamos[id_prestamo] = prestamo

    transaction.commit()

    print("Préstamo registrado correctamente.")


def registrar_devolucion(root):

    print("\n--- REGISTRAR DEVOLUCIÓN ---")

    id_prestamo = input(
        "ID del préstamo: "
    ).strip()

    prestamo = root.prestamos.get(
        id_prestamo
    )

    if prestamo is None:
        print("Préstamo no encontrado.")
        return

    if not prestamo.esta_activo():

        print("El préstamo ya fue devuelto.")
        return

    fecha = input(
        "Fecha de devolución (YYYY-MM-DD): "
    ).strip()

    prestamo.registrar_devolucion(fecha)

    prestamo.libro.devolver_ejemplar()

    transaction.commit()

    print("Devolución registrada correctamente.")


def consultar_prestamos_estudiante(root):

    matricula = input(
        "Matrícula del estudiante: "
    ).strip()

    estudiante = root.estudiantes.get(
        matricula
    )

    if estudiante is None:
        print("Estudiante no encontrado.")
        return

    print(
        f"\n--- PRÉSTAMOS DE "
        f"{estudiante.nombre} ---"
    )

    encontrados = False

    for prestamo in root.prestamos.values():

        if (
            prestamo.estudiante.matricula
            == matricula
        ):

            encontrados = True

            print("-" * 50)
            print(
                prestamo.mostrar_informacion()
            )

    if not encontrados:
        print("No tiene préstamos registrados.")


def mostrar_menu():

    print("\n")
    print("=" * 50)
    print("       BIBLIOTECA UNIVERSITARIA - ZODB")
    print("=" * 50)

    print("1. Registrar autor")
    print("2. Registrar libro")
    print("3. Agregar autor a libro")
    print("4. Registrar estudiante")
    print("5. Consultar libros")
    print("6. Buscar libro por ISBN")
    print("7. Consultar disponibilidad")
    print("8. Registrar préstamo")
    print("9. Registrar devolución")
    print("10. Consultar préstamos de estudiante")
    print("11. Salir")

    print("=" * 50)


def main():

    db, connection, root = abrir_base_datos()

    try:

        inicializar(root)

        while True:

            mostrar_menu()

            opcion = input(
                "Seleccione una opción: "
            ).strip()

            if opcion == "1":
                registrar_autor(root)

            elif opcion == "2":
                registrar_libro(root)

            elif opcion == "3":
                agregar_autor_a_libro(root)

            elif opcion == "4":
                registrar_estudiante(root)

            elif opcion == "5":
                consultar_libros(root)

            elif opcion == "6":
                buscar_libro(root)

            elif opcion == "7":
                consultar_disponibilidad(root)

            elif opcion == "8":
                registrar_prestamo(root)

            elif opcion == "9":
                registrar_devolucion(root)

            elif opcion == "10":
                consultar_prestamos_estudiante(root)

            elif opcion == "11":
                print(
                    "\nPrograma finalizado."
                )
                break

            else:
                print("Opción inválida.")

    finally:

        connection.close()
        db.close()


if __name__ == "__main__":
    main()