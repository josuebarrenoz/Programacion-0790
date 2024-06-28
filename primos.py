#Presentación
print("Bienvenido al programa de suma de numeros primos\nSección 2 de Programacion 0790\nRealizado por:Josue Barreno\n")

#Repeticion del Programa
rep = True
while rep:

    #Validación Numerica
    ciclo=0
    while True:
        num = input("Escribe un numero: ")
        if num.isnumeric() == True:
            num = int(num)
            break
        else:
            ciclo+=1
            print("El valor aportado no es numerico, intente de nuevo\n")
            print("Intento numero {}".format(ciclo))

    #Programa de suma de nuemero primos
    sum =0
    list=[] #Recurso para saber si generaba primos
    print("")
    for n in range (2,num+1):
        cont=0
        for i in range (2,n):
            if n%i==0:
                cont=cont+1
            if cont>1:
                break
        if cont<1:
            list.append(n) #Recurso para saber si generaba primos
            sum=sum+n

        # Barra para medir velocidad del codigo, apoyandose en el ciclo for.
        frac = n/num
        completed = int(frac*30)
        missing = 30 - completed
        print(f"[{'#'*completed}{'-'*missing}]{frac:.2%}",end="\r")
    
    #Respuesta
    print("\n\nLa suma de los numeros primos antes de {} es {}".format(num,sum))
    print(list)
    
    #Validacion Booleana de Repeticion de Programa
    while True:
        quest = str(input("\nDesea repetir el programa?(y/n) "))
        if quest.lower() == "n":
            rep=False
            #Final del programa
            print("\nGracias por utilizar el programa\n@josuebarrenoz en redes sociales")
            break
        elif quest.lower() == "y":
            print("")
            break
        else:
            print("Escribe una opcion valida\n")
    
