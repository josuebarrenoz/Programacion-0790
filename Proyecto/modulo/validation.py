def valInt(arg1,arg2=True):
    if not isinstance(arg1,int):
        return False
    if arg2==True:
        return True
    if not (isinstance(arg2,list) or isinstance(arg2,tuple)):
        raise TypeError
    if len(arg2)!=2:
        return False
    if not (isinstance(arg2[0],int) and isinstance(arg2[1],int)):
        return False
    if arg2[1]<arg2[0]:
        raise ValueError
    if (arg1<arg2[0] or arg1>arg2[1]):
        return False
    if (arg2[0] or arg2[1])==arg1 and isinstance(arg2,tuple):
        return False
    return True

def valFloat(arg1,arg2=True):
    if not isinstance(arg1,float):
        return False
    if arg2==True:
        return True
    if not (isinstance(arg2,list) or isinstance(arg2,tuple)):
        raise TypeError
    if len(arg2)!=2:
        return False
    if not (isinstance(arg2[0],(int,float)) and isinstance(arg2[1],(int,float))):
        return False
    if float(arg2[1])<float(arg2[0]):
        raise ValueError
    if (arg1<float(arg2[0]) or arg1>float(arg2[1])):
        return False
    if (float(arg2[0]) or float(arg2[1]))==arg1 and isinstance(arg2,tuple):
        return 6
    return False

def valComplex(arg1,arg2=True):
    pass

def valList():
    pass

if __name__=="__main__":

    #Probando el modulo ValInt
    print("Probando el modulo valInt")
    print(valInt(4))
    print(valInt(4.0))
    print(valInt(4,(4,10)))
    print(valInt(4,[3,9]))
    print(valInt(4,[4,10]))
    try:
        valInt(4,[10,4])
    except ValueError:
        print("ValueError")
    try:
        valInt(4,5)
    except TypeError:
        print("TypeError")

    print("\nProbando el modulo valFloat")

    print(valFloat(4.0))
    print(valFloat(4))
    print(valFloat(4.4,(4.4,10)))
    print(valFloat(4.4,(4,10)))
    print(valFloat(4.1,[4.1,9.05]))
    print(valFloat(4.2,[4,10]))
    try:
        print(valFloat(4.0,[10,4]))
    except ValueError:
        print("ValueError")
    try:
        print(valFloat(4.0,5))
    except TypeError:
        print("TypeError")
