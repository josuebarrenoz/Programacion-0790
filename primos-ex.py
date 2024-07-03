num = int(input("Escribe un numero: "))

es_primo= True

for n in range(2,num):
    if num%n==0:
        es_primo=False
        break
print("El numero: {}\n primo {} ".format(n,es_primo))