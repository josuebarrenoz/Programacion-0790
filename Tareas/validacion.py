def val_list(arg1,arg2):
    if not isinstance(arg1,list):
        return False
    if not isinstance(arg2,tuple):
        return False
    for i in range (len(arg2)):
        try:
            arg1.index(arg2[i])
        except ValueError:
           return False
    return True

def val_int(arg1,arg2):
    if not isinstance(arg1,int):
        return False
    if not (isinstance(arg2,list) or isinstance(arg2,tuple)):
        return False
    if len(arg2)!=2:
        return False
    if not (isinstance(arg2[0],int) and isinstance(arg2[1],int)):
        return False
    if arg2[1]<arg2[0]:
        return False
    if (arg1<arg2[0] or arg1>arg2[1]):
        return False
    if (arg2[0] or arg2[1])==arg1 and isinstance(arg2,tuple):
        return False
    return True

if __name__=="__main__":
    import repet

    def val(option):
        if option=="1":
            arg=input("Escribe: ")
            return arg
        elif option=="2":
            arg=int(input("Escribe: "))
            return arg
        elif option=="3":
            arg=[]
            while True:
                element=int(input("Escribe: "))
                arg.append(element)
                preg=input("otro elemento (_/n)")
                if preg.lower()=="n":
                    break
            return arg
        elif option=="4":
            arg=()
            while True:
                element=int(input("Escribe: "))
                arg.append(element)
                preg=input("otro elemento (_/n)")
                if preg.lower()=="n":
                    break
            return arg

    def option(num):
        while True:
            option=input("Escribe una opcion para arg{num} (1.str 2.int 3. list 4. tupla): ")
            if not option == ("1"or"2"or"3"or"4"):
                print("Opcion Invalida")
            else:
                break
        return option

    def prueba():
        num=option(1)
        arg1=val(num)
        num=option(2)
        arg2=val(num)

        if val_int(arg1,arg2) == True:
            print("Exito")
        else:
            print("Falla")

    prueba()
    repet.ition(prueba)
