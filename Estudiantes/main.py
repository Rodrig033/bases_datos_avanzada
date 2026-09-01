import transaction

from BTrees.OOBTree import OOBTree
from Estudiantes.database import open_database
from Estudiantes.models import Estudiante

def mostrar_estudiantes(root):
    print("\n--- ESTUDIANTES REGISTRADOS ---")

    if not root.estudiantes:
        print("No hay estudiantes registrados.")
        return

    for estudiante in root.estudiantes.values():
        print(estudiante)


def crear_estudiantes(root):
    root.estudiantes["A001"] = Estudiante(
        "A001",
        "Ana López",
        "Ingeniería en Inteligencia Artificial"
    )

    root.estudiantes["A002"] = Estudiante(
        "A002",
        "Carlos Hernández",
        "Ingeniería en Software"
    )

    root.estudiantes["A003"] = Estudiante(
        "A003",
        "Rodrigo Farid",
        "Ingeniería en Inteligencia artificial"
    )

    transaction.commit()

    print("\n Tres estudiantes fueron almacenados.")


def buscar_estudiante(root, matricula):
    return root.estudiantes.get(matricula)


def modificar_estudiante(root, matricula):
    estudiante = buscar_estudiante(root, matricula)

    if estudiante is None:
        print("\n Estudiante no encontrado.")
        return

    estudiante.carrera = "Ingeniería en Ciencia de Datos"

    transaction.commit()

    print("\n Estudiante modificado:")
    print(estudiante)


def eliminar_estudiante(root, matricula):
    estudiante = buscar_estudiante(root, matricula)

    if estudiante is None:
        print("\n Estudiante no encontrado.")
        return

    del root.estudiantes[matricula]

    transaction.commit()

    print("\n Estudiante eliminado.")


def main():
    db, connection, root = open_database()

    try:
        # Crear colección de estudiantes si todavía no existe
        if not hasattr(root, "estudiantes"):
            root.estudiantes = {}

            transaction.commit()

        # Crear objetos
        crear_estudiantes(root)

        # Consultar objetos
        mostrar_estudiantes(root)

        # Buscar objeto
        print("\n--- BÚSQUEDA ---")

        estudiante = buscar_estudiante(root, "A003")

        if estudiante:
            print("Estudiante encontrado:")
            print(estudiante)
        else:
            print("Estudiante no encontrado.")

        # Modificar objeto
        modificar_estudiante(root, "A001")

        # Mostrar después de modificar
        mostrar_estudiantes(root)

        # Eliminar objeto
        eliminar_estudiante(root, "A002")

        # Mostrar después de eliminar
        mostrar_estudiantes(root)

    finally:
        connection.close()
        db.close()


if __name__ == "__main__":
    main()