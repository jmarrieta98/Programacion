#Introduzco la raiz 
# Vamos calculando la raiz en un bucle a traves de la potencia de un numero desde 1 hasta que su potencia sobrepase la raiz
#Cuando sobrepase o sea el numero lo imprimimos

contador = 1
numero = int(input('Introduzca el numero para calcular su raiz cuadrada: '))
while contador**2 <= numero:
    contador+=1

print("La raiz cuadrada de ",numero,"es ",contador-1)