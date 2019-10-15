try:
    dividendo=int(input('Introduce un numero: '))
    divisor=int(input('Introduce otro numero: '))
    a =  dividendo/divisor
except ZeroDivisionError :
    print("El divisor no puede ser 0")
except ValueError:
    print("Error al instroducir los numeros")
else:
    contador=0
    while dividendo > divisor:
        contador+=1
        dividendo-=divisor
    print("Conciente ",contador,'resto ',dividendo)