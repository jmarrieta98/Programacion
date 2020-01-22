import random


class Carta:
    listaDePalos = ["Tréboles", "Diamantes", "Corazones", "Picas"]

    listaDeValores = ["As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Sota", "Reina", "Rey"]

    def __init__(self, palo=0, valor=0):
        self.palo = palo
        self.valor = valor

    def __str__(self):
        return (f"{self.valor} de {self.palo}")


class Mazo:
    def __init__(self):
        self.cartas = []
        for palo in Carta.listaDePalos:
            for valor in Carta.listaDeValores:
                self.cartas.append(Carta(palo, valor))
        self.mezclar()

    def __str__(self):
        imprimir = ""
        for i in range(len(self.cartas)):
            imprimir += " " + str(self.cartas[i]) + "\n"
            return imprimir

    def muestraMazo(self):
        for carta in self.cartas:
            print(carta)

    def mezclar(self):
        import random
        nCartas = len(self.cartas)
        for i in range(nCartas):
            j = random.randrange(i, nCartas)
            self.cartas[i], self.cartas[j] = self.cartas[j], self.cartas[i]

    def darCarta(self):
        return self.cartas.pop()

    def estaVacio(self):
        return (len(self.cartas) == 0)



class Mano:
    def __init__(self):
        self.cartas = []
        self.valortotal = 0

    def cogercarta(self, mazo):
        self.cartas.append(mazo.darCarta())
        self.calcularvalortotal()

    def calcularvalortotal(self):
            if self.cartas[-1].valor == 'Sota' or self.cartas[-1].valor == 'Reina' or self.cartas[-1].valor == 'Rey':
                self.valortotal += 10
            elif self.cartas[-1].valor == 'As':
                if self.valortotal + 11 > 21:
                    self.valortotal+=1
                else:
                    self.valortotal+=11
            else:
                self.valortotal += int(self.cartas[-1].valor)


if __name__ == "__main__":
    mazo = Mazo()
    jugador = Mano()
    maquina = Mano()
    jugador.cogercarta(mazo)
    print(f"Tu carta es {jugador.cartas[0]} y el valor total es {jugador.valortotal}")
    while True:
        opcion = input("¿Quieres coger otra carta?\t")
        if opcion.lower() == 's' or opcion.lower() == 'si':
            jugador.cogercarta(mazo)
            print("Tus cartas son ",end='')
            for i in jugador.cartas:
                print(i,end=", ")
            print(f"valor total : {jugador.valortotal}")
        elif opcion.lower() == 'n' or opcion.lower() == 'no':
            break
        else:
            print("Opcion no validad")
            continue
        if jugador.valortotal == 21:
            break