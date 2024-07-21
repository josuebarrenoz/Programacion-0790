import repet, bienve
import json

def opcion():
    while True:
        valor = input("\nQue desea modificar? \n1. nombre \n2. apellidos\n3. nota 1\n4. nota 2\n5. nota 3\n\nElige una opción: ")
        if (valor=="1" or valor=="2" or valor=="3" or valor=="4" or valor=="5"):
            break
        print("Escribe una opcion correcta")
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

def val_cel():
    while True:
        cedula = input("Escribe una cedula para buscar en la base de datos: ")
        if cedula.isnumeric():
            return cedula
            break
        else:
            print("Escibe una cedula correcta")

def run():
    with open ("alumnos.json","r") as file:
        data = json.load(file)
    file.close()

    cedula = val_cel()
    index = -1
    existe = False
    for alumno in data["data"]:
        if alumno["cedula"]==cedula:
            existe = True
            index=data["data"].index(alumno)
            print("cedula: ",alumno["cedula"])
            print("nombre: ",alumno["nombre"])
            print("apellido: ",alumno["apellido"])
            print("nota1: ",alumno["nota1"])
            print("nota2: ",alumno["nota2"])
            print("nota3: ",alumno["nota3"])
    if not existe:
        print("No existe")
    if not index==-1:
        if modificacion():
            numero = opcion()
            if numero =="1":
                nuevo_nombre=input("Coloca el nuevo nombre: ")
                data["data"][index]["nombre"] = nuevo_nombre
            elif numero =="2":
                nuevo_apellido=input("Coloca el nuevo apellido: ")
                data["data"][index]["apellido"] = nuevo_apellido
            elif numero == "3":
                nuevo_nota1=str(input("Coloca la nueva nota 1: "))
                data["data"][index]["nota1"] = nuevo_nota1
            elif numero == "4":
                nuevo_nota2=str(input("Coloca la nueva nota 2: "))
                data["data"][index]["nota2"] = nuevo_nota2
            elif numero =="5":
                nuevo_nota3=str(input("Coloca la nueva nota 3: "))
                data["data"][index]["nota3"] = nuevo_nota3

    file = open("alumnos.json" ,"w")
    json.dump(data, file)
    file.close()


if __name__=="__main__":

    bienve.nida(7)
    run()
    repet.ition(run)
