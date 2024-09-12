#Este modulo verifica los datos para almacenar en la data
def nombre():
    while True:
        try:
            nombre = input("Nombre: ")
            nombre = nombre.lower()
            return nombre
        except TypeError:
            print("El nombre debe ser una cadena de caracteres.")

def precio():
    while True:
        try:
            precio = float(input("Precio: "))
            if precio < 0:
                raise ValueError
            return precio
        except ValueError:
            print("El precio debe ser un número positivo.")
        except TypeError:
            print("El precio debe ser un número.")

def cantidad():
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad < 0:
                raise ValueError
            return cantidad
        except ValueError:
            print("La cantidad debe ser un número entero positivo.")
        except TypeError:
            print("La cantidad debe ser un número.")

if __name__=="__main__":
    print("\nEsto es un modulo del programa CRUD. Busca en la carpeta el archivo main.py y ejecutalo")