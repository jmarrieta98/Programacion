import random


class Carta:
	listaDePalos = ["Tréboles", "Diamantes", "Corazones", "Picas"]

	listaDeValores = ["nada", "As", "2", "3", "4", "5",
	    "6", "7", "8", "9", "10", "Sota", "Reina", "Rey"]

	def __init__(self, palo=0, valor=0):
		self.palo = palo
		self.valor = valor

	def __str__(self):
		return (self.listaDeValores[self.valor] +" de "+self.listaDePalos[self.palo])

	def __cmp__(self, otro):
		# controlar el palo
		if self.palo > otro.palo: return 1
		if self.palo < otro.palo: return -1
		# si son del mismo palo, controlar el valor
		if self.valor > otro.valor: return 1
		if self.valor < otro.valor: return -1
		# los valores son iguales, es un empate
		return 0


class Mazo:
	def __init__(self):
		self.cartas = []
		for palo in range(4):
			for valor in range(1, 14):
				self.cartas.append(Carta(palo, valor))

	def muestraMazo(self):
		for carta in self.cartas:
			print(carta)

	def __str__(self):
		s = ""
		for i in range(len(self.cartas)):
			s = s + " "*i + str(self.cartas[i]) + "\n"
			return s

	def mezclar(self):
		import random
		nCartas = len(self.cartas)
		for i in range(nCartas):
		    j = random.randrange(i, nCartas)
		    self.cartas[i], self.cartas[j] =\
		    self.cartas[j], self.cartas[i]

	def eliminaCarta(self, carta):
		if carta in self.cartas:
			self.cartas.remove(carta)
			return 1
		else: return 0

	def darCarta(self):
		return self.cartas.pop()

	def estaVacio(self):
		return (len(self.cartas) == 0)
        
    def repartir(self, manos, nCartas=999):
        nManos = len(manos)
        for i in range(nCartas):
            if self.estaVacio():
                break  # fin si se acaban las cartas
            else:
                carta = self.darCarta()  # da la carta superior
		        mano = manos[i % nManos]  # a quién le toca?
		        mano.agregaCarta(carta)  # agrega la carta a la mano


class Mano(Mazo):
	def __init__(self, nombre=""):
		self.cartas = []
		self.nombre = nombre

	def agregaCarta(self, carta):
		self.cartas.append(carta)

	def __str__(self):
		s = "La mano de " + self.nombre
		if self.estaVacio():
			s = s + " está vac��a\n"
		else:
			s = s + " contiene\n"
	return s + Mazo.__str__(self)


class JuegoDeCartas:
	def __init__(self):
		self.mazo = Mazo()
		self.mazo.mezclar()


class ManoDeLaMona(Mano):
	def eliminaCoincidencias(self):
		cant = 0
		cartasOriginales = self.cartas[:]
		for carta in cartasOriginales:
			empareja = Carta(3 - carta.palo, carta.valor)
			if empareja in self.cartas:
			self.cartas.remove(carta)
			self.cartas.remove(empareja)
			print "Mano %s: %s con %s" % (self.nombre, carta, empareja)
			cant = cant + 1
			return cant


class JuegoDeLaMona(JuegoDeCartas):
    def jugar(self, nombres):
	    # quitamos la Reina de Tréboles
	    self.mazo.eliminaCarta(Carta(0, 12))
	    	# construimos una mano para cada jugador
	    self.manos = []
	for nombre in nombres :
		self.manos.append(ManoDeLaMona(nombre))
		# repartimos los naipes
		self.mazo.repartir(self.manos)
		print "----- Se han repartido las cartas."
		self.muestraManos()
		# eliminamos las coincidencias iniciales
		emparejadas = self.eliminaTodasLasCoincidencias()
		print "----- Coincidencias eliminadas, el juego comienza."
		self.muestraManos()
		# se juega hasta que se han descartado las 50 cartas
		turno = 0
		cantManos = len(self.manos)
		while emparejadas < 25:
		emparejadas = emparejadas + self.jugarUnTurno(turno)
			turno = (turno + 1) % cantManos
			print "----- El juego termin�o."
			self.muestraManos()
    def eliminaTodasLasCoincidencias(self):
	    cant = 0
	    for mano in self.manos:
	    	cant = cant + mano.eliminaCoincidencias()
	    	return cant
	def jugarUnTurno(self, i):
	    if self.manos[i].estaVacio():
	    	return 0
	    	vecino = self.encuentraVecino(i)
	    cartaElegida = self.manos[vecino].darCarta()
	    self.manos[i].agregaCarta(cartaElegida)
	    print "Mano", self.manos[i].nombre, "eligi�o", cartaElegida
	    cant = self.manos[i].eliminaCoincidencias()
	    self.manos[i].mezclar()
	    return cant

	def encuentraVecino(self, i):
	    cantManos = len(self.manos)
	    for proximo in range(1,cantManos):
	    	vecino = (i + proximo) % cantManos
	    	if not self.manos[vecino].estaVacio():
	    		return vecino
	def muestraManos(self) :
	    for mano in self.manos :
	    	print mano
if __name__ == "__main__":
    # JuegoDeLaMona.jugar()
