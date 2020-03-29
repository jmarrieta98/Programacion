from concesionario import *
from datetime import *
coches1 = [ Coche("V40", 2.0, "Diesel", 120, "", date(2019,2,2), 0),
                Coche("S90", 2.0, "Diesel", 150, "", date(2017,11,15), 23435) ]
coches2 = [ Coche("A3", 1.0, "Gasolina", 115, "", date(2018,8,5), 1453),
            Coche("A4", 2.0, "Gasolina", 125, "", date(2019,4,4), 0) ]
coches3 = [ Coche("Corolla", 1.5, "Híbrido", 115, "", date(2018,7,5), 7564),
            Coche("C-HR", 1.8, "Híbrido", 125, "", date(2019,2,3), 0) ]
marcas = [ Marca("Volvo", "Suecia", coches1),
           Marca("Audi", "Alemania", coches2),
           Marca("Toyota", "Japón", coches3) ]
concesionario = Concesionario("Rafael Multimotor", marcas)

if __name__ == "__main__":
    Buscar = Busqueda(input("Introduce la marca:\t"),input("Introduce el modelo:\t"),
    input("Introduce el combustible:\t"),int(input("Introduce la potencia:\t")),
    int(input("Introduce los kilometros máximos:\t")), 
    date(int(input("Introduce el año: ")),int(input("Introduce el mes: ")),int(input("Introduce el dia: ")) )   )
    coches=concesionario.buscar(Buscar)
    if not coches:
        print("No se ha encontrado ningun coche con las caracteristicas dadas")
    else:
        for i in coches:
            print(i)