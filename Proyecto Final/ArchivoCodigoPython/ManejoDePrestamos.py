import mysql.connector
from datetime import datetime

def conectar_db(): #Conectamos la base de datos
    return mysql.connector.connect(
        host="localhost",
        user="tu_usuario",
        password="tu_contraseña",
        database="tu_base_de_datos"
    )

def calcular_multa(dni_usuario, libro_id): #Función para calcular las multas por atraso
    conexion = conectar_db()
    cursor = conexion.cursor()

    try: #Obtenemos los datos del préstamo
        cursor.execute("""
            SELECT fecha_prestamo, fecha_devolucion
            FROM Prestamos
            WHERE dni_usuario = %s AND libro_id = %s
        """, (dni_usuario, libro_id))
        prestamo = cursor.fetchone()

        if prestamo:
            fecha_prestamo = prestamo[0]
            fecha_devolucion = prestamo[1]

            if fecha_devolucion is None: #Si no hubiese fecha de devolución, significa que aún no se ha devuelto
                print("El libro aún no ha sido devuelto.")
                return

            fecha_devolucion_real = datetime.strptime(fecha_devolucion, "%Y-%m-%d") #Calculamos los días de atraso
            fecha_prestamo_real = datetime.strptime(fecha_prestamo, "%Y-%m-%d")
            dias_retraso = (fecha_devolucion_real - fecha_prestamo_real).days

            if dias_retraso > 0: #Obtenemos la cuota mensual del usuario
                cursor.execute("""
                    SELECT monto
                    FROM Cuotas
                    WHERE dni_usuario = %s AND mes = MONTH(CURDATE()) AND anio = YEAR(CURDATE())
                """, (dni_usuario,))
                cuota = cursor.fetchone()

                if cuota:
                    cuota_mensual = cuota[0]
                    multa = cuota_mensual * 0.03 * dias_retraso
                    print(f"El préstamo está retrasado por {dias_retraso} días.")
                    print(f"La multa por el retraso es: ${multa:.2f}")
                else:
                    print("No se encontró la cuota mensual del usuario.")
            else:
                print("No hay retraso en la devolución del libro.")
        else:
            print("No se encontró el préstamo para este libro y usuario.")

    except Exception as e:
        print(f"Error al calcular la multa: {e}")
    finally:
        cursor.close()
        conexion.close()