class Libro:

    def __init__ (self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):

        if self.disponible:
            self.disponible = False
            print(f"Libro {libro.titulo} prestado correctamente.")
        else:
            print(f"El libro {libro.titulo} no está disponible.")

    def devolver(self):

        if not self.disponible:
            self.disponible = True
            print(f"Libro {libro.titulo} se ha devuelto.")

        else:
            print(f"Libro {libro.titulo} ya se encotraba disponible.")


    def mostrar_estado(self):

        if self.disponible:
            print(f"Libro {libro.titulo} disponible.")
        else:
            print(f"Libro {libro.titulo} prestado.")

libro = Libro(
    "Don Quijote de la Mancha",
    "Miguel de Cervantes"
)


libro.mostrar_estado()

# Prestar el libro
libro.prestar()

# Mostrar nuevamente el estado
libro.mostrar_estado()

# Intentar prestar nuevamente el libro
libro.prestar()

# Devolver el libro
libro.devolver()