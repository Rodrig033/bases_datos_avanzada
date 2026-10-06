import transaction
from persistent.mapping import PersistentMapping

from base_datos import abrir_base_datos
from modelos import Recurso, Estudiante, Prestamo


def registrar(mapeo, clave, objeto, etiqueta):
    if clave in mapeo:
        print(f"Ya existe {etiqueta} {clave}.")
        return False
    mapeo[clave] = objeto
    print(f"{etiqueta.capitalize()} {clave} registrado correctamente.")
    return True


def registrar_prestamo(root, id_prestamo, matricula, id_recurso, fecha):
    estudiante = root["estudiantes"].get(matricula)
    recurso = root["recursos"].get(id_recurso)
    if estudiante is None or recurso is None:
        print("Estudiante o recurso inexistente.")
        return None
    if id_prestamo in root["prestamos"]:
        print(f"Ya existe el préstamo {id_prestamo}.")
        return None
    if not recurso.prestar():
        print(f"El recurso '{recurso.nombre}' no está disponible.")
        return None
    prestamo = Prestamo(id_prestamo, estudiante, recurso, fecha)
    root["prestamos"][id_prestamo] = prestamo
    print(f"Préstamo {id_prestamo} registrado correctamente.")
    return prestamo


db, connection, root = abrir_base_datos()
try:
    for clave in ("recursos", "estudiantes", "prestamos"):
        if clave not in root:
            root[clave] = PersistentMapping()

    recursos = [
        Recurso(1, "GPU RTX 4090", "GPU", 45000, "NVIDIA", "RTX 4090"),
        Recurso(2, "Jetson Orin", "Kit IA", 25000, "NVIDIA", "Orin"),
        Recurso(3, "Robot móvil", "Robot", 18000, "Tesla", "Optimus"),
        Recurso(4, "Sensor LiDAR", "Sensor", 32000, "STMicroelectronics", "VL53L0X"),
        Recurso(5, "Servidor IA", "Servidor", 85000, "Open AI", "Astra"),
        Recurso(6, "GPU RTX 3060", "GPU", 9000, "NVIDIA", "RTX 3060"),
    ]
    for r in recursos:
        registrar(root["recursos"], r.id_recurso, r, "recurso")

    estudiantes = [
        Estudiante("A001", "Ana López", "Ingeniería en IA"),
        Estudiante("A002", "Carlos Pérez", "Ingeniería en IA"),
        Estudiante("A003", "María Hernández", "Ingeniería en IA"),
    ]
    for e in estudiantes:
        registrar(root["estudiantes"], e.matricula, e, "estudiante")

    registrar_prestamo(root, 1, "A001", 1, "2026-10-01")
    registrar_prestamo(root, 2, "A002", 3, "2026-10-03")
    registrar_prestamo(root, 3, "A003", 5, "2026-10-04")

    p4 = registrar_prestamo(root, 4, "A003", 6, "2026-09-20")
    if p4:
        p4.devolver()          # préstamo ya devuelto

    transaction.commit()
finally:
    connection.close()
    db.close()