#La WDA organiza una liga de baloncesto en la que participan 6 equipos:
#1. Chiclana Blues (CHB)
#2. Cádiz Wheels (CAW)
#3. Caleta Surfers (CSU)
#4. Conil Suns (COS)
#5. Victoria Bedouins (VIB)
#6. Cortadura Hearts (CHE)
#Debemos realizar un programa para mantener la clasificación de estos equipos de la siguiente forma:
#• Se mostrará la clasificación y se pedirá un resultado hasta que el usuario introduzca “fin”
#• Los resultados estarán en el formato EQ1 PUNTOS1 EQ2 PUNTOS2
#• Para denominar los equipos se puede usar cualquiera de sus palabras, sus iniciales o el nombre completo. Por
#ejemplo, para introducir el resultado de un partido donde jueguen los Conil Suns se puede usar Conil, Suns,
#COS o Conil Suns.
#• El formato de la clasificación será el siguiente:
#Equipo P.J.    P.G.    P.P.    P.A.F.  P.E.C.  MAR
#COS    3       2       1       256     235     +7
#...
#Donde:
#P.J. Partidos jugados
#P.G. Partidos ganados 
#P.P. Partidos perdidos
#P.A.F. Puntos a favor 
#P.E.C. Puntos en contra 
#MAR Margen de victoria/ derrota
#El margen de victoria/derrota puede ser positivo o negativo, dependiendo si el equipo marca más o menos
#puntos de los que recibe.
#El orden de la clasificación será por número de victorias, a igual número de victorias menor número de
#derrotas y si empatan en las dos anteriores por margen de victoria. Si se mantiene el empate se ordenarán
#por puntos a favor y si aún sigue el empate por orden alfabético.
ligabaloncesto = {
    'Equipo'    : [],
    'P.G.'      : [],
    'P.P.'      : [],
    'P.A.F.'    : [],
    'P.E.C.'    : [],
    'MAR'       : []
}
equipos = {
    'CHB' : ['chiclana blues','chiclana','blues','chb'],
    'CAW' : ['cádiz wheels','cádiz','wheels','caw'],
    'CSU' : ['caleta surfers','celta','surfers','csu'],
    'COS' : ['conil suns','conil','suns','cos'],
    'VIB' : ['victoria bedouins','victoria','bedouins','vib'],
    'CHE' : ['cortadura hearts','cortadura','hearts','che']
}

def traducir(eleccion,equipos):
    elec=list(equipos.items())
    for i in range(0,len(elec)):
        for j in range(0,len(elec[i][1])):
            print(elec[i][1][j])
            if eleccion[0] == elec[i][1][j]:
                eleccion[0] = elec[i][0]
            if eleccion[2] == elec[i][1][j]:
                eleccion[2] = elec[i][0]
    return eleccion
            
def grabarequipo(opcion):
    pass

if __name__ == "__main__":
    while True:
        eleccion=input("Introduce el resultado o fin para salir:\t").split(' ')
        if eleccion[0].lower() == 'fin':
            break
        elif len(eleccion) != 4:
            print("Error al introducir el resultado")
        elif eleccion[0].lower() not in sum(equipos.values(), []) or eleccion[2].lower() not in sum(equipos.values(), []) :
            print("Los equipos no estan en la liga")
        elif int(eleccion[1]) < 0 or int(eleccion[3]) < 0:
            print("Los puntos son incorrectos")
        else:
            eleccion=traducir(eleccion,equipos)
            print(eleccion)