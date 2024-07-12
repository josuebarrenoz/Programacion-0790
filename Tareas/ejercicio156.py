import repet

def respuesta_156(n,x):
    str="123456789"
    resultado=""
    num = str.index(x)
    max = int(n)

    for j in range (2,int(n)+2):
        num_i=num
        for i in range(1,max+1):
            resultado+=str[num_i]+" "
            num_i = (num_i + i)%len(str)
        num = (num+j)%len(str)
        resultado+="\n"
        max-=1

    return resultado


def verificacion(num):
    if num.isnumeric() == False:
        return False
    elif int(num)<=0:
        return False
    else:
        return True

def run():
    while True:
        n=input("\nAgregue el valor n: ")
        ver=verificacion(n)
        if ver == True:
            break
        else:
            print("\nInvalido. Repite")

    while True:
        x=input("\nAgregue el valor x: ")
        ver=verificacion(x)
        if ver == True:
            break
        else:
            print("\nInvalido. Repite")

    resultado = respuesta_156(n,x)
    print(f"El resultado es:\n\n{resultado}")

if __name__=="__main__":
    run()
    repet.ition(run)