import random
def comprobar(x,y):
    if y==x:
        print("Enhorabuena has acertador")
        return True 
    elif y<x+2 and y>x-2:
        print("Estas muy cerca")
        return False
    elif y<x:
        print("El numero es mas pequeño")
        return False
    else:
        print("El numero es mas grande")
        return False

if __name__=="__main__":
    contador=5
    y=random.randrange(0,100)
    while contador != 0:
        if not comprobar(int(input("Introduce un numero: ")),y):
            contador-=1
            print("Te queda",contador,"intentos")
        else:
            break
