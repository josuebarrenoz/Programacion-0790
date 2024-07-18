def cesar(palabra,clave,numero):
    abc="abcdefghijklmnopqrstuvwxyz"
    cifrado=""
    for i in range (len(palabra)):
        try:
            cifrado=cifrado+abc[(abc.index(palabra[i])+(((-1)**numero)*(clave)))%len(abc)]
        except ValueError:
            cifrado=cifrado+palabra[i]

    if numero == 1:
        opcion = "Cifrada"
    else:
        opcion = "Descifrada"
    return print(f"\nLa palabra {opcion} es {cifrado}")

def cod_primos(palabra):
    abc="abcdefghijklmnopqrstuvwxyz"
    primos=[]
    cifrado=""
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

        for i in range (len(palabra)):
            try:
                cifrado=cifrado+str(primos[abc.index(palabra[i])])
            except ValueError:
                cifrado=cifrado+palabra[i]
            try:
                if not(isinstance((abc.index(palabra[(i+1)%(len(palabra))])),str)):
                    cifrado=cifrado+"-"
            except ValueError:
                pass
        return print(f"\nLa palabra cifrada es {cifrado}")

"""
def descod_primos(palabra):
    #Variables
    descifrado_list=[]
    descifrado=""


    #Validar la palabra y Agarra la palabra y ponerlo en una lista
    while True:
        cont=0
        palabra_list=[]
        palabra = input("\nEscribe una palabra a descifrar: ")
        #magic
        palabra=" "+palabra+" "

        #Enlistamiento
        for i in range (len(palabra)):
            if (palabra[i].isnumeric() and palabra[(i+1)%len(palabra)].isnumeric() and palabra[(i+2)%len(palabra)].isnumeric()):
                palabra_list.append(palabra[i]+palabra[(i+1)%len(palabra)]+palabra[(i+2)%len(palabra)])
            elif (palabra[i-1].isnumeric() and palabra[(i)%len(palabra)].isnumeric() and palabra[(i+1)%len(palabra)].isnumeric()):
                pass
            elif (palabra[i-2].isnumeric() and palabra[(i-1)%len(palabra)].isnumeric() and palabra[(i)%len(palabra)].isnumeric()):
                pass
            elif (palabra[i].isnumeric() and palabra[(i+1)%len(palabra)].isnumeric()):
                palabra_list.append(palabra[i]+palabra[(i+1)%len(palabra)])
            elif (palabra[i].isnumeric() and palabra[(i-1)%len(palabra)].isnumeric()):
                pass
            else:
                palabra_list.append(palabra[i])

            #Verificacion
            for i in range (len(palabra_list)):
                cont+=1
                if palabra_list[i].isnumeric():
                    try:
                        if primos.index(int(palabra_list[i])):
                            pass
                    except ValueError:
                        print("\nInvalido. Repite de nuevo")
                        break
                else:
                    try:
                        if abc.index(palabra_list[i]):
                            print("\nInvalido. Repite de nuevo")
                            break
                    except ValueError:
                        pass

            #salida
            if cont == len(palabra_list):
                break

        #Buscando el indice y cambiarlo por letras
        for i in range (len(palabra_list)):
            try:
                if palabra_list[i].isnumeric():
                    descifrado_list.append(abc[primos.index(int(palabra_list[i]))])
                else:
                    descifrado_list.append(palabra_list[i])
            except ValueError:
                descifrado_list.append(palabra_list[i])

        #Convertir una lista en un string
        for i in range(len(palabra_list)):
            if palabra_list[i]!="-":
                descifrado= descifrado + descifrado_list[i]

        #Impresion final
        print(f"\nLa palabra descifrada es {descifrado}")
"""
def base():
    pass

if __name__=="__main__":
    """
    palabra = input("\nEscribe una palabra a cifrar: ")
    palabra = palabra.lower()
    while True:
        try:
            clave = int(input("\nEscribe la clave de cifrado: "))
            break
        except ValueError:
            print("\nEscribe un Numero Entero")
    cesar(palabra,clave,0)
    """
    pass
