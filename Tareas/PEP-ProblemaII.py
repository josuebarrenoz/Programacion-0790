"""
  Simula el movimiento del caracol en un pozo y calcula los días que tarda en salir.

  Parámetros:
    h: Profundidad del pozo en metros (float).
    ld: Distancia ascendida por el caracol durante el día en metros (float).
    ln: Distancia que resbala el caracol durante la noche en metros (float).

  Retorno:
    Días que tarda el caracol en salir del pozo (int) o -1 si no logra salir.
"""
while True:
    h = input("Ingrese la profundidad del pozo en metros: ")
    if h.isnumeric() == True:
        h = int(h)
        break
    else:
      print("Ingrese un valor correcto")

while True:
    ld = input("Ingrese la distancia ascendida por el caracol durante el día en metros: ")
    if ld.isnumeric() == True:
        ld = int(ld)
        break
    else:
      print("Ingrese un valor correcto")

while True:
    ln = input("Ingrese la distancia que resbala el caracol durante la noche en metros: ")
    if ln.isnumeric() == True:
        ln = int(ln)
        break
    else:
      print("Ingrese un valor correcto")

Sal=True
dias = 1
altura = 0


while altura < h:
  altura += ld
  if altura > h:
    break
  altura = altura - ln
  dias += 1
  if altura < 0:
    Sal = False
    break


if Sal == True:
  print(f"El caracol sale del pozo en {dias} días.")
else:
  print("El caracol no logra salir del pozo.")
