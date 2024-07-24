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
    arg1=input("Escribe ")
    arg2=listortuple(list[int(opcion)-1])
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

def menu_cry():
    pass


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


