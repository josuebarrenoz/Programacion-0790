def val_list(arg1,arg2):
    if not is isinstance(arg1,list):
        return False
    if not is  isinstance(arg2,tuple):
        return False
    for i in range (len(arg2)):
        try:
            arg1.index(arg2[i])
        except ValueError:
            return False
    return True

def val_int(arg1,arg2):
    if not is isinstance(arg1,int):
        return False
    if not is (isinstance(arg2,list) or isinstance(arg2,tuple)):
        return False
    if len(arg2)!=2:
        return False
    if not is (isinstance(arg2[0],int) and isinstance(arg2[1],int)):
        return False
    if arg2[1]<arg2[0]:
        return False
    if (arg1<arg2[0] or arg1>arg2[1]):
        return False
    if (arg2[0] or arg2[1])==arg1 and isinstance(arg2,tuple):
        return False
    return True

if __name__=="__main__":
    pass
