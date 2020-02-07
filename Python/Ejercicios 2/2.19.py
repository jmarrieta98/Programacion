#Introducimos los 3 numeros en una lista
#Eliminamos el maximo y el minimo de la lista
#Imprimimos el unico numero que queda
numeros=[]
for i in range(3):
    numeros.append(int(input("Introduce un numero: ")))

numeros.remove(max(numeros))
numeros.remove(min(numeros))
print(numeros[0])