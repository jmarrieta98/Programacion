try:
    n1 = float(input("Introduce el primero numero: "))
    n2 = float(input("Introduce el segundo numero: "))
except ValueError:
    print("Error al introducir el numero")
else:
    if n1 > n2:
        n2 = float(input("Introduce el tercer numero: "))
        if n1>n2:
            print("El mayor es ",n1)
        else:
            print("El mayor es ",n2)
    else:
        n1 = float(input("Introduce el tercer numero: "))
        if n1>n2:
            print("El mayor es ",n1)
        else:
            print("El mayor es ",n2)