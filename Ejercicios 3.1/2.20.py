contador = 1
numero = int(input('Introduzca el numero para calcular su raiz cuadrada: '))
while contador**2 <= numero:
    contador+=1

print("La raiz cuadrada de ",numero,"es ",contador-1)