import persistent

# Al heredar persistens estamos diciendo que el objeto puede ser persistente
class Estudiante(persistent.Persistent):
    def __init__(self, matricula, nombre, carrera):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera

    def __repr__(self):
        return (
            f"Estudiante("
            f"matricula='{self.matricula}', "
            f"nombre='{self.nombre}', "
            f"carrera='{self.carrera}')"
        )