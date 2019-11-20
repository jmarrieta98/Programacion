import sys
try:
    ip = sys.argv[1].split(".")
except:
    print("No has introducido nada")
else:
    if  len(ip)==4:
        try:
            if int(ip[0]) in range(0, 256) and int(ip[1]) in range(0, 256) and int(ip[2]) in range(0, 256) and int(ip[3]) in range(0, 256):
                print("Correcto")
            else:
                print("Valores fuera de rango")
        except:
            print("Has introducido letras o en blanco")
    else:
        print("Longitud incorrecta")