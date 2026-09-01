from persistent import Persistent


class Persona(Persistent):
    """Clase base para representar una persona."""

    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre} | Correo: {self.correo}"


class Estudiante(Persona):
    """Representa un estudiante y hereda de Persona."""

    def __init__(self, matricula, nombre, correo, carrera, semestre):
        super().__init__(nombre, correo)

        self.matricula = matricula
        self.carrera = carrera
        self.semestre = semestre

    def cambiar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera

    def avanzar_semestre(self):
        self.semestre += 1

    def mostrar_informacion(self):
        return (
            f"Matrícula: {self.matricula} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo} | "
            f"Carrera: {self.carrera} | "
            f"Semestre: {self.semestre}"
        )