from Tienda.modelos import ( Autor, Libro, Estudiante, Prestamo ) 
from base_datos import ( abrir_base_datos, inicializar_base_datos, cerrar_base_datos )
import transaction
from datetime import datetime

def generar_reporte(root):

    total_libros = len(root.libros)

    libros_prestados = sum(
        1
        for libro in root.libros.values()
        if not libro.esta_disponible()
    )

    libros_disponibles = total_libros - libros_prestados

    total_estudiantes = len(root.estudiantes)

    total_autores = len(root.autores)

    total_prestamos = len(root.prestamos)

    prestamos_activos = sum(
        1
        for prestamo in root.prestamos.values()
        if prestamo.esta_activo()
    )

    prestamos_devueltos = total_prestamos - prestamos_activos

    print("\n========================================")
    print("         REPORTE DE BIBLIOTECA")
    print("========================================")

    print("\nLIBROS")
    print("----------------------------------------")
    print(f"Total de libros: {total_libros}")
    print(f"Disponibles: {libros_disponibles}")
    print(f"Prestados: {libros_prestados}")

    print("\nESTUDIANTES")
    print("----------------------------------------")
    print(f"Total de estudiantes: {total_estudiantes}")

    print("\nAUTORES")
    print("----------------------------------------")
    print(f"Total de autores: {total_autores}")

    print("\nPRÉSTAMOS")
    print("----------------------------------------")
    print(f"Total de préstamos: {total_prestamos}")
    print(f"Activos: {prestamos_activos}")
    print(f"Devueltos: {prestamos_devueltos}")

    print("\n========================================")


