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

if __name__=="__main__":
    print("\nEsto es un modulo del programa CRUD. Busca en la carpeta el archivo main.py y ejecutalo")