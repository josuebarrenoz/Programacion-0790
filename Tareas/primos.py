a=1
while a>=1:
  print("Tarea de Numeros Primos con ciclos for y while\n")

  while True:
    try:
      num = int(input("Escribe hasta que numero quieres revisar cuales son primos: "))
      break
    except ValueError:
      print("\nNo has escrito un numero, sigue intentando\n")

  for i in range(2,num+1):
      cont = 0
      for j in range(1,i):
        if i%j == 0:
          cont += 1
      if cont < 2:
        print(i,end=" ")


  while True:
    rep = str(input("\nDesea repetir el programa?(y/n) "))

    if rep.lower() == "n":
      a=0
      print("\nGracias por utilizar el programa\n@josuebarrenoz en redes sociales")
      break
    elif rep.lower() == "y":
      break
    else:
      print("Escribe una opcion valida\n")
