import math
def distancia(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

if __name__=="__main__":
    x1=int(input("Introduce la coordenada x: "))
    y1=int(input("Introduce la coordenada y: "))
    x2=int(input("Introduce la segunda coordenada x: "))
    y2=int(input("Introduce la segunda coordenada y: "))
    print("La distancia es ",distancia(x1,x2,y1,y2))