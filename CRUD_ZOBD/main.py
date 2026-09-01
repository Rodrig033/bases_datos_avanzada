import transaction

from BTrees.OOBTree import OOBTree

from Estudiantes.database import abrir_base_datos
from Estudiantes.models import Estudiante


def inicializar_base_datos(root):
    """Crea la colección de estudiantes si todavía no existe."""

    if not hasattr(root, "estudiantes"):
        root.estudiantes = OOBTree()
        transaction.commit()


def crear_estudiante(root):
    """CREATE: crea y almacena un nuevo estudiante."""

    matricula = input("Matrícula: ").strip()

    if matricula in root.estudiantes:
        print("Ya existe un estudiante con esa matrícula.")
        return

    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    carrera = input("Carrera: ").strip()

    try:
        semestre = int(input("Semestre: "))
    except ValueError:
        print("El semestre debe ser un número.")
        return

    estudiante = Estudiante(
        matricula,
        nombre,
        correo,
        carrera,
        semestre
    )

    root.estudiantes[matricula] = estudiante

    transaction.commit()

    print("\nEstudiante creado correctamente.")


def consultar_estudiantes(root):
    """READ: muestra todos los estudiantes."""

    print("\n--- ESTUDIANTES ---")

    if not root.estudiantes:
        print("No existen estudiantes registrados.")
        return

    for estudiante in root.estudiantes.values():
        print(estudiante.mostrar_informacion())


def buscar_estudiante(root):
    """READ: busca un estudiante mediante su matrícula."""

    matricula = input("Matrícula a buscar: ").strip()

    estudiante = root.estudiantes.get(matricula)

    if estudiante is None:
        print("\nEstudiante no encontrado.")
        return

    print("\nEstudiante encontrado:")
    print(estudiante.mostrar_informacion())


def modificar_estudiante(root):
    """UPDATE: modifica los datos de un estudiante."""

    matricula = input("Matrícula del estudiante: ").strip()

    estudiante = root.estudiantes.get(matricula)

    if estudiante is None:
        print("\nEstudiante no encontrado.")
        return

    print("\nEstudiante actual:")
    print(estudiante.mostrar_informacion())

    print("\n¿Qué deseas modificar?")
    print("1. Nombre")
    print("2. Correo")
    print("3. Carrera")
    print("4. Semestre")

    opcion = input("Opción: ").strip()

    if opcion == "1":
        estudiante.nombre = input("Nuevo nombre: ").strip()

    elif opcion == "2":
        estudiante.correo = input("Nuevo correo: ").strip()

    elif opcion == "3":
        nueva_carrera = input("Nueva carrera: ").strip()
        estudiante.cambiar_carrera(nueva_carrera)

    elif opcion == "4":
        try:
            estudiante.semestre = int(
                input("Nuevo semestre: ")
            )
        except ValueError:
            print("El semestre debe ser un número.")
            transaction.abort()
            return

    else:
        print("Opción inválida.")
        return

    transaction.commit()

    print("\nEstudiante modificado correctamente.")


def eliminar_estudiante(root):
    """DELETE: elimina un estudiante."""

    matricula = input("Matrícula del estudiante: ").strip()

    estudiante = root.estudiantes.get(matricula)

    if estudiante is None:
        print("\nEstudiante no encontrado.")
        return

    print("\nSe eliminará:")
    print(estudiante.mostrar_informacion())

    confirmacion = input(
        "¿Deseas eliminarlo? (s/n): "
    ).lower()

    if confirmacion == "s":
        del root.estudiantes[matricula]

        transaction.commit()

        print("\nEstudiante eliminado correctamente.")

    else:
        transaction.abort()

        print("\nOperación cancelada.")


def mostrar_menu():
    """Muestra el menú principal."""

    print("\n" + "=" * 45)
    print("      SISTEMA DE ESTUDIANTES - ZODB")
    print("=" * 45)
    print("1. Crear estudiante")
    print("2. Consultar estudiantes")
    print("3. Buscar estudiante")
    print("4. Modificar estudiante")
    print("5. Eliminar estudiante")
    print("6. Salir")
    print("=" * 45)


def main():

    db, connection, root = abrir_base_datos()

    try:

        inicializar_base_datos(root)

        while True:

            mostrar_menu()

            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                crear_estudiante(root)

            elif opcion == "2":
                consultar_estudiantes(root)

            elif opcion == "3":
                buscar_estudiante(root)

            elif opcion == "4":
                modificar_estudiante(root)

            elif opcion == "5":
                eliminar_estudiante(root)

            elif opcion == "6":
                print("\nPrograma finalizado.")
                break

            else:
                print("\nOpción inválida.")

    finally:

        connection.close()
        db.close()


if __name__ == "__main__":
    main()