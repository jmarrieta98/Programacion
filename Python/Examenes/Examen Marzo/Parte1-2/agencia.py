import datetime

class Ciudad():
    def __init__(self,nombre,distancia,precio_estancia):
        self.nombre = nombre
        self.distancia = distancia
        self.precioEst = precio_estancia
    
    def __str__(self):
        return f"{self.nombre} que tiene una distancia de {self.distancia} y vale {self.precioEst} "

class Viaje():
    def __init__(self,personas,Evento,precio):
        self.personas = personas
        self.precio = precio
        self.evento = Evento

    def __str__(self):
        return f"El viaje para el evento {self.evento.denominacion} es para {self.personas} personas con un precio de {self.precio}"

class Evento():
    def __init__(self,denominacion,fecha,ciudad,dias,precio_estancia):
        self.denominacion=denominacion
        self.fecha = fecha
        self.ciudad = ciudad
        self.dias = dias
        self.precio_Ent = precio_estancia
    def __str__(self) -> str:
        return f"El evento {self. denominacion} es en la fecha {self.fecha} con {self.dias} dias y de precio {self.precio_Ent} en {self.ciudad}"

    def precio_persona(self,fecha):
         precio_total = 0
         dias = int((fecha-self.fecha).days)
         precio_total=self.precio_Ent+self.ciudad.distancia*0.12+self.ciudad.precioEst*dias
         return float(precio_total)

class Agencia():
    def __init__(self,nombre,listaE):
        self.nombre=nombre
        self.eventos = []
        for evento in listaE:
            self.eventos.append(evento)

    def __str__(self):
        frase = f"La agencia {self.nombre} tiene los eventos: \n"
        for evento in self.eventos:
            frase += f"{evento}"
        return (frase)

if __name__ == "__main__":
    e1 = Evento("Concierto de Sphinx",datetime.date.today(),Ciudad("Sevilla",200,60.35),1,34)
    e2 = Evento("La vida de Brian",datetime.date.today(),Ciudad("Cádiz",0,52.12),1,7)
    agencia = Agencia("Eventos Alberti", [e1,e2])
    viaje = Viaje(2,e1,68)
    print(agencia)
    print(viaje)