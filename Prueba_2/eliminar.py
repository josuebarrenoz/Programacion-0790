import verificacion as val
def producto(data):
    print("\nEliminando un producto en la lista")
    nombre = val.nombre()
    #Verificar si esta el elemento en el diccionario
    if nombre in data:
        data.pop(nombre)
        print("\nProducto eliminado exitosamente.")
        return data
    else:
        print("\nEste producto no se encuentra en la lista.")