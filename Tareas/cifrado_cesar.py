def repit():
    #Repetimos usando un While True.
    while True:
        rep = input("\nDesea repetir el Programa? y/n: ")
        if rep.lower()=="y":
            run()
        elif rep.lower()=="n":
            print("\nGracias por usar el programa de @josuebarrenoz")
            break
        else:
            print("Escribe una opcion valida")

def cifrado(numero):
    #Aqui es donde se cifra/descifra, es decir la verdadera magia
    #Lo primero es declarar variables
    abc="abcdefghijklmnopqrstuvwxyz"
    cifrado=""
    #Un while True para validar la clave y que no se rompa el programa por un error.
    while True:
        try:
            clave = int(input("\nEscribe la clave de cifrado: "))
            break
        except ValueError:
            print("\nEscribe un Numero Entero")
    #Aqui le pedimos al usuario la palabra
    palabra = input("\nEscribe una palabra a cifrar: ")
    palabra = palabra.lower()
    #Y el cifrado ocurre en un ciclo for
    for i in range (len(palabra)):
        # Este if existe por que existen espacios en la vida
        if palabra[i]==" ":
            cifrado=cifrado+" "
        else:
            # Este try existe, para que si pongan una coma, no se me caiga el programa
            try:
                #¿Que es lo que sucede aqui?
                #Primero el for va en un rango del tamaño de la palabra
                #De la formula de abajo lo mas importante es palabra[i] ya que ella secciona el primer caracter de palabra
                #Teniendo el primer caracter de la palabra inmediatamente buscando el indice en el abc edario
                #Eso genera un numero. Si le sumo o le resto la clave, me cambiara el indice
                #Que puedo de nuevo buscarlo en el mismo abc edario.
                #Lo importante es que como el abc edario es finito, tengo que modularlo
                #El tamaño del modulo, será siempre el tamaño del abc edario
                #Como se darán cuenta, el primer caracter genera un numero que es el indice
                #La opcion me dice que si lo sumo o lo resto
                #La clave cuanto tengo que sumar en los indices
                #Y el modulo me permite no salir del ancho del abc edario
                #Con el numero nuevo, solo tengo que traer cual letra del abc edario corresponde al numero
                #Y cifrado es la concatenacion de todos los i dentro del ciclo for
                cifrado=cifrado+abc[(abc.index(palabra[i])+(((-1)**numero)*(clave)))%len(abc)]
            except ValueError:
                #Esta es facil. Como no pertenece al diccionario, concatenalo
                cifrado=cifrado+palabra[i]

    #Aqui declarando otra variable para que el print se vea hermoso
    if numero == 1:
        opcion = "Cifrada"
    else:
        opcion = "Descifrada"
    #Teniendo la palabra opcion bien definida y la palabra cifrada se imprime
    print(f"\nLa palabra {opcion} es {cifrado}")


def run():
    #Aqui, el mero programa
    #While True, para validar bien el menu

    while True:
        #Se le pide opciones al usuario
        try:
            opcion=int(input("\nMenu\n1.Cifrar palabra\n2.Descifrar Palabra\n3.Salir del menu\n\nEscribe tu opcion: "))
            #Aqui que hace las opciones a cara del usuario
            if opcion==1:
                cifrado(opcion)
            elif opcion==2:
                cifrado(opcion)
            elif opcion==3:
                break
            else:
                print("\nEscribe un numero correcto")
        except ValueError:
            print("\nEscribe un numero..")

#Aqui empieza el programa
if __name__=="__main__":
    #La bienvenida
    print("\nBienvenidos a lo que debio ser la Practica 5\nSeccion 2 Programacion\nJosue Barreno")
    #El plato fuerte
    run()
    #Repetir el programa
    repit()
