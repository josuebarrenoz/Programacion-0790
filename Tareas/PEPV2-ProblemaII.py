while True:
    numero = input("Escrie un numero: ")
    if numero.isnumeric():
        numero = int(numero)
        break
    else:
        print("\nError\n")

sum = 0

for i in range (1,numero+1):
    sum = sum + ((((-1)**(i-1))*(i**(-6))))
    # Barra para medir velocidad del codigo, apoyandose en el ciclo for.
    frac = (i)/(numero)
    completed = int(frac*30)
    missing = 30 - completed
    print(f"[{'#'*completed}{'-'*missing}]{frac:.2%}",end="\r")

pi= (30240*sum/31)**(1/6)

print(f"\nEl valor de Pi es {pi}")
