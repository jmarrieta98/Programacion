import random


def mostrar_personaje(usuario):
    user = open('Examenes/Examen Marzo/Parte2-1/'+usuario, 'r')
    lista = []
    lineas = [x for x in user]
    for i in range(0, len(lineas), 2):
        diccionario = {}
        diccionario[lineas[i][:-1]] = lineas[i+1][:-1]
        lista.append(diccionario)
    user.close()
    for personaje in lista:
        print(personaje)
    return lista


with open("Examenes\Examen Marzo\Parte2-1\\brawlers", "r") as brawl:
    lista = []
    lineas = [x for x in brawl]
    for i in range(0, len(lineas), 2):
        diccionario = {}
        diccionario[lineas[i][:-1]] = lineas[i+1][:-1]
        lista.append(diccionario)

try:
    usuario = input("Introduce tu usuario:\t")
    user = open('Examenes/Examen Marzo/Parte2-1/'+usuario, 'r')
except FileNotFoundError:
    print(f"Bienvenido {usuario}")
else:
    lista_p = mostrar_personaje(usuario)
    for personaje in lista:
        if personaje in lista_p:
            lista.remove(personaje)

user = open('Examenes/Examen Marzo/Parte2-1/'+usuario, 'a+')
while True:
    opcion = input("Introduce una opción:\t")
    opcion = opcion.split(" ")
    if opcion[-1].lower() == 'fin':
        user.close()
        break
    elif opcion[-1].lower() == "simular":
        print("Simulando ...")
        cajasG = 0
        try:
            cajasD = int(opcion[0])
        except ValueError:
            print("Error al introducir los dias")
        if cajasD % 2.5 == 2:
            cajasG = int(2*((cajasD//2.5)+1))
        elif int(opcion[0]) % 2.5 == 0:
            cajasG = int(2*(cajasD//2.5))
        for i in range(0, cajasD+cajasG):
            numero = random.randint(0, len(lista)-1)
            personaje = lista[numero]
            lista.remove(personaje)
            print(str(personaje))
            user.write("".join(personaje.keys())+"\n" +
                       "".join(personaje.values())+"\n")
    else:
        print("No ha introducido ningun comando valido")
