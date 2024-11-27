import mysql.connector

def menu_principal():
    while True:
        print("\nGestión de Usuarios")
        print("1) Agregar Usuario")
        print("2) Ver Usuarios")
        print("3) Actualizar Usuario")
        print("4) Eliminar Usuario")
        print("5) Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            ver_usuarios()
        elif opcion == "3":
            actualizar_usuario()
        elif opcion == "4":
            eliminar_usuario()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

def agregar_usuario():
    print("\n-Agregar Usuario-")
    dni = input("DNI: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    telefono = input("Teléfono: ")

    try: #Conectamos a la base de datos e inserción
        conexion = mysql.connector.connect(host="localhost", user="root", password="", database="mi_biblioteca")
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuarios (dni, nombre, apellido, email, telefono, fecha_registro) VALUES (%s, %s, %s, %s, %s, CURDATE())", 
                       (dni, nombre, apellido, email, telefono))
        conexion.commit()
        print("Usuario agregado exitosamente.")
    except mysql.connector.Error as e:
        print(f"Error al agregar usuario: {e}")
    finally:
        cursor.close()
        conexion.close()

def ver_usuarios():
    print("\n-Ver Usuarios-")
    print("1) Ver todos los usuarios")
    print("2) Buscar usuario por DNI")
    opcion = input("Seleccione una opción: ")

    try:
        conexion = mysql.connector.connect(host="localhost", user="root", password="", database="mi_biblioteca")
        cursor = conexion.cursor()

        if opcion == "1":
            cursor.execute("SELECT * FROM usuarios")
            usuarios = cursor.fetchall()
            for usuario in usuarios:
                print(usuario)
        elif opcion == "2":
            dni = input("Ingrese el DNI del usuario: ")
            cursor.execute("SELECT * FROM usuarios WHERE dni = %s", (dni,))
            usuario = cursor.fetchone()
            if usuario:
                print(usuario)
            else:
                print("Usuario no encontrado.")
        else:
            print("Opción no válida.")
    except mysql.connector.Error as e:
        print(f"Error al consultar usuarios: {e}")
    finally:
        cursor.close()
        conexion.close()

def actualizar_usuario():
    print("\n-Actualizar Usuario-")
    dni = input("Ingrese el DNI del usuario a actualizar: ")

    try:
        conexion = mysql.connector.connect(host="localhost", user="root", password="", database="mi_biblioteca")
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE dni = %s", (dni,))
        usuario = cursor.fetchone()
        if not usuario:
            print("Usuario no encontrado.")
            return

        print("1) Actualizar Nombre")
        print("2) Actualizar Apellido")
        print("3) Actualizar Email")
        print("4) Actualizar Teléfono")
        opcion = input("Seleccione el dato a actualizar: ")

        if opcion == "1":
            nuevo_valor = input("Nuevo Nombre: ")
            cursor.execute("UPDATE usuarios SET nombre = %s WHERE dni = %s", (nuevo_valor, dni))
        elif opcion == "2":
            nuevo_valor = input("Nuevo Apellido: ")
            cursor.execute("UPDATE usuarios SET apellido = %s WHERE dni = %s", (nuevo_valor, dni))
        elif opcion == "3":
            nuevo_valor = input("Nuevo Email: ")
            cursor.execute("UPDATE usuarios SET email = %s WHERE dni = %s", (nuevo_valor, dni))
        elif opcion == "4":
            nuevo_valor = input("Nuevo Teléfono: ")
            cursor.execute("UPDATE usuarios SET telefono = %s WHERE dni = %s", (nuevo_valor, dni))
        else:
            print("Opción no válida.")
            return

        conexion.commit()
        print("Usuario actualizado exitosamente!")
    except mysql.connector.Error as e:
        print(f"Error al actualizar usuario: {e}")
    finally:
        cursor.close()
        conexion.close()

def eliminar_usuario():
    print("\n-Eliminar Usuario-")
    dni = input("Ingrese el DNI del usuario a eliminar: ")

    try:
        conexion = mysql.connector.connect(host="localhost", user="root", password="", database="mi_biblioteca")
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE dni = %s", (dni,))
        usuario = cursor.fetchone()
        if not usuario:
            print("Usuario no encontrado.")
            return

        confirmacion = input(f"¿Está seguro de eliminar al usuario con DNI {dni}? (s/n): ")
        if confirmacion.lower() == "s":
            cursor.execute("DELETE FROM usuarios WHERE dni = %s", (dni,))
            conexion.commit()
            print("Usuario eliminado exitosamente.")
        else:
            print("Operación cancelada.")
    except mysql.connector.Error as e:
        print(f"Error al eliminar usuario: {e}")
    finally:
        cursor.close()
        conexion.close()