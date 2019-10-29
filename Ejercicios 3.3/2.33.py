# Cuando el numero es divisible entre 100 o es divisible entre 4 y 100 imprime si 
# en caso contrario imprime no
# tambien hay un control de variable para que sea un numero lo que se introduce
try:
    a=int(input("numero: "))
    if not a%400 or (not a%4 and a%100):
        print("si")
    else:
        print("no")
except:
    print("no es un numero")