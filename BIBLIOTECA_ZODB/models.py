from persistent import Persistent
from persistent.list import PersistentList


class Autor(Persistent):

    def __init__(self, id_autor, nombre, nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrar_informacion(self):
        return (
            f"{self.nombre} "
            f"({self.nacionalidad})"
        )


class Libro(Persistent):

    def __init__(
        self,
        isbn,
        titulo,
        anio_publicacion,
        categoria,
        numero_ejemplares
    ):
        self.isbn = isbn
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.categoria = categoria

        self.numero_ejemplares = numero_ejemplares
        self.ejemplares_disponibles = numero_ejemplares

        self.autores = PersistentList()

    def agregar_autor(self, autor):
        if autor not in self.autores:
            self.autores.append(autor)

    def esta_disponible(self):
        return self.ejemplares_disponibles > 0

    def prestar_ejemplar(self):

        if not self.esta_disponible():
            raise ValueError(
                "No hay ejemplares disponibles."
            )

        self.ejemplares_disponibles -= 1

    def devolver_ejemplar(self):

        if (
            self.ejemplares_disponibles
            < self.numero_ejemplares
        ):
            self.ejemplares_disponibles += 1

    def mostrar_informacion(self):

        autores = ", ".join(
            autor.nombre
            for autor in self.autores
        )

        return (
            f"ISBN: {self.isbn}\n"
            f"Título: {self.titulo}\n"
            f"Año: {self.anio_publicacion}\n"
            f"Categoría: {self.categoria}\n"
            f"Ejemplares: {self.numero_ejemplares}\n"
            f"Disponibles: {self.ejemplares_disponibles}\n"
            f"Autores: {autores}"
        )


class Estudiante(Persistent):

    def __init__(
        self,
        matricula,
        nombre,
        carrera,
        correo
    ):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.correo = correo

    def mostrar_informacion(self):

        return (
            f"Matrícula: {self.matricula}\n"
            f"Nombre: {self.nombre}\n"
            f"Carrera: {self.carrera}\n"
            f"Correo: {self.correo}"
        )


class Prestamo(Persistent):

    def __init__(
        self,
        id_prestamo,
        estudiante,
        libro,
        fecha_prestamo,
        fecha_limite
    ):
        self.id_prestamo = id_prestamo

        self.estudiante = estudiante
        self.libro = libro

        self.fecha_prestamo = fecha_prestamo
        self.fecha_limite = fecha_limite

        self.fecha_devolucion = None

        self.estado = "ACTIVO"

    def registrar_devolucion(self, fecha):

        if self.estado == "DEVUELTO":
            raise ValueError(
                "El préstamo ya fue devuelto."
            )

        self.fecha_devolucion = fecha
        self.estado = "DEVUELTO"

    def esta_activo(self):

        return self.estado == "ACTIVO"

    def mostrar_informacion(self):

        return (
            f"Préstamo: {self.id_prestamo}\n"
            f"Estudiante: {self.estudiante.nombre}\n"
            f"Libro: {self.libro.titulo}\n"
            f"Fecha préstamo: {self.fecha_prestamo}\n"
            f"Fecha límite: {self.fecha_limite}\n"
            f"Fecha devolución: {self.fecha_devolucion}\n"
            f"Estado: {self.estado}"
        )