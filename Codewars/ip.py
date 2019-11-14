import sys
try:
    ip = sys.argv[1]
    ip = ip.split(".")
except:
    print("No has introducido nada")
else:
    if  len(ip)==4 and int(ip[0]) >=0 and int(ip[0]) <= 255 and int(ip[1]) >=0 and int(ip[1]) <= 255 and int(ip[2]) >=0 and int(ip[2]) <= 255 and int(ip[3]) >=0 and int(ip[3]) <= 255:
            print("Correcto")
    else:
        print("Incorrecto")