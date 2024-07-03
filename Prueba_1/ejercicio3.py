abc= "abcdefghijklmnopqrstuvwxyz"
primos=[]
num=2

while len(primos)!=len(abc):
    cont=0
    for j in range (1,num):
        if num%j==0:
            cont+=1
        if cont > 1:
            break

    if cont==1:
        primos.append(num)
    num+=1

while True:
    opcion=input("Elige una opcio:\n\n1. Codificarun mensaje\n2. Decodificar un mensaje\n3. Contar frecue...\n\n...:  ")
    if opcion.isnumeric()==True:
        opcion=int(opcion)
        if opcion==1:
            while True:
                palabra=input("Ingrese el mensaje a codificar: ")
                if palabra.isnumeric()==False:
                    break
                else:
                    print("Escribe una palabra valida")
            cifrado=""
            palabra=palabra.lower()
            for i in range (len(palabra)):
                cifrado+=str(primos[abc.index(palabra[i])])
            print(f"\nEl mensaje codificado es:{cifrado}")
        elif opcion==2:
            pass
        elif opcion==3:
            pass
        elif opcion==4:
            print("Gracias por usar el programa")
            break
        else:
            print("Escribe una opcion valida")
    else:
        print("Escribe una opcion valida")
