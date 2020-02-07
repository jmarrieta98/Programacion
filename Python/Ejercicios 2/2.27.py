numero = int(input('Introduzca un numero: '))
binario = []
while numero >= 2:
        binario.append(str(numero%2))
        numero = numero // 2
binario.append(str(numero))
binario.reverse()
binario = ''.join(binario)
print(binario)