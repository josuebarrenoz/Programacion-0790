while True:
    palabra_1=input("Escribe una palabra: ")
    if palabra_1.isnumeic()==False:
        break
    else:
        print("Escribe una opcion valida")

while True:
    palabra_2=input("Escribe una palabra: ")
    if palabra_2.isnumeic()==False:
        break
    else:
        print("Escribe una opcion valida")

cont=0
for i in range (len(palabra_1)):
    try:
        palabra_2.index(palabra_1[i])
        cont+=1
    except:
        cont-=1

if cont == len(palabra_1):
    print("Es una anagrama")
else:
    print("No es un anagrama")
