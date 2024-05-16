while True:
    try:
        num_1 = int(input("Escribe el primer numero: "))
        break
    except ValueError:
        print("\nError\n")
if num_1%2 == 0:
    print("\nEste numero es par\n")
else:
    print("\nEste numero es impar\n")