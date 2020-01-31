import os
equipos = ['CHB', 'CAW', 'CSU', 'COS', 'VIB', 'CHE']
traduccion = {
    'CHB': ['chiclana blues', 'chiclana', 'blues', 'chb'],
    'CAW': ['cádiz wheels', 'cádiz', 'wheels', 'caw'],
    'CSU': ['caleta surfers', 'caleta', 'surfers', 'csu'],
    'COS': ['conil suns', 'conil', 'suns', 'cos'],
    'VIB': ['victoria bedouins', 'victoria', 'bedouins', 'vib'],
    'CHE': ['cortadura hearts', 'cortadura', 'hearts', 'che']
}


def traducir(eq1, eq2, diccionario):
    elec = list(diccionario.items())
    for i in range(0, len(elec)):
        for j in range(0, len(elec[i][1])):
            if eq1 == elec[i][1][j]:
                eq1 = elec[i][0]
            if eq2 == elec[i][1][j]:
                eq2 = elec[i][0]
    return eq1, eq2


class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidosjugados = 0
        self.partidosganados = 0
        self.partidosperdidos = 0
        self.puntosafavor = 0
        self.puntosencontra = 0
        self.marcador = 0

    def __str__(self):
        return f'{self.nombre}\t {str(self.partidosjugados)}\t {str(self.partidosganados)}\t {str(self.partidosperdidos)}\t {str(self.puntosafavor)}\t {str(self.puntosencontra)}\t {str(self.marcador)}'


class liga:
    def __init__(self):
        self.equipos = []
        for i in equipos:
            self.equipos.append(Equipo(i))

    def mostrar(self):
        self.equipos = sorted(self.equipos, key=lambda objeto: (objeto.partidosganados, sorted(self.equipos, key=lambda objeto: objeto.partidosperdidos),
                                                                objeto.puntosafavor, sorted(self.equipos, key=lambda objeto: objeto.puntosencontra), objeto.marcador, objeto.nombre), reverse=True)
        print('Nombre\tP.J.\tP.G\tP.P\tP.A.F\tP.E.C\tMarcador')
        for i in self.equipos:
            print(i)

    def insertar(self, equipo1, equipo2, marcador1, marcador2):
        if marcador2 > marcador1:
            for i in self.equipos:
                if i.nombre == equipo2:
                    i.partidosjugados += 1
                    i.partidosganados += 1
                    i.puntosafavor += marcador2
                    i.puntosencontra += marcador1
                    i.marcador += (marcador2-marcador1)
                if i.nombre == equipo1:
                    i.partidosjugados += 1
                    i.partidosperdidos += 1
                    i.puntosafavor += marcador1
                    i.puntosencontra += marcador2
                    i.marcador += (marcador1-marcador2)
        elif marcador1 > marcador2:
            for i in self.equipos:
                if i.nombre == equipo1:
                    i.partidosjugados += 1
                    i.partidosganados += 1
                    i.puntosafavor += marcador1
                    i.puntosencontra += marcador2
                    i.marcador += 3
                if i.nombre == equipo2:
                    i.partidosjugados += 1
                    i.partidosperdidos += 1
                    i.puntosafavor += marcador2
                    i.puntosencontra += marcador1


if __name__ == "__main__":
    baloncesto = liga()
    while True:

        opcion = input("Introduzca una opcion:\t")
        opcion = opcion.split('\t')
        if len(opcion) == 2:
            equipo1 = opcion[0].split()
            equipo2 = opcion[1].split()
            try:
                if int(equipo1[-1]) >= 0 and int(equipo2[-1]) >= 0:
                    marcador1 = equipo1.pop(-1)
                    marcador2 = equipo2.pop(-1)
                    equipo1 = " ".join(equipo1)
                    equipo2 = " ".join(equipo2)
                    equipo1, equipo2 = traducir(
                        equipo1.lower(), equipo2.lower(), traduccion)
                    if marcador1 == marcador2:
                        print("Error los partidos no pueden quedar en empate")
                    else:
                        baloncesto.insertar(equipo1, equipo2, int(
                            marcador1), int(marcador2))
                else:
                    print("Los resultados no pueden ser negativos")
            except ValueError:
                print("Error, no has introducido bien los resultados")
        elif len(opcion) == 1:
            if str(opcion[0]).lower() == 'mostrar':
                os.system("cls")
                baloncesto.mostrar()
            elif str(opcion[0]).lower() == 'cls':
                os.system("cls")
            elif str(opcion[0]).lower() == "fin":
                os.system("cls")
                break