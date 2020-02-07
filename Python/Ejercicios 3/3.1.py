import math

def solpos(a,b,c):
    try:
        r=(-b+math.sqrt(b**2-4*a*c))/2*a
    except:
        return "no hay solución"
    return (-b+math.sqrt(b**2-4*a*c))/2*a

def solneg(a,b,c):
    try: 
        (-b-math.sqrt(b**2-4*a*c))/2*a
    except:    
        return "no hay solución"
    return (-b-math.sqrt(b**2-4*a*c))/2*a

if __name__=="__main__":
    x=int(input("Introduce el numero de segundo grado: "))
    y=int(input("Introduce el numero de primer grado: "))
    z=int(input("Introduce el numero: "))
    print("La primera solucion es",solpos(x,y,z),"y la segunda es",solneg(x,y,z))
