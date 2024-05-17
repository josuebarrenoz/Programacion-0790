num = int(input("Bienvenidos a Practica 2\n Seccion 2 Programacion\n Josue Barreno\nEjercicio 2\n\nIngrese una clasificacion:"))

if num<0 or num>100:
    print("\nClasificación Invalida\n")
elif num==100:
    print("\nClasificación Perfecta\n")
elif num>89:
    print("\nExcelente\n")
elif num>69:
    print("\nBueno\n")
elif num>49:
    print("\nSuficiente\n") 
else:
    print("\nInsuficiente\n")