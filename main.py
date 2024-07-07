import funciones as ff
import os 
import csv

op = 0 #para guardar la opción del menu
nombre_campos = ["id_producto","nombre_producto","cantidad","precio"]

bienvenida = """******************************************************
    BIENVENIDO AL SISTEMA DE GESTION DE INVENTARIOS"""

selecciona = """******************************************************
                ELIJE QUE QUIERES HACER
******************************************************"""

nombre_csv = "inventario.csv"
os.system("cls")

ff.crear_archivo(nombre_csv)


print(bienvenida)
while op!=7:
    print(selecciona)
    ff.mostrar_menu()
    op = ff.elegir_opcion_menu()
    if op==1:
        os.system("cls")
        ff.mostrar_inventario(nombre_csv)
        os.system("pause")
    elif op==2:
        os.system("cls")
        ff.buscar_producto(nombre_csv)
        os.system("pause")
    elif op==3:
        os.system("cls")
        ff.actualizar_stock(nombre_csv,nombre_campos)
        os.system("pause")
    elif op==4:
        os.system("cls")
        ff.agregar_producto(nombre_csv,nombre_campos)
        os.system("pause")
    elif op==5:
        os.system("cls")
        ff.eliminar_producto(nombre_csv,nombre_campos)
        os.system("pause")
    elif op==6:
        ff.convertir_csv_a_dict(nombre_csv)
        os.system("pause")
    os.system("cls")


