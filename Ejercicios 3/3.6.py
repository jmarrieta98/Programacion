def bisiesto(año):
    if not año%4:
        return "si"
    else:
        return "no"

if __name__=="__main__":
    print("El año",bisiesto(int(input("Introduce un año: "))),"es bisiesto")
