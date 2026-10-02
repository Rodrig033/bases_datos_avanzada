class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Auto: {self.autor}")        
        print(f"Año: {self.anio}")


libro1 = Libro(
    "Cien años de soledad",
    "Gabriel García Márquez",
    1967
)
 
libro2 = Libro(
    "El principito",
    "Antoine de Saint-Exupéry",
    1943
)
 
# Tercer libro
libro3 = Libro(
    "1984",
    "George Orwell",
    1949
)

# Mostrar información
print("-- LIBROS --")
print()
for libro in [libro1, libro2, libro3]:
    libro.mostrar_informacion()
    print()