num = int(input("Bienvenidos a Practica 2\n Seccion 2 Programacion\n Josue Barreno\n\nEscribe un numero entero:"))

if num<0:
    print("\nEl numero es negativo\n")
elif num>100:
    print("\nEl numero es mayor que 100\n")
elif num%6==0:
    print("\nEl numero es divisible por 6\n")
elif num%3==0:
    print("\nEl numero es divisible por 3\n")
elif num%2==0:
    print("\nEl numero es divisible por 2\n")
else:
    print("\nEl numero no cumple ningún condición especial\n")