"""Este examen consiste en implementar un sistema básico de gestión de inventario para un supermercado utilizando Python. El sistema debe permitir a los usuarios realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los productos en el inventario. Los datos del inventario deben estar almacenados en un archivo JSON llamado inventario.json."""

import json
import menu, repet, crear, mostrar, actualizar, eliminar

# Función principal del programa. Recibe los datos del inventario y llama al menu principal.
def run():
    # Leer los datos del inventario desde el archivo JSON.
    try:
        with open ("inventario.json","r") as file:
            data = json.load(file)
        file.close()
    except FileNotFoundError:
        print("\nNo existe ningun archivo Json con el nombre inventario.json ")
        with open ("inventario.json","w") as file:
            data = {}
        file.close()
        print("\nArchivo creado automaticamente")

    #opciones del Programa
    while True:
        opcion=menu.principal()
        if opcion=="1":
            crear.producto(data)
        elif opcion=="2":
            mostrar.todos(data)
        elif opcion=="3":
            mostrar.producto(data)
        elif opcion=="4":
            actualizar.producto(data)
        elif opcion=="5":
            eliminar.producto(data)
        elif opcion=="6":
            break

    # Guardar los datos del inventario en el archivo JSON.
    with open ("inventario.json","w") as file:
        data = json.dump(data,file)
    file.close()

if __name__ == "__main__":
    # Llamar al programa principal con los datos del inventario.
    run()
    repet.ition(run)