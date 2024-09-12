import verificacion as val
import menu

def producto(data):
        #Primero pedir la info
        producto = input("\nIngrese producto a modificar: ")
        producto = producto.lower()
        #Luego verificar si el producto existe en el inventario
        if producto in data:
            #Consultar que tipo de Modificacion se desea hacer al producto
            opcion=menu.modificar()
            #Si la opcion es la de modificar nombre, precio o cantidad
            if opcion=="1":
                nombre=val.nombre()
                info=data.pop(producto)
                data[nombre]=info
                print("\nProducto modificado exitosamente")
                return data
            elif opcion=="2":
                precio = val.precio()
                data[producto]["Precio"]=precio
                print("\nPrecio modificado exitosamente")
                return data
            elif opcion=="3":
                cantidad = val.cantidad()
                data[producto]["Cantidad"] = cantidad
                print("\nCantidad modificada exitosamente")
                return data
        else:
            print(f"\nEl producto nombrado {producto} no se encuentra en el inventario")
            return data

if __name__=="__main__":
    print("\nEsto es un modulo del programa CRUD. Busca en la carpeta el archivo main.py y ejecutalo")