def rgb(cmyk):
    rgb=[]
    for i in range(0,3):
        rgb.append(round(255*(1-cmyk[i]/100)*(1-cmyk[3]/100),0))
    return rgb

def cmyk(rgb):
    cmyk=[]
    k= 1 - max(rgb[0]/255,rgb[1]/255,rgb[2]/255)
    if k == 1:
        cmyk=[0,0,0,100]
    else:
        for i in range(0,3):
            cmyk.append(round(100*(1-rgb[i]/255-k)/(1-k),0))
        cmyk.append(round(k,2)*100)
    return cmyk

if __name__ == "__main__":
    while True:
        opcion=input("Introduzca un color (salir):\t")
        opcion=opcion.split()
        if opcion[0] == 'salir':
            break
        elif len(opcion)==3 and float(opcion[0])>=0 and float(opcion[0]) <=255 and float(opcion[1]) >=0 and float(opcion[1]) <=255 and float(opcion[2])>=0 and float(opcion [2]) <= 255:
            opcion = [float(v) for v in opcion]
            print(cmyk(opcion))
        elif len(opcion)==4 and float(opcion[0])>=0 and float(opcion[0]) <=100 and float(opcion[1]) >=0 and float(opcion[1]) <=100 and float(opcion[2])>=0 and float(opcion [2]) <= 100 and float(opcion[3]) >=0 and float(opcion[3]) <=100:
            opcion = [float(v) for v in opcion]
            print(rgb(opcion))
        else:
            print("Error al introducir los datos")