numeros = []
numero = ''
while numero != "fin":
    numero = input("Introduzca un numero: ")
    if numero == "fin":
        break
    try:
        numeros.append(int(numero))
    except ValueError:
        print("Incorrecto")
    
suma=0
for i in numeros:
    suma+=i
print(suma, len(numeros), int(suma/len(numeros)))
