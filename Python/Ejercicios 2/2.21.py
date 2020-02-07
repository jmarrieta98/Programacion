# Introducimos la distancia de ida y los dias de estancia.
#Creamos la condicion de si la distancia total es mayor a 800 y la estancia mas de 7 nos descuente el 30% 
# sino lo calculamos normal
distancia=float(input("Introduce la distancia a recorrer (ida): "))
estancia=int(input("Introduce los dias de estancia: "))
if distancia*2 > 800 and estancia > 7:
    print("El precio del billete es ",distancia*2*10*0.7)
else:
    print("El precio del billete es ",distancia*2*10)