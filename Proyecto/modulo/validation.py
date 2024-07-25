def valInt(arg1,arg2=True):
    if not isinstance(arg1,int):
        return False
    if arg2==True:
        return True
    if not (isinstance(arg2,list) or isinstance(arg2,tuple)):
        raise TypeError
    if len(arg2)!=2:
        return False
    if not (isinstance(arg2[0],(int,float)) and isinstance(arg2[1],(int,float))):
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
        return False
    return True

def valComplex(arg1,arg2=True):
    if not isinstance(arg1,complex):
        return False
    if arg2==True:
        return True
    modulo=((arg1.real * arg1.real)+(arg1.imag *arg1.imag))**(0.5)
    if not modulo:
        return False
    if not (isinstance(arg2,list) or isinstance(arg2,tuple)):
        raise TypeError
    if len(arg2)!=2:
        return False
    if not (isinstance(arg2[0],(int,float)) and isinstance(arg2[1],(int,float))):
        return False
    if float(arg2[1])<float(arg2[0]):
        raise ValueError
    if (modulo<float(arg2[0]) or modulo>float(arg2[1])):
        return False
    if (float(arg2[0]) or float(arg2[1]))==modulo and isinstance(arg2,tuple):
        return False
    return True

def valList(arg1,arg2=True,arg3=True):
    if not isinstance(arg1,list):
        return True
    if (arg2==True and arg3==True):
        return False
    if not ((isinstance(arg2,int)and isinstance(arg3,str)) or (isinstance(arg2,list) and isinstance(arg3,str)) or arg3==True):
        raise TypeError
    if not (arg3=="value" or arg3=="len"):
        raise ValueError
    if (arg3=="len" and isinstance(arg2,int) and len(arg1)==arg2):
        return True
    if not((arg3=="len" and isinstance(arg2,int) and len(arg1)==arg2) or arg3=="value"):
        return False
    if not isinstance(arg2, list):
        return False
    try:
        for i in range(len(arg1)):
            arg2.index(arg1[i])
    except ValueError:
        return False
    return True

if __name__=="__main__":

    #Probando el modulo ValInt
    print("Probando el modulo valInt")
    print("1 ",valInt(4))
    print("2 ",valInt(4.0))
    print("3 ",valInt(4,(4,10)))
    print("4 ",valInt(4,[3,9]))
    print("5 ",valInt(4,[4,10]))
    try:
        valInt(4,[10,4])
    except ValueError:
        print("ValueError")
    try:
        valInt(4,5)
    except TypeError:
        print("TypeError")

    #Probando el modulo valFloat
    print("\nProbando el modulo valFloat")
    print("1 ",valFloat(4.0))
    print("2 ",valFloat(4))
    print("3 ",valFloat(4.4,(4.4,10)))
    print("4 ",valFloat(4.4,(4,10)))
    print("5 ",valFloat(4.1,[4.1,9.05]))
    print("6 ",valFloat(4.2,[4,10]))
    try:
        print(valFloat(4.0,[10,4]))
    except ValueError:
        print("ValueError")
    try:
        print(valFloat(4.0,5))
    except TypeError:
        print("TypeError")


    #Probando el modulo valComplex
    print("\nProbando el modulo valComplex")
    print("1 ",valComplex(3+4j))
    print("2 ",valComplex(4.0))
    print("3 ",valComplex(3+4j,(5,10)))
    print("4 ",valComplex(3+4j,[5,10]))
    print("5 ",valComplex(3+4j,[4,10]))
    try:
        print(valComplex(3+4j,[10,4]))
    except ValueError:
        print("ValueError")
    try:
        print(valComplex(3+4j,5))
    except TypeError:
        print("TypeError")

    #Probando el modulo valList
    print("\nProbando el modulo valList")
    print("1 ",valList(3+4j))
    print("2 ",valList([1,2]))
    try:
        print(valList([1,2],2))
    except ValueError:
        print("ValueError")
    print("3 ",valList([1,2],2,"len"))
    print("4 ",valList([1,2],3,"len"))
    print("5 ",valList([1,2],[2],"len"))
    print("6 ",valList([1,2],2,"value"))
    print("7 ",valList([1,2],[2],"value"))
    print("8 ",valList([1,2],[2,3],"value"))
    print("9 ",valList([1,2],[2,1],"value"))
    try:
        print(valList([1,2],[10,4],3))
    except TypeError:
        print("TypeError")
    try:
        print(valList([1,2],3,[10]))
    except TypeError:
        print("TypeError")
    try:
        print(valList([1,2],[10,4],"palabra"))
    except ValueError:
        print("ValueError")
