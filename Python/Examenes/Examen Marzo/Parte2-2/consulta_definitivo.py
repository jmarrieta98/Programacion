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
    marca=input("Introduce la marca:\t")
    modelo=input("Introduce el modelo:\t")
    combutible=input("Introduce el combustible:\t")
    potencia=  input("Introduce la potencia:\t")
    km = input("Introduce los kilometros máximos:\t")
    fecha = input("Introduce la fecha con '/':\t")
    if marca: marca = re.compile(marca)
    else: marca = re.compile(".*")
    if modelo: modelo = re.compile(modelo)
    else: modelo = re.compile(".*")
    if combutible: combutible =  re.compile(combutible)
    else: combutible = re.compile(".*")
    try:
        if potencia: potencia = int(potencia)
        else: potencia = 0
    except:
        print("Error al introducir la potencia")
    try:    
        if km: km = int(km)
        else: km = 99999
    except:
        print("Error al introducir los kilómetros")
    try: 
        if fecha: 
            fecha = fecha.split("/",3)
            fecha = date(int(fecha[2]),int(fecha[1]),int(fecha[0]))
        else: fecha = date(1885,1,1)
    except:
        print("Error al introducir la fecha")
    
    Buscar = Busqueda(marca,modelo,combutible,potencia,km,fecha)
    coches=concesionario.buscar(Buscar)
    if not coches:
        print("No se ha encontrado ningun coche con las caracteristicas dadas")
    else:
        for i in coches:
            print(i)