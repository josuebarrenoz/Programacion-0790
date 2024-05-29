a = 1
while a==1:
    while True:
        num = input("Escribe un numero: ")
        if num.isnumeric() == True:
            num = int(num)
            break

    sum = 0 
    list=[]
    
    for n in range (2,num+1):
        cont=0
        for i in range (1,n+1):
            if n%i==0:
                cont=cont+1
        if cont < 3:
            list=list.append(num)
            sum=sum+num
    
    print(f"Los numeros primos son {list}\n y la suma seria {sum}")
    
    validator = str ()
    if         
    