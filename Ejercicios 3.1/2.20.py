contador = 0
numero = int(input('Introduzca el numero para calcular su raiz cuadrada: '))
while contador < numero:
    contador+=1
    if contador**2 == numero:
        print("La raiz cuadrada de ",numero,"es ",contador)
        break