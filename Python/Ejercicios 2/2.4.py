try:
    numero = int(input("Introduzca un numero: "))
except ValueError:
    print("Error al introducir el numero")
else:
    if numero%2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")