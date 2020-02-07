try:
    n1=float(input("Introduce el primer numero: "))
    n2=float(input("Introduce el segundo numero: "))
except ValueError:
    print("Error al introducir los numeros")
else:
    operacion=input("Introduzca la operacion que desea realizar + (suma) - (resta) * (multiplicacion) / (division) ")
    if operacion == '+' or operacion.lowe == 'suma':
        print("El resultado es ",n1+n2)
    elif operacion == '-' or operacion.lower == 'resta':
        print("El resultado es ",n1-n2)
    elif operacion == '*' or operacion.lower == 'multiplicacion':
        print("El resultado es ",n1*n2)
    elif operacion == '/' or operacion.lower == 'division':
        print("El resultado es ",n1/n2)
    else:
        print("Error al introducir la operacion")