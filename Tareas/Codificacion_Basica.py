
def Run():
    #variables
    base_1="0123456789abcdefghijklmnopqrstuvwxyz"
    base_2="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #Inputs
    frase = input("Escribe una frase a cifrar: ")

    list=[]
    for i in range len(frase):
        try:
            if base_1.index(frase[i]):
                list.append(frase[i])
        except ValueError:
            list.append("aqui")


if __name__=="__main__":
    Run()
