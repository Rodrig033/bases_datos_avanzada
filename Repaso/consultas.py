from base_datos import abrir_base_datos
import modelos  # necesario para que ZODB reconstruya los objetos


def consulta_1(root):
    print("\n--- CONSULTA 1: TODOS LOS RECURSOS ---\n")
    for recurso in root["recursos"].values():
        recurso.mostrar_informacion()
        print()


def consulta_2(root):
    print("\n--- CONSULTA 2: BUSCAR POR ID ---\n")
    try:
        id_buscar = int(input("ID del recurso: "))
    except ValueError:
        print("El ID debe ser un número entero.")
        return
    recurso = root["recursos"].get(id_buscar)
    if recurso:
        recurso.mostrar_informacion()
    else:
        print(f"No existe un recurso con ID {id_buscar}.")


def consulta_3(root):
    print("\n--- CONSULTA 3: RECURSOS DISPONIBLES ---\n")
    for recurso in root["recursos"].values():
        if recurso.esta_disponible():
            recurso.mostrar_informacion()
            print()


def consulta_4(root):
    print("\n--- CONSULTA 4: RECURSOS POR TIPO ---\n")
    tipo = input("Tipo (GPU, Robot, Sensor, Servidor): ").strip().lower()
    encontrados = [r for r in root["recursos"].values() if r.tipo.lower() == tipo]
    if not encontrados:
        print(f"No hay recursos de tipo '{tipo}'.")
    for recurso in encontrados:
        recurso.mostrar_informacion()
        print()


def consulta_5(root, marca="NVIDIA"):
    print(f"\n--- CONSULTA 5: RECURSOS DE {marca} ---\n")
    for recurso in root["recursos"].values():
        if recurso.marca == marca:
            print(f"{recurso.nombre} ({recurso.modelo})")


def consulta_6(root):
    print("\n--- CONSULTA 6: PRÉSTAMOS ACTIVOS ---\n")
    for prestamo in root["prestamos"].values():
        if prestamo.esta_activo():
            print(f"Estudiante: {prestamo.estudiante.nombre}")
            print(f"Recurso:    {prestamo.recurso.nombre}")
            print(f"Fecha:      {prestamo.fecha}")
            print()


def consulta_7(root):
    print("\n--- CONSULTA 7: NAVEGACIÓN ENTRE OBJETOS ---\n")
    for prestamo in root["prestamos"].values():
        print(f"{prestamo.estudiante.nombre} → {prestamo.recurso.nombre}")


def consulta_8(root):
    print("\n--- CONSULTA 8: GPU CON COSTO > $20,000 ---\n")
    for recurso in root["recursos"].values():
        if recurso.tipo == "GPU" and recurso.costo > 20000:
            print(f"{recurso.nombre}: ${recurso.costo:,.2f}")


def consulta_9(root):
    print("\n--- CONSULTA 9: ESTADÍSTICAS ---\n")
    recursos = list(root["recursos"].values())
    total = len(recursos)
    disponibles = sum(1 for r in recursos if r.esta_disponible())
    print(f"Total de recursos:     {total}")
    print(f"Recursos disponibles:  {disponibles}")
    print(f"Recursos prestados:    {total - disponibles}")
    print(f"Valor total:           ${sum(r.costo for r in recursos):,.2f}")


def consulta_10(root, umbral=30000):
    """Estudiantes con equipo de alto valor en préstamo activo.

    Problema: el responsable del laboratorio necesita saber quién tiene
    en su poder equipo costoso (mayor al umbral) para darle seguimiento.
    Clases: Prestamo, Estudiante y Recurso.
    Relaciones: prestamo.estudiante y prestamo.recurso.
    Condición: préstamo activo y recurso con costo > umbral.
    """
    print(f"\n--- CONSULTA 10: EQUIPO DE ALTO VALOR (> ${umbral:,}) EN PRÉSTAMO ---\n")
    hubo = False
    for prestamo in root["prestamos"].values():
        if prestamo.esta_activo() and prestamo.recurso.costo > umbral:
            hubo = True
            print(f"{prestamo.estudiante.nombre} ({prestamo.estudiante.matricula}) "
                  f"tiene {prestamo.recurso.nombre} "
                  f"(${prestamo.recurso.costo:,.2f}) desde {prestamo.fecha}")
    if not hubo:
        print("No hay equipo de alto valor en préstamo.")


def main():
    db, connection, root = abrir_base_datos()
    try:
        for consulta in (consulta_1, consulta_2, consulta_3, consulta_4,
                         consulta_5, consulta_6, consulta_7, consulta_8,
                         consulta_9, consulta_10):
            consulta(root)
    finally:
        connection.close()
        db.close()


if __name__ == "__main__":
    main()