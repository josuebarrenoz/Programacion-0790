#1
'''
numeros = [1,2,3,4,5,6]
for numero in numeros:
    print(numero)
'''
#2
'''
for numero in [1,2,3,4,5,6]:
    if numero %2==0:
        print(numero, end =" ")
        print("numero par")
'''
#3
'''
for numero in [1,2,3,4,5,6]:
    if numero %2==0:
        print(numero,"","numero par")
'''
#4
'''
print(list(range(0,21)))
'''
#5
'''
print(list(range(21))) 
'''
#6    
'''
for i in range(1000):
    if i %2 == 0:
        print(i)
'''
#7
''' 
acumulador =[]
for numero in range (1001):
    if numero%7 == 0:
        acumulador.append(numero)
print(sum(acumulador))
'''
#8 
acumulador = 0
for numero in range (1001):
    if numero%7 == 0:
        acumulador += numero  
print(acumulador)      