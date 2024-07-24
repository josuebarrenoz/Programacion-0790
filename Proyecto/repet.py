def ition(func,frase1="Repetimos el programa? (y/n): ",frase2="Gracias por usar el programa"):
    while True:
        rep = input(frase1)
        if rep.lower() == "y":
            func()
        elif rep.lower()=="n":
            print(frase2)
            break
        else:
            print("Escriba un valor valido")




def prueba():
    print("hola mundo")
    print(2+2)


if __name__=="__main__":

    prueba()
    ition(prueba)