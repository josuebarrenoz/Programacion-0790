#Verificando N
while True:
    n = input("Escriba la cantidad de filas: ")
    if n.isnumeric()==True:
        n=int(n)
        if n>0:
            break
        else:
            print("Reintenta, el numero no puede ser cero ni negativo")

    else:
        print("No es numero lo que escribiste")
#Vericando M
while True:
    m = input("Escriba la cantidad de columnas: ")
    if m.isnumeric()==True:
        m=int(m)
        if m>0:
            break
        else:
            print("Reintenta, el numero no puede ser cero ni negativo")

    else:
        print("No es numero lo que escribiste")
#Verificacion de data y presentacion
print(f"\nLa matrix N x M tiene {n} filas y {m} columnas\n")
#Programa en si
fila=0
valor=0
for i in range (n):
    list=[]
    for j in range (m):
        valor = valor +1
        list.append(valor)
    if fila%2==0:
        print(list)
    else:
        list = list[::-1]
        print(list)
    fila = fila +1
