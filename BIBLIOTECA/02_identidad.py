class Libro:
    def __init__ (self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

libro1 = Libro(
    "El principito",
    "Antoine de Saint-Exupéry"
)
 
libro2 = Libro(
    "El principito",
    "Antoine de Saint-Exupéry"
)
 
 
print("Libro 1:")
print(id(libro1))
 
print("\nLibro 2:")
print(id(libro2))

# Determinar si ambos objetos son el mismo
print("\nlibro1 == libro2:", libro1 == libro2)
print("libro1 is libros2", libro1 is libro2)
print("id(libro1) == id(libro2)", id(libro1) == id(libro2))


#  Modificar el título de libro1.
libro1.titulo = "El principito (edición ilustrada)"
 
 
# Mostrar las propiedades de libro1 y libro2.
print("\nLibro 1:")
print("  Título:", libro1.titulo)
print("  Autor:", libro1.autor)
 
print("Libro 2:")
print("  Título:", libro2.titulo)
print("  Autor:", libro2.autor)

libro3 = libro1
libro3.titulo = "Le Petite Prince"
print("libro3 is libros1", libro3 is libro1)
print("Título de libro1 tras modificar libro3:", libro1.titulo)

