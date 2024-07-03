while True:
    palabra=input("Escribe una palabra: ")
    if palabra.isnumeric() == False:
        palara_invertida == palabra[::-1]
        if palabra == palabra_invertida:
            print("Es palindromo")
            break
        else:
            print("No es palindromo")
    else:
        print("Escribe una opcion valida")
