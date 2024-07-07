import os 
import csv
import json

def mostrar_menu():
    menu = """[1] Mostrar inventario.
[2] Buscar producto
[3] Actualizar stock de un producto en el inventario
[4] Agregar nuevo producto
[5] Eliminar producto
[6] Exportar datos a JSON
[7] Salir...
--> """
    print(menu,end="")

def elegir_opcion_menu():
    while True:
        try:
            op = int(input())
            if op>0 and op<8:
                return op
            else:
                raise ValueError
        except:
            print("Selecciona una opcion valida. --> ",end="")


def crear_archivo(ruta):
    if not os.path.isfile(ruta):
        with open(ruta,"w",newline="") as archivo:
            nombre_campos = ["id_producto","nombre_producto","cantidad","precio"]
            escritor = csv.DictWriter(archivo, fieldnames=nombre_campos)
            escritor.writeheader()

def mostrar_inventario(inventario):
    with open(inventario,"r",newline="") as archivo:
        for fila in archivo:
            print(fila)

def buscar_producto(inventario):
    id = input("Ingresa el ID del producto: ")
    encontrado = False

    with open(inventario,"r",newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila["id_producto"] == id:
                print(fila)
                encontrado = True

        if not encontrado:
            print("Ese ID de producto no existe en el inventario.")

def actualizar_stock(inventario,campos):
    id = input("Ingresa el ID del producto: ")
    encontrado = False

    productos = []
    with open(inventario,"r",newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            productos.append(fila)

    for item in productos:
        if item["id_producto"] == id:
            item["cantidad"] = input("Ingresa la nueva cantidad del producto: ")
            encontrado = True
            break

    if encontrado:
        with open(inventario,"w",newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            print(productos)
            escritor.writerows(productos)
    else:
        print("Producto no encontrado.")

def agregar_producto(inventario,campos):
    id = input("Ingresa el id del producto: ")
    nombre = input("Ingresa el nombre del producto: ")
    stock = input("Ingresa el stock del producto: ")
    precio = input("Ingresa el precio del producto: ")

    with open(inventario,"a",newline="") as archivo:
        escritor = csv.DictWriter(archivo,fieldnames=campos)
        escritor.writerow({"id_producto":id,"nombre_producto":nombre,"cantidad":stock,"precio":precio})

def eliminar_producto(inventario,campos):
    id = input("Ingresa el ID del producto: ")
    encontrado = False

    productos = []
    with open(inventario,"r",newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            productos.append(fila)

    for item in productos:
        if item["id_producto"] == id:
            index = productos.index(item)
            encontrado = True
            break
    del(productos[index])

    if encontrado:
        with open(inventario,"w",newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(productos)
    else:
        print("Producto no encontrado.")
    

def convertir_csv_a_dict(inventario):
    productos = {}
    productos["inventario"] = []
    with open(inventario,"r",newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            productos["inventario"].append(fila)    

        with open("export.json",'w',) as j:
            json.dump(productos,j,indent=4)
            





        