def main():
    
    db, connection, root = abrir_base_datos() 

    inicializar_base_datos(root) 

    print("===================================") 
    print(" SISTEMA DE BIBLIOTECA CON ZODB") 
    print("===================================")

    # ---------------------------------- # Crear autores # ---------------------------------- 
    
    autor1 = Autor( 1, "Gabriel García Márquez", "Colombia" ) 
    autor2 = Autor( 2, "Julio Verne", "Francia" ) 
    autor3 = Autor( 3, "Jorge Luis Borges", "Argentina" )
    autor4 = Autor( 4, "Julio Cortázar", "Argentina" )
    autor5 = Autor( 5, "Mario Vargas Llosa", "Perú" )
    autor6 = Autor( 6, "Isabel Allende", "Chile" )
    autor7 = Autor( 7, "Haruki Murakami", "Japón" )
    autor8 = Autor( 8, "George Orwell", "Reino Unido" )
    autor9 = Autor( 9, "Fyodor Dostoevsky", "Rusia" )
    autor10 = Autor( 10, "Ernest Hemingway", "Estados Unidos" )
    autor11 = Autor( 11, "Jane Austen", "Reino Unido" )
    autor12 = Autor( 12, "Frank Herbert", "Estados Unidos" )
    

    root.autores[autor1.id_autor] = autor1 
    root.autores[autor2.id_autor] = autor2 
    root.autores[autor3.id_autor] = autor3 
    root.autores[autor4.id_autor] = autor4 
    root.autores[autor5.id_autor] = autor5 
    root.autores[autor6.id_autor] = autor6 
    root.autores[autor7.id_autor] = autor7 
    root.autores[autor8.id_autor] = autor8 
    root.autores[autor9.id_autor] = autor9 
    root.autores[autor10.id_autor] = autor10 
    root.autores[autor11.id_autor] = autor11
    root.autores[autor12.id_autor] = autor12 


    # ---------------------------------- # Crear libros # ---------------------------------- 

    libro1 = Libro( "9780307474728", "Cien años de soledad", 1967, "Novela", autor1 ) 
    libro2 = Libro( "9780199538474", "Viaje al centro de la Tierra", 1864, "Aventura", autor2 ) 
    libro3 = Libro( "9788491050295", "Ficciones", 1944, "Cuento", autor3 )
    libro4 = Libro( "9788420664204", "Rayuela", 1963, "Novela", autor4 )
    libro5 = Libro( "9788420471833", "La ciudad y los perros", 1963, "Novela", autor5 )
    libro6 = Libro( "9788401337208", "La casa de los espíritus", 1982, "Novela", autor6 )
    libro7 = Libro( "9780099448781", "Tokio Blues", 1987, "Novela", autor7 )
    libro8 = Libro( "9780451524935", "1984", 1949, "Distopía", autor8 )
    libro9 = Libro( "9780140449136", "Crimen y castigo", 1866, "Novela", autor9 )
    libro10 = Libro( "9780684837389", "El viejo y el mar", 1952, "Novela", autor10 )
    libro11 = Libro( "9780141439518", "Orgullo y prejuicio", 1813, "Novela", autor11 )
    libro12 = Libro( "9780441172719", "Dune", 1965, "Ciencia ficción", autor12 )


    root.libros[libro1.isbn] = libro1 
    root.libros[libro2.isbn] = libro2 
    root.libros[libro3.isbn] = libro3 
    root.libros[libro4.isbn] = libro4 
    root.libros[libro5.isbn] = libro5 
    root.libros[libro6.isbn] = libro6 
    root.libros[libro7.isbn] = libro7 
    root.libros[libro8.isbn] = libro8 
    root.libros[libro9.isbn] = libro9 
    root.libros[libro10.isbn] = libro10 
    root.libros[libro11.isbn] = libro11
    root.libros[libro12.isbn] = libro12

    # ---------------------------------- # Crear estudiantes # ---------------------------------- 

    estudiante1 = Estudiante( "A001", "Ana López", "Ingeniería en Sistemas", "ana@universidad.edu.mx" ) 
    estudiante2 = Estudiante( "A002", "Carlos Pérez", "Ingeniería Informática", "carlos@universidad.edu.mx" ) 
    estudiante3 = Estudiante( "A003", "Rodrigo Farid", "Ingeniería en Inteligencia Artificial", "farid@universidad.edu.mx")
    estudiante4 = Estudiante( "A004", "Alan Turing", "Ingeniería en Inteligenica Artificial", "turing@universidad.edu.mx" ) 
    estudiante5 = Estudiante( "A005", "John McCarthy", "Ingeniería en Sistemas", "ana@universidad.edu.mx" ) 



    root.estudiantes[ estudiante1.matricula ] = estudiante1 
    root.estudiantes[ estudiante2.matricula ] = estudiante2 
    root.estudiantes[ estudiante3.matricula ] = estudiante3
    root.estudiantes[ estudiante4.matricula ] = estudiante4
    root.estudiantes[ estudiante5.matricula ] = estudiante5

    # ---------------------------------- # Crear préstamos # ---------------------------------- 

    prestamo1 = Prestamo("P001", libro12, estudiante1, datetime.now())
    prestamo2 = Prestamo("P002", libro3, estudiante2, datetime.now())
    prestamo3 = Prestamo("P003", libro1, estudiante3, datetime.now())
    prestamo4 = Prestamo("P004", libro5, estudiante4, datetime.now())
    prestamo5 = Prestamo("P005", libro6, estudiante5, datetime.now())

    # Registrar devolución del préstamo 2
    prestamo2.registrar_devolucion(datetime.now())

    root.prestamos[prestamo1.id_prestamo] = prestamo1
    root.prestamos[prestamo2.id_prestamo] = prestamo2
    root.prestamos[prestamo3.id_prestamo] = prestamo3
    root.prestamos[prestamo4.id_prestamo] = prestamo4
    root.prestamos[prestamo5.id_prestamo] = prestamo5

    
    transaction.commit() 

    print("\nAutores registrados:") 

    for autor in root.autores.values(): 
        print( autor.id_autor, autor.mostrar_info() ) 

    print("\nLibros registrados:") 

    for libro in root.libros.values(): 
        print( libro.isbn, libro.titulo, "- Disponible:", libro.esta_disponible() ) 

    print("\nEstudiantes registrados:") 

    for estudiante in root.estudiantes.values(): 
        print( estudiante.matricula, estudiante.mostrar_info() )    

    print("\nPrestamos registrados:") 

    for prestamo in root.prestamos.values(): 
            print( prestamo.mostrar_info())    


    # ============================================================
    # CONSULTAS
    # ============================================================

    # Consulta 1. Mostrar todos los libros
    print("\n===================================")
    print("CONSULTA 1: TODOS LOS LIBROS")
    print("===================================")

    for libro in root.libros.values():
        print(
            libro.isbn,
            "-",
            libro.titulo,
            "-",
            libro.anio,
            "-",
            libro.categoria
        )


    # Consulta 2. Buscar el libro: 9780307474728
    print("\n===================================")
    print("CONSULTA 2: BUSCAR LIBRO POR ISBN")
    print("===================================")

    isbn_busqueda = "9780307474728"

    if isbn_busqueda in root.libros:
        libro = root.libros[isbn_busqueda]

        print("ISBN:", libro.isbn)
        print("Título:", libro.titulo)
        print("Año:", libro.anio)
        print("Categoría:", libro.categoria)
        print("Disponible:", libro.esta_disponible())

    else:
        print("Libro no encontrado.")


    # Consulta 3. Buscar un ISBN inexistente
    print("\n===================================")
    print("CONSULTA 3: ISBN INEXISTENTE")
    print("===================================")

    isbn_busqueda = "9999999999999"

    if isbn_busqueda in root.libros:
        libro = root.libros[isbn_busqueda]
        print("Libro encontrado:", libro.titulo)

    else:
        print("No existe ningún libro con el ISBN:", isbn_busqueda)


    # Consulta 4. Mostrar únicamente los libros disponibles
    print("\n===================================")
    print("CONSULTA 4: LIBROS DISPONIBLES")
    print("===================================")

    for libro in root.libros.values():

        if libro.esta_disponible():
            print(
                libro.isbn,
                "-",
                libro.titulo
            )


    # Consulta 5. Mostrar libros publicados después de 1990
    print("\n===================================")
    print("CONSULTA 5: LIBROS DESPUÉS DE 1990")
    print("===================================")

    for libro in root.libros.values():

        if libro.anio > 1990:
            print(
                libro.isbn,
                "-",
                libro.titulo,
                "-",
                libro.anio
            )


    # Consulta 6. Mostrar todos los alumnos
    print("\n===================================")
    print("CONSULTA 6: TODOS LOS ALUMNOS")
    print("===================================")

    for estudiante in root.estudiantes.values():

        print(
            estudiante.matricula,
            "-",
            estudiante.nombre,
            "-",
            estudiante.carrera,
            "-",
            estudiante.correo
        )


    # Consulta 7. Mostrar préstamos activos
    print("\n===================================")
    print("CONSULTA 7: PRÉSTAMOS ACTIVOS")
    print("===================================")

    for prestamo in root.prestamos.values():

        if prestamo.esta_activo():
            prestamo.mostrar_info()


    # Consulta 8. Mostrar préstamos devueltos
    print("\n===================================")
    print("CONSULTA 8: PRÉSTAMOS DEVUELTOS")
    print("===================================")

    for prestamo in root.prestamos.values():

        if not prestamo.esta_activo():
            prestamo.mostrar_info()


    # Consulta 9. Mostrar todos los autores con nacionalidad
    print("\n===================================")
    print("CONSULTA 9: AUTORES Y NACIONALIDAD")
    print("===================================")

    for autor in root.autores.values():

        print(
            autor.nombre,
            "-",
            autor.nacionalidad
        )


    # Consulta 10. Mostrar libros publicados antes de 1990
    print("\n===================================")
    print("CONSULTA 10: LIBROS ANTES DE 1990")
    print("===================================")

    for libro in root.libros.values():

        if libro.anio < 1990:
            print(
                libro.isbn,
                "-",
                libro.titulo,
                "-",
                libro.anio
            )
    # Consulta 11.registro con nombre del alumno y el título del libro prestado
    print("\n===================================")
    print("CONSULTA 11: PRÉSTAMOS CON ALUMNO Y LIBRO")
    print("===================================")

    for prestamo in root.prestamos.values():

        print(
            "Préstamo:", prestamo.id_prestamo,
            "| Alumno:", prestamo.estudiante.nombre,
            "| Libro:", prestamo.libro.titulo
        )            
        
    # Consulta 12. Registro de todos los prestamos de un alumno: 
    print("\n===================================")
    print("CONSULTA 12: PRÉSTAMOS DE UN ALUMNO")
    print("===================================")

    matricula_busqueda = "A001"

    if matricula_busqueda in root.estudiantes:

        estudiante = root.estudiantes[matricula_busqueda]

        print("Alumno:", estudiante.nombre)
        print("Matrícula:", estudiante.matricula)

        for prestamo in root.prestamos.values():

            if prestamo.estudiante.matricula == matricula_busqueda:

                print(
                    "Préstamo:", prestamo.id_prestamo,
                    "| Libro:", prestamo.libro.titulo,
                    "| Estado:", prestamo.estado
                )

    else:
        print("Estudiante no encontrado.") 

    # Libros prestados actualmente:
    print("\n===================================")
    print("CONSULTA 13: LIBROS ACTUALMENTE PRESTADOS")
    print("===================================")

    for libro in root.libros.values():

        if not libro.esta_disponible():

            print(
                "ISBN:", libro.isbn,
                "| Título:", libro.titulo,
                "| Prestado a:",
                next(
                    (
                        prestamo.estudiante.nombre
                        for prestamo in root.prestamos.values()
                        if prestamo.libro.isbn == libro.isbn
                        and prestamo.esta_activo()
                    ),
                    "Desconocido"
                )
            )

        generar_reporte(root)
        cerrar_base_datos(db, connection)


if __name__ == "__main__":
    main()