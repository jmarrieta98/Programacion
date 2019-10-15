numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))
if numero2 == numero1**2:
    print("El segundo es el cuadrado exacto del primero")
elif numero2 < numero1**2:
    print("El segundo es menor que el cuadrado del primero")
else:
    print("El segundo es mayor que el cuadrado del primero")