let_1 = str(input("Bienvenidos a esta Tarea de Programacion Seccion 2\n\nEscribe una frase cualquiera: "))
num_1 = len(let_1.split())

if num_1%2 == 0:
    print("\nEsta frase tiene un numero PAR de palabras\n")
elif num_1 == 1:
    print(f"\nEsta frase tiene {num_1} palabra\n")
else:
    print(f"\nEsta frase tiene {num_1} palabras\n")
    