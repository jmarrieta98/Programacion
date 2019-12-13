def rgb(cmyk):
    rgb=[]
    for i in range(0,3):
        rgb.append(int(round(255*(1-cmyk[i]/100)*(1-cmyk[3]/100),0)))
    return rgb

def cmyk(rgb):
    cmyk=[]
    k = 1 - max(rgb[0]/255,rgb[1]/255,rgb[2]/255)
    if k == 1:
        cmyk=[0,0,0,0]
    else:
        for i in range(0,3):
            cmyk.append(int(round(100*(1-rgb[i]/255-k)/(1-k),0)))
        cmyk.append(int(round(100*k,0)))
    return cmyk

if __name__ == "__main__":
    while True:
        opcion=input("Introduzca un color (salir):\t")
        opcion=opcion.split()
        if opcion[0] == 'salir':
            break
        elif len(opcion)==3:
            if float(opcion[0])>=0 and float(opcion[0]) <=255 and float(opcion[1]) >=0 and float(opcion[1]) <=255 and float(opcion[2])>=0 and float(opcion [2]) <= 255:
                opcion = [float(i) for i in opcion]
                print('Color cmyk:',end=' ')
                for i in cmyk(opcion):
                    print(i,end=' ')
                print()
            else:
                print("Error los numeros para rgb deben comprender entre 0 y 255")
        elif len(opcion)==4:
            if float(opcion[0])>=0 and float(opcion[0]) <=100 and float(opcion[1]) >=0 and float(opcion[1]) <=100 and float(opcion[2])>=0 and float(opcion [2]) <= 100 and float(opcion[3]) >=0 and float(opcion[3]) <=100:
                opcion = [float(i) for i in opcion]
                print('Color rgb:',end=' ')
                for i in rgb(opcion):
                    print(i,end=" ")
                print()
            else:
                print("Error los numeros para cmyk deben comprender entre 0 y 100")
        else:
            print("Error longitud no valida")