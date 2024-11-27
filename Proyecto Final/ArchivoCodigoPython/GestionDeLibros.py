import mysql.connector

def conectar_db(): #Conectamos la base de datos
    return mysql.connector.connect(
        host="localhost",
        user="tu_usuario",
        password="tu_contraseña",
        database="tu_base_de_datos"
    )

def registrar_libro(): #Función para poder registrar un libro nuevo
    conexion = conectar_db()
    cursor = conexion.cursor()

    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")
    editorial = input("Ingrese la editorial: ")
    anio_publicacion = input("Ingrese el año de publicación (YYYY): ")

    try:
        cursor.execute(
            "INSERT INTO Libros (titulo, autor, genero, editorial, anio_publicacion) VALUES (%s, %s, %s, %s, %s)",
            (titulo, autor, genero, editorial, anio_publicacion)
        )
        conexion.commit()
        print("Libro registrado correctamente.")
    except Exception as e:
        print(f"Error al registrar el libro: {e}")
    finally:
        cursor.close()
        conexion.close()

def ver_libros(): #Función para ver los detalles de un libro
    conexion = conectar_db()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM Libros")
        libros = cursor.fetchall()

        if libros:
            print("Lista de libros:")
            for libro in libros:
                print(f"ID: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}, Género: {libro[3]}, Editorial: {libro[4]}, Año: {libro[5]}")
        else:
            print("No hay libros registrados.")
    except Exception as e:
        print(f"Error al consultar los libros: {e}")
    finally:
        cursor.close()
        conexion.close()

def actualizar_libro(): #Función para actualizar la información de los libros
    conexion = conectar_db()
    cursor = conexion.cursor()

    libro_id = input("Ingrese el ID del libro que desea actualizar: ")
    print("¿Qué desea actualizar?")
    print("1) Título\n2) Autor\n3) Género\n4) Editorial\n5) Año de publicación")
    opcion = int(input("Seleccione una opción (1-5): "))

    campos = ["titulo", "autor", "genero", "editorial", "anio_publicacion"]
    if 1 <= opcion <= 5:
        nuevo_valor = input(f"Ingrese el nuevo valor para {campos[opcion - 1]}: ")

        try:
            query = f"UPDATE Libros SET {campos[opcion - 1]} = %s WHERE libro_id = %s"
            cursor.execute(query, (nuevo_valor, libro_id))
            conexion.commit()

            if cursor.rowcount > 0:
                print("Libro actualizado correctamente.")
            else:
                print("No se encontró un libro con ese ID.")
        except Exception as e:
            print(f"Error al actualizar el libro: {e}")
        else:
            print("Opción no válida.")
        finally:
            cursor.close()
            conexion.close()

def eliminar_libro(): #Función para eliminar libros
    conexion = conectar_db()
    cursor = conexion.cursor()

    libro_id = input("Ingrese el ID del libro que desea eliminar: ")

    try:
        cursor.execute("DELETE FROM Libros WHERE libro_id = %s", (libro_id,))
        conexion.commit()

        if cursor.rowcount > 0:
            print("Libro eliminado correctamente.")
        else:
            print("No se encontró un libro con ese ID.")
    except Exception as e:
        print(f"Error al eliminar el libro: {e}")
    finally:
        cursor.close()
        conexion.close()

def menu_libros(): #Menú para gestiionar libros
    while True:
        print("\n--- Gestión de Libros ---")
        print("1) Registrar un nuevo libro")
        print("2) Ver todos los libros")
        print("3) Actualizar información de un libro")
        print("4) Eliminar un libro")
        print("5) Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_libro()
        elif opcion == "2":
            ver_libros()
        elif opcion == "3":
            actualizar_libro()
        elif opcion == "4":
            eliminar_libro()
        elif opcion == "5":
            print("Saliendo del menú de libros.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")