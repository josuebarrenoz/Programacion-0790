def ition(func):
    while True:
        rep = input("Repetimos el programa? (y/n): ")
        if rep.lower() == "y":
            func()
        elif rep.lower()=="n":
            print("Gracias por usar el programa")
            break
        else:
            print("Escriba un valor valido")


def prueba():
    print("hola mundo")
    print(2+2)


if __name__=="__main__":

    prueba()
    ition(prueba)