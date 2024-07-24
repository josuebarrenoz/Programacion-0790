def cesar(palabra,numero,clave=0,abc="abcdefghijklmnopqrstuvwxyz"):
    abc2="abcdefghijklmnopqrstuvwxyz"
    sym=""
    cifrado=""
    if abc!="abcdefghijklmnopqrstuvwxyz":
        for i in abc:
            if i not in abc2:
                sym+=i
    if  abc!="abcdefghijklmnopqrstuvwxyz" and numero==1:
        abc2="abcdefghijklmnopqrstuvwxyz"+sym
    if abc!="abcdefghijklmnopqrstuvwxyz" and numero==2:
        abc2=abc
        abc="abcdefghijklmnopqrstuvwxyz"+sym
    for i in range (len(palabra)):
        try:
            cifrado+=abc2[(abc.index(palabra[i])+(((-1)**numero)*(clave)))%len(abc)]
        except ValueError:
            cifrado+=palabra[i]
        except IndexError:
            pass
    return cifrado

def primos(palabra,numero,abc="abcdefghijklmnopqrstuvwxyz"):
    palabra+=" "
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

    cifrado=""
    if numero == 1:
        return cod_primos(palabra,abc,primos,cifrado)
    else:
        return descod_primos(palabra,abc,primos,cifrado)

def cod_primos(palabra,abc,primos,cifrado):
    for i in range (len(palabra)):
        try:
            cifrado+=str(primos[abc.index(palabra[i])])
            try:
                if not(isinstance((abc.index(palabra[(i+1)%(len(palabra))])),str)):
                    cifrado=cifrado+"-"
            except ValueError:
                pass
        except ValueError:
            cifrado+=palabra[i]
    return cifrado

def descod_primos(palabra,abc,primos,cifrado):
    palabra_list=[]
    aux=""
    for i in range(len(palabra)):
        if not palabra[i].isnumeric():
            palabra_list.append(aux)
            palabra_list.append(palabra[i])
            aux=""
        else:
            aux+=palabra[i]
    for i in range(len(palabra_list)):
        if  not palabra_list[i]=="-":
            try:
                cifrado+=str(abc[primos.index(int(palabra_list[i]))])
            except ValueError:
                cifrado+=str(palabra_list[i])
    return cifrado

def abc_random(sym=""):
    import random
    abc="abcdefghijklmnopqrstuvwxyz"
    abc_list=[]
    abcr=""
    list=[]
    for i in sym:
        if i not in list:
            list.append(i)
    for i in range(len(list)):
        abc+=list[i]
    abc_list = random.sample(abc,len(abc))
    for i in range(len(abc_list)):
        abcr+=str(abc_list[i])
    return abcr

# def base():
#    pass

if __name__=="__main__":
    def cifrado():
        palabra = input("\nEscribe una palabra a cifrar/descifrar: ")
        palabra = palabra.lower()

        while True:
            try:
                clave = int(input("\nEscribe la clave de cifrado: "))
                break
            except ValueError:
                print("\nEscribe un Numero Entero")
        abc="e'¿i=p$hÇbo&:`tkdcl¡;qm?jau*^wz.sy,v¨xfn/rg+-_!"
        while True:
            quest=input("\nDescifrar o cifrar? \n\n Opciones: \n\n1. Cifrar \n2.Descifrar\nOpcion: ")
            if quest=="1":
                print(f"\nLa palabra cifrada es {primos(palabra,1,abc)}")
                break
            if quest =="2":
                print(f"\nLa palabra descifrada es {primos(palabra,2,abc)}")
                break
            print("Escribe una opcion valida")
    cifrado()
    #print(abc_random("!$%&/=?¿¡'^*+`¨Ç_.,;:-+*/"))
