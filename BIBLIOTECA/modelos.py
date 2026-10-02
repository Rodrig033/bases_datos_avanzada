from persistent import Persistent
from persistent.list import PersistentList

class Autor(Persistent):
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = PersistentList()

class Libro(Persistent):
    def __init__(self, titulo, isbn, autor, anio):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        self.anio = anio

        self.disponible = True
        autor.libros.append(self)

    def prestar(self):
        if not self.disponible:
            return False
        self.disponible = False
        return True  

    def devolver(self):
        self.disponible = True

class Usuario(Persistent):
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.prestamos = PersistentList()

class Prestamos(Persistent):
    def __init__(self, usuario, libro, fecha):
        self.usuario = usuario
        self.libro = libro
        self.fecha = fecha
        