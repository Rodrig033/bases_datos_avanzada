from base_datos import abrir_base_datos, cerrar_base_datos

def listar_libros(): 
    db, connection, root = abrir_base_datos() 
    print("\n--- LIBROS ---") 


    for libro in root.libros.values(): 
        print( f"ISBN: {libro.isbn}" ) 
        print( f"Título: {libro.titulo}" ) 
        print( f"Autor: {libro.autor.nombre}" ) 
        print( f"Año: {libro.anio}" ) 
        print( f"Categoría: {libro.categoria}" ) 
        print( f"Disponible: {libro.disponible}" ) 
        print("----------------------") 

    cerrar_base_datos(db, connection) 

def buscar_libro(isbn): 
    db, connection, root = abrir_base_datos() 
    libro = root.libros.get(isbn) 

    if libro: 
        print("\nLibro encontrado:") 
        print("Título:", libro.titulo) 
        print("Autor:", libro.autor.nombre) 
        print("Año:", libro.anio) 
        print("Categoría:", libro.categoria) 
        print("Disponible:", libro.disponible) 
    else: 
        print("Libro no encontrado.") 

    cerrar_base_datos(db, connection)