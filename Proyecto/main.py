import msg, repet
import modulo.validation as val
import modulo.crypto as cry
import json


def listortuple(palabra):
    while True:
        opcion=input("¿El rango a evaluar el {palabra} que es?\n\n1.Lista\n2.Tupla\n\nEscribe la opcion: ")
        if opcion=="1":
            return []
        elif opcion=="2":
            return ()
        else:
            print("\nEscribe una opcion valida")


def submenu_val1(opcion):
    list=["Entero","Flotante","Complejo"]
    palabra=list[int(opcion)-1]
    print(palabra)
    arg1=input("Escribe el numero: ")
    arg2=listortuple(palabra)
    if opcion=="1":
        pass


def menu_val():
    while True:
        opcion=input("¿Que desea validar?\n\n1.Entero\n2.Flotante\n3.Complejo\n4.Lista\n\nEscribe la opcion: ")
        if opcion=="1" or opcion=="2" or opcion=="3":
            submenu_val1(opcion)
            break
        elif opcion=="4":
            pass
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
        if opcion.lower() == "y":
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


