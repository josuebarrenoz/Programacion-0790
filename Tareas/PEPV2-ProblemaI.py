
while True:
    porcentaje = input("Escrie un numero: ")
    if porcentaje.isnumeric():
        porcentaje = int(porcentaje)
        break
    else:
        print("\nError\n")

cont1=0
cont2=0

for i in range(1,porcentaje+1):

#Establecer el primer numero como lista
    list = []
    num = i
    while True:
        list.append(num%10)
        num = num//10
        if num == 0:
            break
    list = list[::-1]
    #print(f"numero principal {list}")

#Revisar la cadena de numeros del primer numero
    sum=0
    while True:
        for k in list:
            sum = sum + (k*k)
        if sum ==1:
            cont1=cont1+1
            break
        elif sum == 89:
            cont2=cont2+1
            break
        else:
            list=[]
            while True:
                list.append(sum%10)
                sum = sum//10
                if sum == 0:
                    break
            list = list[::-1]
            #print(list)

        # Barra para medir velocidad del codigo, apoyandose en el ciclo for.
        frac = (i+1)/(porcentaje)
        completed = int(frac*30)
        missing = 30 - completed
        print(f"[{'#'*completed}{'-'*missing}]{frac:.2%}",end="\r")

#print(cont1,cont2)
#Sacar porcentajes
print(f"\nEL porcentaje de numeros que terminan en 1 es {100*cont1/porcentaje} y el porcentaje de numeros que terminan en 89 es {100*cont2/porcentaje}")






