abc="abcdefghijklmnopqrstuvwxyz"
primos=[]
index = 0
num=2

while index < (len(abc)):
    cont=0
    for i in range (2,num):
        if num%i==0:
            cont=cont+1
        if cont>1:
            break
    if cont<1:
        primos.append(num)
        index+=1
    num+=1

print(primos)

palabra = input("\nEscribe una palabra a cifrar: ")
palabra = palabra.lower()

palabra =" "+palabra+" "
cifrado=""

for i in range (len(palabra)):
    if palabra[i]==" ":
        cifrado=cifrado+" "
    elif palabra[i]==",":
        cifrado=cifrado+","
    else:
        cifrado=cifrado+str(primos[abc.index(palabra[i])])
        if palabra[i]==" ":
            pass
        if palabra[(i+1)%len(palabra)]==" ":
            pass
        else:
            cifrado=cifrado+"-"


print(cifrado)

