"""
Escribir un programa que solicite al usuario un
conjunto de numeros primos y calcule el cuadrado de
la suma de estos. Tenga en cuenta:

    - Si el usuario ingresa un valor no numerico
    ignorar dicho valor, enviar un mensaje y permitir reintentos
    -Si el usuario ingresa un numero no primo
    ignorar dicho valor, enviar un mensaje y permitir reintentos
    -Si el usuario ingresa al string "stop" detener la solicitud
    de números al usuario
"""
list = []
print("Bienvenidos a Practica 3\n Seccion 2 Programacion\n Josue Barreno")
while True:
    primo = input("\nIngrese la cantidad de numeros primos que desee, \n escriba <<stop>> para dejar de enviar numeros: ")
    if primo.isnumeric()== True:
        primo = int(primo)
        cont=0
        for n in range (2,primo):
            if primo%n==0:
                cont=cont+1
        if cont==0:
            list.append(primo)
        else:
            print("\nEsto NO ES UN NUMERO PRIMO, agregue uno correcto\n")
    elif primo.lower()=="stop":
        break
    else:
        print("\nEste valor no es un NUMERO, por favor reintente el numero\n")

sum=0
for i in list:
    sum=sum+ i**2

print(f"\nEl valor de la suma es {sum}\n\n Gracias por usar el programa de @josuebarrenoz")
