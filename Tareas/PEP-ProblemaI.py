"""
Función para generar números aleatorios con la técnica del cuadrado medio.
"""
cont=0
while True:
    ent = input("Ingrese un número de al menos 4 dígitos: ")
    if ent.isnumeric()== True:
        semilla = int(ent)
        if len(str(semilla)) >= 4:
            aleatorio = []
            n=[]
            n2=[]
            for _ in range(10):
                cuadrado = semilla * semilla
                str_cuadrado = str(cuadrado)
                #Se agrega la semilla como el cuadrado
                n.append(semilla)
                n2.append(cuadrado)
                # Si el cuadrado tiene menos de 2N digitos, se rellena con cero a la izquierda
                if len(str_cuadrado) < 2 * len(str(semilla)):
                    str_cuadrado = "0" * (2 * len(str(semilla)) - len(str_cuadrado)) + str_cuadrado
                # Se extraen los N digitos del medio
                medio = int(str_cuadrado[len(str(semilla))-2:len(str(semilla))+2])
                #Se agrega al numero aleatorio
                aleatorio.append(cuadrado/10**len(str(cuadrado)))
                semilla = medio
            print("Números aleatorios generados:")
            print("  N  |    N^2   | Aleatorio|")
            print("____________________________")
            for i,j,k in zip(n,n2,aleatorio):
                print(i,"|",j,"|",k)
            print("____________________________")
            break
        else:
            print("Error: El número debe tener al menos 4 dígitos.")
            cont=cont+1
    else:
        print("Error: No es un numero valido")
        cont=cont+1
    print(f"Reintento numero {cont}")
