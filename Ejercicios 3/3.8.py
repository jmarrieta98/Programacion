nmes=[1,2,3,4,5,6,7,8,9,10,11,12]
m30=[1,3,5,7,8,10,12]
m31=[4,6,9,11]

def fecha(d,m,a):
        if bisiesto(a)=='no' and m==2 and d==29:
            return "incorrecto"
        elif m==2 and d <= 29:
                return "correcto"

        if m in m30 and d <= 30:
            return "correcto"
        elif m in m31 and d <=31:
            return "correcto"
        else:
            return "incorrecto"

def bisiesto(año):
    if not año%4:
        return "si"
    else:
        return "no"


def mayor(ahora,nacimiento):
    if int(ahora[2])-int(nacimiento[2]) < 20:
        return("No es mayor de 20 años")
    elif int(ahora[2]) - int(nacimiento[2]) > 20:
        return("Es mayor de 20 años")
    elif int(ahora[1]) > int(nacimiento[1]) :
        return("Es mayor de 20 años")
    elif int(ahora[1]) == int(nacimiento[1]) and int(ahora[0]) >= int(nacimiento[0]):
        return("Es mayor de 20 años")
    else:
        return("Es menor de 20 años")

if __name__=="__main__":
    ahora = input('Ingrese la fecha de ahora: ')
    nacimiento = input('Ingrese la fecha de su nacimiento: ')
    ahora = ahora.split(sep='/')
    nacimiento = nacimiento.split(sep='/')
    if fecha(int(ahora[0]),int(ahora[1]),int(ahora[2])) == 'correcto' and fecha(int(nacimiento[0]),int(nacimiento[1]),int(nacimiento[2])) == 'correcto':
        print(mayor(ahora,nacimiento))