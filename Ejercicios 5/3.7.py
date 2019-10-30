nmes=[1,2,3,4,5,6,7,8,9,10,11,12]
m30=[1,3,5,7,8,10,12]
m31=[4,6,9,11]

def fecha(d,m,a):
        if bisiesto(a)=='no' and m==2 and d==29:
            return "fecha incorrecta"
        elif m==2 and d <= 29:
                return "fecha correcta"

        if m in m30 and d <= 30:
            return "fecha correcta"
        elif m in m31 and d <=31:
            return "fecha correcta"
        else:
            return "fecha incorrecta"

def bisiesto(año):
    if not año%4:
        return "si"
    else:
        return "no"

if __name__=="__main__":
    print(fecha(int(input("Introduzca el dia de la fecha a comprobar: ")),int(input("Introduzca el mes de la fecha a comprobar: ")),int(input("Introduzca el año de la fecha a comprobar: "))))