import mysql.connector

def conectar_db():  #Conectamos la base de datos
    return mysql.connector.connect(
        host="localhost",
        user="tu_usuario",
        password="tu_contraseña",
        database="tu_base_de_datos"
    )

def buscar_libros():  #Función para filtrar los libros por atributos seleccionados por el usuario
    conexion = conectar_db()
    cursor = conexion.cursor()

    print("Seleccione el criterio de búsqueda:")
    print("1) Título")
    print("2) Autor")
    print("3) Libros con préstamos (INNER JOIN con Usuarios)")

    opcion = input("Ingrese la opción (1-3): ")

    if opcion == "1":
        texto = input("Ingrese el título (o parte del título) a buscar: ")
        query = "SELECT * FROM Libros WHERE titulo LIKE %s ORDER BY anio_publicacion DESC"
        parametro = ("%" + texto + "%",)
    elif opcion == "2":
        texto = input("Ingrese el autor (o parte del autor) a buscar: ")
        query = "SELECT * FROM Libros WHERE autor LIKE %s ORDER BY titulo"
        parametro = ("%" + texto + "%",)
    elif opcion == "3":
        query = """
        SELECT 
            Libros.libro_id, Libros.titulo, COUNT(Prestamos.id) AS total_prestamos
        FROM 
            Libros
        INNER JOIN 
            Prestamos ON Libros.libro_id = Prestamos.libro_id
        GROUP BY 
            Libros.libro_id, Libros.titulo
        HAVING 
            total_prestamos > 0
        ORDER BY 
            total_prestamos DESC
        """
        parametro = ()
    else:
        print("Opción no válida.")
        cursor.close()
        conexion.close()
        return

    try:
        cursor.execute(query, parametro)
        libros = cursor.fetchall()

        if libros:
            print("Resultados de la búsqueda de libros:")
            for libro in libros:
                if opcion == "3":  #Caso especial para mostrar préstamos
                    print(f"ID: {libro[0]}, Título: {libro[1]}, Total de Préstamos: {libro[2]}")
                else:
                    print(f"ID: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}, Género: {libro[3]}, Editorial: {libro[4]}, Año: {libro[5]}")
        else:
            print("No se encontraron libros con ese criterio.")
    except Exception as e:
        print(f"Error al realizar la búsqueda: {e}")
    finally:
        cursor.close()
        conexion.close()

def buscar_usuarios():  #Función para filtrar los usuarios por atributos seleccionados por el usuario
    conexion = conectar_db()
    cursor = conexion.cursor()

    print("Seleccione el criterio de búsqueda: ")
    print("1) DNI")
    print("2) Usuarios con préstamos activos (INNER JOIN con Prestamos)")
    print("3) Usuarios con cuotas pendientes (LEFT JOIN con Cuotas)")

    opcion = input("Ingrese la opción (1-3): ")

    if opcion == "1":
        texto = input("Ingrese el DNI (o parte del DNI) a buscar: ")
        query = "SELECT * FROM Usuarios WHERE dni LIKE %s ORDER BY nombre"
        parametro = ("%" + texto + "%",)
    elif opcion == "2":
        query = """
        SELECT 
            Usuarios.dni, Usuarios.nombre, Usuarios.apellido, COUNT(Prestamos.id) AS prestamos_activos
        FROM 
            Usuarios
        INNER JOIN 
            Prestamos ON Usuarios.dni = Prestamos.dni_usuario
        WHERE 
            Prestamos.fecha_devolucion IS NULL
        GROUP BY 
            Usuarios.dni, Usuarios.nombre, Usuarios.apellido
        HAVING 
            prestamos_activos > 0
        ORDER BY 
            prestamos_activos DESC
        """
        parametro = ()
    elif opcion == "3":
        query = """
        SELECT 
            Usuarios.dni, Usuarios.nombre, Usuarios.apellido, COUNT(Cuotas.id) AS cuotas_pendientes
        FROM 
            Usuarios
        LEFT JOIN 
            Cuotas ON Usuarios.dni = Cuotas.dni_usuario AND Cuotas.estado_pago = 'PENDIENTE'
        GROUP BY 
            Usuarios.dni, Usuarios.nombre, Usuarios.apellido
        HAVING 
            cuotas_pendientes > 0
        ORDER BY 
            cuotas_pendientes DESC
        """
        parametro = ()
    else:
        print("Opción no válida.")
        cursor.close()
        conexion.close()
        return

    try:
        cursor.execute(query, parametro)
        usuarios = cursor.fetchall()

        if usuarios:
            print("Resultados de la búsqueda de usuarios:")
            for usuario in usuarios:
                if opcion in ["2", "3"]:  #Mostrar campos especiales para estas opciones
                    print(f"DNI: {usuario[0]}, Nombre: {usuario[1]}, Apellido: {usuario[2]}, Total: {usuario[3]}")
                else:
                    print(f"DNI: {usuario[0]}, Nombre: {usuario[1]}, Apellido: {usuario[2]}, Email: {usuario[3]}, Teléfono: {usuario[4]}, Fecha de Registro: {usuario[5]}")
        else:
            print("No se encontraron usuarios con ese criterio.")
    except Exception as e:
        print(f"Error al realizar la búsqueda: {e}")
    finally:
        cursor.close()
        conexion.close()

def menu_busqueda():  #Menú de búsqueda y filtrado
    while True:
        print("\n-Menú de Búsqueda y Filtrado-")
        print("1) Buscar libros")
        print("2) Buscar usuarios")
        print("3) Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            buscar_libros()
        elif opcion == "2":
            buscar_usuarios()
        elif opcion == "3":
            print("Saliendo del menú de búsqueda.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")