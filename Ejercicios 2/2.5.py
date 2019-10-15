try:
    n1 = float(input("Introduce el primero numero: "))
    n2 = float(input("Introduce el segundo numero: "))
    n3 = float(input("Introduce el tercer numero: "))
except ValueError:
    print("Error al introducir los numeros")
else:
    if n1 > n2 and n1 > n3:
        print("El mayor es ",n1)
    elif n2>n3:
        print("El mayor es ",n2)
    else:
        print("El mayor es ",n3)
