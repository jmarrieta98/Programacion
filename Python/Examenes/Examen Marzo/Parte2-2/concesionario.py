import datetime
import re


class Busqueda:
    def __init__(self, marca=None, modelo=None, combustible=None, potencia=None, km=None, año=None):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.min_potencia = potencia
        self.max_kilometros = km
        self.min_año = año

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.combustible} {self.min_potencia} {self.max_kilometros} {self.min_año}"


class Marca:
    def __init__(self, marca, nacionalidad, coches):
        self.nombre = marca
        self.nacionalidad = nacionalidad
        self.coches = []
        for coche in coches:
            self.coches.append(coche)

    def __str__(self):
        frase = f"{self.marca}, {self.nacionalidad}"
        for coche in self.coches:
            frase += f"{coche} "
        return frase


class Coche:
    def __init__(self, modelo, cilindrada, combustible, potencia, matricula, fecha, kilometros):
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.combustible = combustible
        self.potencia = potencia
        self.matricula = matricula
        self.fecha = fecha
        self.kilometros = kilometros

    def __str__(self):
        return f"{self.modelo} {self.cilindrada} {self.combustible} {self.potencia} {self.matricula} {self.fecha} {self.kilometros}"


class Concesionario:
    def __init__(self, nombre, marcas):
        self.nombre = nombre
        self.marcas = []
        for marca in marcas:
            self.marcas.append(marca)

    def __str__(self):
        frase = f"{self.nombre}\n"
        for marca in self.marcas:
            frase += f"{marca}\n"
        return frase

    def buscar(self, busqueda):
        busqueda.marca
        busqueda.modelo
        busqueda.combustible
        busqueda.min_potencia
        busqueda.max_kilometros
        busqueda.min_año
        listacoches = []
        for mar in self.marcas:
            for co in mar.coches:
                if busqueda.marca.lower() == mar.nombre.lower() and busqueda.modelo.lower() == co.modelo.lower() and busqueda.combustible.lower() == co.combustible.lower() and co.potencia >= busqueda.min_potencia and co.kilometros <= busqueda.max_kilometros  and co.fecha >= busqueda.min_año:
                    listacoches.append(co)
        return(listacoches)
