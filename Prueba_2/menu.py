def principal():
    while True:
        opcion = input("\n--- Gestión de Inventario ---\n1. Crear producto\n2. Mostrar todos los productos\n3. Mostrar información de un producto\n4. Actualizar producto\n5. Eliminar producto\n6. Salir\n\nEscribe la opcion: ")
        if opcion == "1" or "2" or "3" or "4" or "5" or "6":
            return opcion
        else:
            print("\nEscribe una opcion valida")

def modificar():
        opcion = input("\n--- Gestión de Inventario ---\n1. Modificar el nombre\n2. Modificar el precio\n3. Modificar la cantidad\nEscribe la opcion: ")
        if opcion == "1" or "2" or "3":
            return opcion
        else:
            print("\nEscribe una opcion valida")

if __name__=="__main__":
    print("\nEsto es un modulo del programa CRUD. Busca en la carpeta el archivo main.py y ejecutalo")