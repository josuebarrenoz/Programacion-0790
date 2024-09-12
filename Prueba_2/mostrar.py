def todos (data):
    # Determinar la longitud de la cadena más larga para el encabezado
    aux = 0
    cont= 0
    for producto in data:
        dato = f"{producto}{data[producto]["Precio"]}{data[producto]["Cantidad"]}"
        cont = len(dato)
        if cont > aux:
            aux = cont
    # Mostrar el encabezado
    print("\n--- Productos en el Inventario ---")
    print("-" * (aux+35))

    # Mostrar los productos
    for producto in data:
        mensaje = f"Producto = {producto}, Precio = {data[producto]["Precio"]}, Cantidad = {data[producto]["Cantidad"]}"
        print(mensaje)
        print("-" * (aux+35))


def producto (data):
    # Obtener el nombre del producto a mostrar
    producto = input("\nIngrese producto a mostrar: ")
    producto = producto.lower()
    # Verificar si el producto existe en el inventario
    if producto in data:
        mensaje = f"|Producto = {producto}, Precio = {data[producto]["Precio"]}, Cantidad = {data[producto]["Cantidad"]}|"
        print("\n"+"-"*len(mensaje))
        print(mensaje)
        print("-"*len(mensaje))
        return data
    else:
        print(f"\nEl producto nombrado {producto} no se encuentra en el inventario")
        return data

if __name__=="__main__":
    print("\nEsto es un modulo del programa CRUD. Busca en la carpeta el archivo main.py y ejecutalo")