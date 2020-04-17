import pymysql
from clase8 import *


def comprobrartelefono(tel):
    if tel[0] == '+':
        telefono = tel[1:-1]
    try:
        telefono = int(telefono)
    except ValueError:
        return False
    else:
        return True


def comprobarnombre(texto):
    if len(opcion) == 1:
        while True:
            nombre = input("Introduzca el nombre del contacto: \t")
            if nombre:
                break
        return nombre
    else:
        texto.pop(0)
        nombre = " ".join(texto)
        return nombre


if __name__ == "__main__":
    agenda = Agenda()
    print(agenda)
    while True:
        opcion = input("Introduzca una opcion: ")
        opcion = opcion.split()  # me lo transforma en lista

        if opcion[0].lower() == "consulta":
            nombre = comprobarnombre(opcion)
            print(agenda.consulta(nombre))  # terminar elif (completarlas)

        elif opcion[0].lower() == "alta":
            nombre = comprobarnombre(opcion)
            telefono = input("Introduzca el teléfono: \t")
            if comprobrartelefono(telefono):
                print(agenda.alta(nombre, telefono))
            else:
                print("Telefono no valido")

        elif opcion[0].lower() == "borra":
            nombre = comprobarnombre(opcion)
            print(agenda.borrar(nombre))

        elif opcion[0].lower() == "modifica":
            nombre = comprobarnombre(opcion)
            telefono = input("Introduzca el teléfono: \t")
            if comprobrartelefono(telefono):
                print(agenda.modificar(nombre, telefono))
            else:
                print("Telefono no valido")

        elif opcion[0].lower() == "fin":
            print("Saliendo del programa")
            break

        elif opcion[0].lower() == "mostrar":
            agenda.mostrar()

        else:
            print("Comando no existente")
