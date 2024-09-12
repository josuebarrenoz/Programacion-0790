def todos (data):
    pass

def producto (data):
    producto = input("\nIngrese producto a mostrar: ")
    producto = producto.lower()
    if producto in data:
        mensaje = f"|Producto = {producto}, Precio = {data[producto]["Precio"]}, Cantidad = {data[producto]["Cantidad"]}|"
        print("-"*len(mensaje))
        print(mensaje)
        print("-"*len(mensaje))
        return data
    else:
        print(f"\nEl producto nombrado {producto} no se encuentra en el inventario")
        return data