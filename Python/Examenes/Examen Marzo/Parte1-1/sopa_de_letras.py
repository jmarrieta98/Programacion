import random
cuadrado = []

abecedario=['a','b','c','d','e','f','g','h','i','k','l','m','n','ñ','o','q','r','s','t','u','w','x','y','z']

for i in range(0,10):
    linea=[]
    for j in range(0,10):
        linea.append(random.choice(abecedario))
    cuadrado.append(linea)

for lineas in cuadrado:
    for letra in lineas:
        print(f"{letra}", end=" ")
    print()
