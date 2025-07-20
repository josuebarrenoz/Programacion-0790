import msg, repet
import modulo.validation as val
import modulo.crypto as cry
import json


def listortuple(palabra):
    while True:
        opcion=input(f"\nEl rango a evaluar del numero {palabra} es una:\n\n1.Lista\n2.Tupla\n\nEscribe la opcion: ")
        if opcion=="1":
            arg1=float(input("\nEscribe el primer valor: "))
            arg2=float(input("\nEscribe el segundo valor: "))
            return [arg1,arg2]
        elif opcion=="2":
            arg1=float(input("\nscribe el primer valor: "))
            arg2=float(input("\nEscribe el segundo valor: "))
            return (arg1,arg2)
        else:
            print("\nEscribe una opcion valida")

def submenu_val1(opcion):
    list=["entero","flotante","complejo"]
    palabra=list[int(opcion)-1]
    arg1=input("\nEscribe el numero: ")
    arg2=listortuple(palabra)
    if opcion=="1":
        try:
            arg1=int(arg1)
            print(val.valInt(arg1,arg2))
        except ValueError:
            print(False)
    elif opcion=="2":
        try:
            arg1=float(arg1)
            print(val.valFloat(arg1,arg2))
        except ValueError:
            print(False)
    elif opcion=="3":
        try:
            arg1=complex(arg1)
            print(val.valComplex(arg1,arg2))
        except ValueError:
            print(False)

def list_generic():
    print("\nConstruye la lista...")
    list=[]
    while True:
        try:
            num=input("\nEscribe un numero: ")
            list.append(float(num))
        except ValueError:
            print("\nError de Valor, Escribe un numero")
        if input("\nDesea agregar mas numeros? (y/): ").lower()!="y":
            break
    return list

def submenu_val2():
    arg1=list_generic()
    while True:
        opcion=input("¿Que deseas evaluar en la lista?\n\n1. Longitud\n2. Valor\n\nEscribe una opcion: ")
        if opcion=="1":
            arg3="len"
            break
        if opcion=="2":
            arg3="value"
            break
        print("\nEscribe una opcion valida")
    if arg3=="len":
        while True:
            try:
                arg2=int(input("\nEscribe la longitud: "))
                print(val.valList(arg1,arg2,arg3))
                break
            except ValueError:
                print("\nEscribe un numero entero")
    if arg3=="value":
        arg2=list_generic()
        print(val.valList(arg1,arg2,arg3))
    
def menu_val():
    while True:
        opcion=input("\n¿Que desea validar?\n\n1.Entero\n2.Flotante\n3.Complejo\n4.Lista\n\nEscribe la opcion: ")
        if opcion=="1" or opcion=="2" or opcion=="3":
            submenu_val1(opcion)
            break
        elif opcion=="4":
            submenu_val2()
            break
        else:
            print("\nEscribe una opcion valida")

def json_cry(palabra):
    try:
        with open ("cifrados.json","r") as file:
            data = json.load(file)
        file.close()
    except FileNotFoundError:
        print("\nNo existe ningun archivo Json con clave. ")
        with open ("cifrados.json","w") as file:
            data = {}
        file.close()
        print("\nArchivo creado automaticamente")
    if data=={}:
        sym=str(input("Escribas los simbolos que desea poner en su clave(Presionar enter es valido): "))
        abc = str(cry.abc_random(sym))
        data={"abecedario":abc}
        data2=data
        with open ("cifrados.json","w") as file:
            data2 = json.dump(data,file)
        file.close()
    if data["abecedario"]=="":
        print("\nNo tiene clave generada. Generando una...")
        sym=str(input("Escribas los simbolos que desea poner en su clave(Presionar enter es valido): "))
        abc = str(cry.abc_random(sym))
        data["abecedario"]=abc
        data2=data
        with open ("cifrados.json","w") as file:
            data2 = json.dump(data,file)
        file.close()
    simp_cry(palabra, data["abecedario"])

def primos_simp_cry(palabra, *abc):
        while True:
            quest=input("\nDescifrar o cifrar? \n\nOpciones: \n\n1. Cifrar \n2.Descifrar\n\nOpcion: ")
            if quest=="1":
                print(f"\nLa palabra cifrada es {cry.primos(palabra,1,*abc)}")
                break
            if quest =="2":
                print(f"\nLa palabra descifrada es {cry.primos(palabra,2,*abc)}")
                break
            print("\nEscribe una opcion valida")

def cesar_simp_cry(palabra, *abc):
    while True:
        try:
            clave = int(input("\nEscribe la clave de cifrado: "))
            break
        except ValueError:
            print("\nEscribe un Numero Entero")
    while True:
        quest=input("\nDescifrar o cifrar? \n\nOpciones: \n\n1. Cifrar \n2.Descifrar\n\nOpcion: ")
        if quest=="1":
            print(f"\nLa palabra cifrada es {cry.cesar(palabra,1,clave,*abc)}")
            break
        if quest =="2":
            print(f"\nLa palabra descifrada es {cry.cesar(palabra,2,clave,*abc)}")
            break
        print("\nEscribe una opcion valida")

def simp_cry(palabra, *abc):
    while True:
        opcion=input("¿Quieres encriptar con Cesar ó Primos?\n\n1. Cesar\n2. Primos\n\nEscribe una opcion: ")
        if opcion=="1":
            cesar_simp_cry(palabra,*abc)
            break
        if opcion=="2":
            primos_simp_cry(palabra,*abc)
            break
        print("\nEscribe una opcion valida")

def menu_cry():
    palabra = input("\nEscribe una palabra a cifrar/descifrar: ")
    palabra=palabra.lower()
    while True:
        opcion=input("\n¿Quieres encriptar bajo un archivo Json? (s/n): ")
        if opcion.lower() == "s":
            json_cry(palabra)
            break
        elif opcion.lower()=="n":
            simp_cry(palabra)
            break
        else:
            print("Escriba un valor valido")

def menu_grande():
    while True:
        opcion = input("¿Que programa utilizaras?\n\n1.Validacion\n2.Crypto\n\nEscribe la opcion: ")
        if opcion=="1":
            menu_val()
            repet.ition(menu_val,"¿Otra Validacion? (y/n): ", "")
            break
        elif opcion=="2":
            menu_cry()
            repet.ition(menu_cry,"¿Otra frase a encriptar? (y/n): ", "")
            break
        else:
            print("\nEscribe una opcion valida")

def run():
    menu_grande()

if __name__=="__main__":
    msg.inicio()
    run()
    repet.ition(run)
    msg.final()
