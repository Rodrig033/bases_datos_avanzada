from persistent import Persistent


class Recurso(Persistent):
    def __init__(self, id_recurso, nombre, tipo, costo, marca, modelo, disponible=True):
        self.id_recurso = id_recurso
        self.nombre = nombre
        self.tipo = tipo
        self.costo = costo
        self.marca = marca
        self.modelo = modelo
        self.disponible = disponible

    def mostrar_informacion(self):
        print(f"ID: {self.id_recurso}")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Costo: ${self.costo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Disponible: {self.disponible}")

    def prestar(self):
        if not self.disponible:
            return False
        self.disponible = False
        return True

    def devolver(self):
        self.disponible = True

    def esta_disponible(self):
        return self.disponible


class Estudiante(Persistent):
    def __init__(self, matricula, nombre, carrera):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera

    def mostrar_informacion(self):
        print(f"Matrícula: {self.matricula}")
        print(f"Nombre: {self.nombre}")
        print(f"Carrera: {self.carrera}")


class Prestamo(Persistent):
    def __init__(self, id_prestamo, estudiante, recurso, fecha):
        self.id_prestamo = id_prestamo
        self.estudiante = estudiante
        self.recurso = recurso
        self.fecha = fecha
        self.activo = True

    def devolver(self):
        self.activo = False
        self.recurso.devolver()

    def esta_activo(self):
        return self.activo