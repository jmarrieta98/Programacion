n1=int(input('Introduce un numero: '))

for i in range(2,n1):
    suma=1
    for j in range(2,i):
        if i%j==0:
            suma+=j
    if suma == i:
        print("El numero ",i," es perfecto")