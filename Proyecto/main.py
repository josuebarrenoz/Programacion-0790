import msg, repet
import modulo.validation as val
import modulo.crypto as cry


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
    pass

def simp_cry(palabra, *abc):
    while True:
        opcion=input("¿Quieres encriptar con Cesar ó Primos?\n\n1. Cesar\n2. Primos")


def menu_cry():
    palabra = input("\nEscribe una palabra a cifrar/descifrar: ")
    while True:
        opcion=input("¿Quieres encriptar bajo un archivo Json? (s/n)")
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
            break
        elif opcion=="2":
            menu_cry()
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


