def suma(x,n):
    suma=0
    for i in range(0,n+1):
        suma+=x**i
    return suma

if __name__=="__main__":
    print("La suma de la progresión es ",suma(int(input("Introduzca el numero: ")),int(input("Introduce las veces que se suma: "))))