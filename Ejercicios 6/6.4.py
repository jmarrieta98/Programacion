
lista_nacionalidad = ['Alemania', 'Argentina', 'Australia', 'Bélgica',
                      'Brasil', 'Canadá', 'Chile', 'Dinamarca', 'Egipto', 'España']
lista_nombre = ['James', 'Emma', 'Alexander', 'Anastasia',
                'Li', 'Wang', 'Ben', 'Miguel', 'Alicia', 'Sofia']


lista_motor = ['Ferrari', 'Mercedes', 'Ford', 'Renault',
               'BMW', 'Honda', 'Convetry', 'TAG', 'BRM', 'Alfa Romeo']

lista_nombre_escuderias = ['Mercedes', 'Ferrari', 'Red Bull', 'Williams',
                           'McLaren', 'Alpha Tauri', 'Haas', 'Renault', 'Alfa Romeo', 'Racing Point']

lista_pilotos = []
lista_escuderias = []


def clase_pilotos(lista_nacionalidad, lista_nombre, lista_pilotos):
    for i in range(10):
        lista_pilotos.append(
            Piloto(lista_nombre[i], lista_nacionalidad[i], i+1))


def clase_escuderias(lista_escuderias, lista_nombre_escuderias, lista_motor, lista_pilotos):
    for i in range(10):
        lista_escuderias.append(
            Escuderia(lista_nombre_escuderias[i], lista_motor[i], lista_pilotos[i]))


class Campeonato:
    pass


class Escuderia:
    def __init__(self, nombre, motor, piloto):
        self.nombre = nombre
        self.motor = motor
        self.piloto = [piloto]

    def __str__(self):
        escuderia = self.nombre + "-" + self.motor +": "
        for i in self.piloto:
            escuderia += f'{i} '
        return escuderia


class Piloto:
    def __init__(self, nombre, nacionalidad, numero):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.numero = numero

    def __str__(self):
        return f'{self.nombre}, {self.numero}, {self.nacionalidad}'


class Circuito:
    pass


if __name__ == "__main__":
    clase_pilotos(lista_nacionalidad, lista_nombre, lista_pilotos)
    clase_escuderias(lista_escuderias,lista_nombre_escuderias,lista_motor,lista_pilotos)
    for i in lista_escuderias:
        print(i)
