import repet, bienve
import json

def opcion():
    valor = int(input("\nQue desea modificar? \n1. nombre \n2. apellidos\n3. nota 1\n4. nota 2\n5. nota 3\n\nElige una opción: "))
    return valor


def modificacion():
    while True:
        pregunta_1 = input("\nQuieres modificar algun elemento? (y/n): ")
        if pregunta_1.lower() == "y":
            return True
            break
        elif pregunta_1.lower()=="n":
            return False
            break
        else:
            print("\nEscriba un valor valido")

def run():
    with open ("alumnos.json","r") as file:
        data = json.load(file)
    file.close()

    while True:
        cedula = input("Escribe una cedula para buscar en la base de datos: ")
        if cedula.isnumeric():
            break
        else:
            print("Escibe una cedula correcta")

    existe = False
    for alumno in data["data"]:
        if alumno["cedula"]==cedula:
            existe = True
            print("cedula: ",alumno["cedula"])
            print("nombre: ",alumno["nombre"])
            print("apellido: ",alumno["apellido"])
            print("nota1: ",alumno["nota1"])
            print("nota2: ",alumno["nota2"])
            print("nota3: ",alumno["nota3"])
            if modificacion():
                if opcion() ==1:
                    nuevo_nombre=input("Coloca el nuevo nombre: ")
                    alumno["nombre"] = nuevo_nombre
                elif opcion() ==2:
                    nuevo_apellido=input("Coloca el nuevo apellido: ")
                    alumno["apellido"] = nuevo_apellido
                elif opcion() == 3:
                    nuevo_nota1=str(input("Coloca la nueva nota 1: "))
                    alumno["nota1"] = nuevo_nota1
                elif opcion() == 4:
                    nuevo_nota2=str(input("Coloca la nueva nota 2: "))
                    alumno["nota2"] = nuevo_nota2
                elif opcion() == 5:
                    nuevo_nota3=str(input("Coloca la nueva nota 3: "))
                    alumno["nota3"] = nuevo_nota3
                else:
                    pass
    if not existe:
        print("No existe")
    file = open("alumnos.json" ,"w")
    json.dump(data, file)
    file.close()
    print(data)


if __name__=="__main__":

    bienve.nida(7)
    run()
    repet.ition(run)
