from BusquedaYFiltrado import menu_busqueda
from GestionDeLibros import menu_libros
from GestionDeUsuarios import menu_principal
from ManejoDePrestamos import calcular_multa
from ModificacionDeCuota import modificar_cuota
from ReporteDeMorosos import calcular_diferencia_meses,reporte_morosos

def main():
    while True:
        print("\n-Gestion de biblioteca-")
        print("1) Busqueda y filtrado")
        print("2) Gestion de libros")
        print("3) Gestion de usuarios")
        print("4) Manejo de prestamos")
        print("5) Modificacion de cuotas")
        print("6) Reporte de morosos")
        print("7) Salir")
        
        opcion=int(input("Elija una opcion: "))

        if opcion==1:
            menu_busqueda()
        elif opcion==2:
            menu_libros()
        elif opcion==3:
            menu_principal()
        elif opcion==4:
            dni_usuario=int(input("Ingrese el DNI del usuario a calcular la multa: "))
            libro_id=int(input("Ingrese el ID del libro que tomo el usuario: "))
            calcular_multa(dni_usuario,libro_id)
        elif opcion==5:
            modificar_cuota()
        elif opcion==6:
            print("\n-Gestion de morosos-")
            print("1) Calcular diferencia de meses")
            print("2) Reporte de morosos")
            
            opcion2=int(input("Elija una opcion: "))

            if opcion2==1:
                calcular_diferencia_meses()
            elif opcion2==2:
                reporte_morosos()
            else:
                print("Opcion incorrecta.")

        elif opcion==7:
            break
        else:
            print("Opcion incorrecta.")

if "__main__" == __name__:
    main()