import random

# Guardar cartas en diccionario


def guardar_cartas():
    with open("Examenes\Examen Marzo\Parte2-1\\brawlers", "r") as brawl:
        lineas = [x for x in brawl]
        cartas = {}
        cartas['especial'] = []
        cartas['superespecial'] = []
        cartas['epico'] = []
        cartas['mitico'] = []
        cartas['legendario'] = []
        for i in range(0, len(lineas), 2):
            cartas[lineas[i][:-1]].append(lineas[i+1][:-1])
    return cartas

# Guardar cartas del usuario en diccionario y eliminar del diccionario genereal las cartas que ya tenga el usuario


def guardar_usuario(cartas, usuario):
    with open("Examenes\Examen Marzo\Parte2-1\\"+usuario, "r+") as user:
        lineas = [x for x in user]
        cartas_u = {}
        cartas_u['especial'] = []
        cartas_u['superespecial'] = []
        cartas_u['epico'] = []
        cartas_u['mitico'] = []
        cartas_u['legendario'] = []
        for i in range(0, len(lineas), 2):
            cartas_u[lineas[i][:-1]].append(lineas[i+1][:-1])
        for tipo, personajes in cartas_u.items():
            if personajes:
                for personaje in personajes:
                    cartas.get(tipo).remove(personaje)
    user.close()
    return cartas, cartas_u

# Muestra las cartas que tiene el usuario


def mostrar_usuario(cartas_u):
    for tipo, personajes in cartas_u.items():
        for personaje in personajes:
            print(f"{tipo}: {personaje}")

# Saca la carta aleaoriamente con probabilidad y lo guarda en el archivo


def sacar_cartas(cartas, cartas_u, user, dias, simulacion):

    with open("Examenes\Examen Marzo\Parte2-1\\"+usuario, "a+") as user:
        cajasG = 0

        try:
            d_cajaG = int(dias % 2.5)
            dias += int(simulacion)
            cajasD = int(simulacion)
        except ValueError:
            print("Error al introducir los dias")
        else:
            if (cajasD+d_cajaG) % 2.5 == 2:
                cajasG = int(2*(((cajasD+d_cajaG)//2.5)+1))
            else:
                cajasG = int(2*((cajasD+d_cajaG)//2.5))
            for i in range(0, cajasD+cajasG):
                tipo = "".join(random.choices(
                    list(cartas.keys()), weights=[0.4, 0.3, 0.2, 0.09, 0.01]))
                numero = random.randint(0, len(list(cartas.get(tipo)))-1)
                personaje = cartas.get(tipo)[numero]
                user.write(tipo+"\n" + personaje+"\n")
                print(f"{tipo}: {personaje}")
                cartas_u[tipo].append(personaje)
                cartas[tipo].pop(numero)
    return cartas, cartas_u, dias


# ---------------------------------------------------------------------------
#        r="".join(random.choices(list(cartas_u.keys()), weights=[0.4,0.3,0.2,0.09,0.01]))
if __name__ == "__main__":
    cartas = guardar_cartas()
    try:
        usuario = input("Introduce tu usuario:\t")
        user = open('Examenes/Examen Marzo/Parte2-1/'+usuario, 'r')
    except FileNotFoundError:
        print(f"Bienvenido {usuario}")
        cartas_u = {}
        cartas_u['especial'] = []
        cartas_u['superespecial'] = []
        cartas_u['epico'] = []
        cartas_u['mitico'] = []
        cartas_u['legendario'] = []
    else:
        cartas, cartas_u = guardar_usuario(cartas, usuario)
        mostrar_usuario(cartas_u)
#cartas, cartas_u = sacar_cartas()
    dias = 0
    while True:
        opcion = input("Introduce una opción:\t")
        opcion = opcion.split(" ")
        if opcion[-1].lower() == 'fin':
            break
        elif opcion[-1].lower() == "simular":
            print("Simulando ...")
            cartas, cartas_u, dias = sacar_cartas(
                cartas, cartas_u, usuario, dias, opcion[0])
        else:
            print("No ha introducido ningun comando valido")
