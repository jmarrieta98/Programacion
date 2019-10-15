numeros=[]
for i in range(3):
    numeros.append(int(input("Introduce un numero: ")))

numeros.remove(max(numeros))
numeros.remove(min(numeros))
print(numeros[0])