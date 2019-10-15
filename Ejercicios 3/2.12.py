positivo = 0
negativo = 0
suma = 0
numero = 1
while numero !=0:
    numero = int(input("Introduzca un numero: "))
    if numero <0:
        negativo+=1
    elif numero >0:
        positivo+=1
    suma+=numero
print("La suma es ",suma,'hay ',positivo,'numeros positivos y ',negativo,'numeros negativos')