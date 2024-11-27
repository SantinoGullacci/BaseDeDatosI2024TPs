import mysql.connector
from datetime import datetime

def conectar_db(): #Conectamos la base de datos
    return mysql.connector.connect(
        host="localhost",
        user="tu_usuario",
        password="tu_contraseña",
        database="tu_base_de_datos"
    )

def calcular_diferencia_meses(fecha_inicio, fecha_fin): #Función para poder calcular la diferencia en meses entre dos fechas
    diferencia = (fecha_fin.year - fecha_inicio.year) * 12 + fecha_fin.month - fecha_inicio.month
    return diferencia

def reporte_morosos(): #Función para generar el reporte de morosos
    conexion = conectar_db()
    cursor = conexion.cursor()

    try: #Obtenemos todas las cuotas pendientes de pago
        cursor.execute("SELECT dni_usuario, fecha_registro FROM Cuotas WHERE estado_pago = 'PENDIENTE'")
        cuotas_pendientes = cursor.fetchall()

        if cuotas_pendientes:
            total_meses_morosidad = 0
            cantidad_morosos = 0
            fecha_actual = datetime.now()

            for cuota in cuotas_pendientes: #Calcular la cantidad de meses de morosidad por socio
                dni_usuario = cuota[0]
                fecha_registro = cuota[1]

                meses_morosidad = calcular_diferencia_meses(fecha_registro, fecha_actual) #Calculamos los meses de morosidad para cada cuota pendiente de pago

                total_meses_morosidad += meses_morosidad
                cantidad_morosos += 1

            if cantidad_morosos > 0: #Calculamos el promedio de meses de morosidad
                promedio_meses = total_meses_morosidad / cantidad_morosos
                print(f"Promedio de meses de morosidad de los socios: {promedio_meses:.2f} meses")
            else:
                print("No hay socios morosos.")
        else:
            print("No hay cuotas pendientes.")

    except Exception as e:
        print(f"Error al generar el reporte de morosos: {e}")
    finally:
        cursor.close()
        conexion.close()