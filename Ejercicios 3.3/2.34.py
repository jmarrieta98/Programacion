#Te busca si el numero es primo, cuando encuentra un divisor entre 2 y antes del numero te devuelve false 
# y no es primo
try:
    a=int(input("numero: "))
    p=True
    for n in range(2,a):
        if not a%n:
            p=False
            break
    if p:
        print("si")
    else:
        print("no")
except:
    print("no es un numero")
