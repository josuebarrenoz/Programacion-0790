"""
Crear un programa en Python que permita al usuario gestionar una lista de compras.
El programa debe mostrar un menú con las siguientes opciones:

Agregar un artículo a la lista.
Eliminar un artículo de la lista.
Mostrar la lista completa.
Salir del programa.

El programa debe permitir al usuario elegir una opción del menú.Dependiendo de la opción elegida, el programa debe realizar la acción correspondiente:

Si el usuario elige "Agregar", debe pedirle que ingrese el nombre del artículo y agregarlo a la lista.
Si el usuario elige "Eliminar", debe pedirle que ingrese el nombre del artículo y eliminarlo de la lista.
Si el usuario elige "Mostrar", debe mostrar todos los artículos de la lista.
Si el usuario elige "Salir", el programa debe finalizar.

El programa debe seguir mostrando el menú y permitiendo al usuario realizar acciones hasta que elija la opción "Salir".
"""
#Declarando variables
list=[]
#Mostrando Bienvenida
print("\nBienvenidos a Practica 4\nSeccion 2 Programacion\nGrupo 3\nJosue Barreno")
#Reiterando el programa hasta que el usuario lo detenga
while True:
    #Imprimiendo el  menu y capturando la opcion
    valor = input("\n---       Menu       ---\n--- Lista de compras ---\n1. Agregar artículo\n2. Eliminar artículo\n3. Mostrar lista\n4. Salir\n\nElige una opción: ")
    #Determinar si es Numerico o no
    if valor.isnumeric()==True:
        #Convirtiendolo en un entero
        valor=int(valor)
        #Condiccionando la accion para un valor en concreto
        if valor ==1:
            #Añadiendo el elemento
            elemento = input("Ingresa el nombre del artículo: ")
            elemento=elemento.lower()
            list.append(elemento)
        elif valor==2:
            #Removiendo el elemento
            elemento = input("Ingresa el nombre del artículo: ")
            for i in list:
                if elemento.lower() == i:
                    list.remove(i)
        elif valor==3:
            #mostrando la lista
            print("\n--- Lista de compras ---\n")
            for i in list:
                print(i,end="\n")
            print("")
        elif valor ==4:
            #Cerrando el programa
            print("\nGracias por usar el programa de @josuebarrenoz")
            break
        #Mostrando error, si digitan un numero fuera de la lista de opciones
        else:
            print("Reintenta, no es una opcion valida")
    #Mostrando error, si tipean una frase
    else:
        print("Reintenta, no es una opcion valida")
