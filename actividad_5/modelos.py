from persistent import Persistent
from datetime import datetime

class Autor(Persistent):

    def __init__(self,id_autor: str, nombre: str, nacionalidad: str):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrar_info(self) -> str:
        return f"Nombre: {self.nombre}, nacionalidad: {self.nacionalidad}"


class Libro(Persistent):

    def __init__(self, isbn: str, titulo:str, anio: int, categoria: str, autor: list[Autor]):
        self.isbn = isbn
        self.titulo = titulo
        self.anio = anio
        self.categoria = categoria
        self.autor = autor
        self.disponible = True

    def prestar(self) -> bool:
        if not self.disponible:
            return False

        self.disponible = False
        return True


    def devolver(self) -> bool:

        self.disponible = True

        return True


    def esta_disponible(self) -> bool:
        return self.disponible



class Estudiante(Persistent):

    def __init__(self, matricula: str, nombre: str, carrera: str, correo: str):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.correo = correo


    def mostrar_info(self) -> str:
        return f"Nombre: {self.nombre}, matricula: {self.matricula}, carrera: {self.carrera}"

class Prestamo(Persistent):

    def __init__(self, id_prestamo: str, libro: str, estudiante: str, fecha_prestamo: datetime):
        self.id_prestamo = id_prestamo
        self.libro = libro
        self.estudiante = estudiante
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = None
        self.estado = "Activo"

    def registrar_devolucion(self, fecha: datetime) -> str:
        self.fecha_devolucion = fecha
        self.estado = "Devuelto"

        return self.estado

    def esta_activo(self) -> bool:
        return self.estado == "Activo"

    def mostrar_info(self):
        print(f"ID del préstamo: {self.id_prestamo}")
        print(f"ISBN del libro: {self.libro}")
        print(f"Matrícula del estudiante: {self.estudiante}")
        print(f"Fecha de préstamo: {self.fecha_prestamo}")
        print(f"Fecha de devolución: {self.fecha_devolucion}")
        print(f"Estado: {self.estado}")
