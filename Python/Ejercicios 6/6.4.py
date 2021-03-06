from datetime import date
import os
lista_nacionalidad = ['Alemania', 'Argentina', 'Australia', 'Bélgica',
                      'Brasil', 'Canadá', 'Chile', 'Dinamarca', 'Egipto', 'España']
lista_nombre = ['James', 'Emma', 'Alexander', 'Anastasia',
                'Li', 'Wang', 'Ben', 'Miguel', 'Alicia', 'Sofia']
lista_motor = ['Ferrari', 'Mercedes', 'Ford', 'Renault',
               'BMW', 'Honda', 'Convetry', 'TAG', 'BRM', 'Alfa Romeo']
lista_nombre_escuderias = ['Mercedes', 'Ferrari', 'Red Bull', 'Williams',
                           'McLaren', 'Alpha Tauri', 'Haas', 'Renault', 'Alfa Romeo', 'Racing Point']
lista_puntuacion = [25, 18, 15, 10, 8, 6, 5, 3, 2, 1]
lista_nombre_circuito = ["Circuito de Spa-Francorchamps (Bélgica)",
                         "Circuito de Monza (Italia)", "Circuito de Suzuka (Japón)", "Circuito de Sakhir(Bahrein)", "Circuito de Melbourne(Australia)", "Circuito de Gilles Villeneuve(Canada)", "Circuito de Mónaco(Mónaco)", "Circuito de Istanbul Park(Estambul)", "Circuito de Sepang(Malasia)", "Circuito de Interlagos(Brasil)"]
lista_pilotos = []
lista_escuderias = []
lista_circuito = []


def clase_circuito(lista_circuito, lista_nombre_circuito, lista_nacionalidad, lista_puntuacion, lista_nombre):
    for i in range(10):
        lista_circuito.append(Circuito(lista_nombre_circuito[i], lista_nacionalidad[i], os.popen(
            'date /t').read()[:-1], lista_puntuacion, lista_pilotos))


def clase_pilotos(lista_nacionalidad, lista_nombre, lista_pilotos):
    for i in range(10):
        lista_pilotos.append(
            Piloto(lista_nombre[i], lista_nacionalidad[i], i+1))


def clase_escuderias(lista_escuderias, lista_nombre_escuderias, lista_motor, lista_pilotos):
    for i in range(10):
        lista_escuderias.append(
            Escuderia(lista_nombre_escuderias[i], lista_motor[i], lista_pilotos[i]))


class Circuito:
    def __init__(self, circuito, pais, fecha, lista_P, lista_N):
        self.nombre = circuito
        self.pais = pais
        self.fecha = fecha
        lista = []
        for i in range(10):
            lista.append(lista_P[i])
            lista.append(lista_N[i])
            lista_N[i].puntos += lista_P[i]
        self.resultado = lista

    def __str__(self):
        circuito = self.nombre + "-" + self.pais + "-" + self.fecha + ": "
        for i in self.resultado:
            if type(i) == type(1):
                circuito += f'{i}-'
            else:
                circuito += f'{i} || '
        return circuito
    


class Campeonato:
    def __init__(self):
        self.temporada = "Temporada 1"
        self.escuderias = lista_escuderias
        self.resultados = lista_circuito

    def clasificacion_pilotos(self):
        clas_pil = sorted(lista_pilotos, key=lambda objeto: objeto.puntos, reverse=True)

    def clasificacion_escuderias(self):
        clas_esc = {}

    def calendario(self):
        for circuito in self.resultados:
                print(f"{circuito.nombre} - {circuito.fecha}:")
                for i in range(1,len(circuito.resultado),2):
                    print(f"{circuito.resultado[i-1]} {circuito.resultado[i]}",end="\t")
                print()

    def resultado(self):
        pass


class Escuderia:
    def __init__(self, nombre, motor, piloto):
        self.nombre = nombre
        self.motor = motor
        self.piloto = [piloto]

    def __str__(self):
        escuderia = self.nombre + "-" + self.motor + ": "
        for i in self.piloto:
            escuderia += f'{i} '
        return escuderia


class Piloto:
    def __init__(self, nombre, nacionalidad, numero):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.numero = numero
        self.puntos = 0

    def __str__(self):
        return f'{self.nombre}'


if __name__ == "__main__":
    clase_pilotos(lista_nacionalidad, lista_nombre, lista_pilotos)
    clase_escuderias(lista_escuderias, lista_nombre_escuderias,
                     lista_motor, lista_pilotos)
    clase_circuito(lista_circuito, lista_nombre_circuito,
                   lista_nacionalidad, lista_puntuacion, lista_nombre)
    f1 = Campeonato()
    while True:
        opcion = input("Escriba la opcion:\t")
        if opcion.lower() == 'calendario':
            f1.calendario()
        elif opcion.lower() == "clasificacion pilotos":
            pass
        elif opcion.lower() == "clasificacion escuderias":
            pass
        elif opcion.lower() == "fin":
            break
        else:
            print("Error, no has introducido un opcion valida")