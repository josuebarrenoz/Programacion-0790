# mooulo que ayuda a repetir el programa
def ition(func,frase1="\nRepetimos el programa? (y/n): ",frase2="\nGracias por usar el programa"):
    while True:
        rep = input(frase1)
        if rep.lower() == "y":
            func()
        elif rep.lower()=="n":
            print(frase2)
            break
        else:
            print("\nEscriba un valor valido")

if __name__=="__main__":
    print("\nEsto es un modulo del programa CRUD. Busca en la carpeta el archivo main.py y ejecutalo")