import verificacion as val
def producto(data):
    #Agregando un elemento a la data
    print("\nAgregando un producto en la lista")
    nombre=val.nombre()
    #Verificar si esta el elemento en el diccionario
    if nombre in data:
        print("\nEste producto ya se encuentra en la lista.")
        return data
    #Si no esta, agregarlo
    else:
        precio=val.precio()
        cantidad=val.cantidad()
        print("\nProducto agregado exitosamente.")
        data[nombre]= {"Precio":precio,"Cantidad":cantidad}
        return data

if __name__=="__main__":
    print("\nEsto es un modulo del programa CRUD. Busca en la carpeta el archivo main.py y ejecutalo")