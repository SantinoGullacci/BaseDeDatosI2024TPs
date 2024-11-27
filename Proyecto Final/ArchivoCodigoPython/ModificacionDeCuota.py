import mysql.connector

def conectar_db(): #Conectamos la base de datos
    return mysql.connector.connect(
        host="localhost",
        user="tu_usuario",
        password="tu_contraseña",
        database="tu_base_de_datos"
    )

def modificar_cuota(): #Función para modificar las cuotas
    conexion = conectar_db()
    cursor = conexion.cursor()

    dni_usuario = input("Ingrese el DNI del usuario: ") #Solicitamos el mes y el año de la cuota que se va a modificar
    mes = int(input("Ingrese el mes de la cuota a modificar (1-12): "))
    anio = int(input("Ingrese el año de la cuota a modificar (YYYY): "))

    nuevo_monto = float(input("Ingrese el nuevo monto para la cuota: ")) #Solicitamos el nuevo monto

    try: #Comprobamos si existe la cuota con el mes, año y dni_usuario proporcionados por el usuario
        cursor.execute("""
            SELECT * FROM Cuotas 
            WHERE dni_usuario = %s AND mes = %s AND anio = %s
        """, (dni_usuario, mes, anio))
        
        cuota = cursor.fetchone()

        if cuota: #Si la cuota existe, actualizamos el monto
            cursor.execute("""
                UPDATE Cuotas 
                SET monto = %s 
                WHERE dni_usuario = %s AND mes = %s AND anio = %s
            """, (nuevo_monto, dni_usuario, mes, anio))
            conexion.commit()

            if cursor.rowcount > 0:
                print("Cuota modificada correctamente!")
            else:
                print("No se pudo modificar la cuota.")
        else:
            print("No se encontró una cuota con esos datos.")
    except Exception as e:
        print(f"Error al modificar la cuota: {e}")
    finally:
        cursor.close()
        conexion.close()