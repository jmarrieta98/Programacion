import re

def decimales(abrir):
    numeros=[]
    try:
        archivo=open(abrir)
        archivo=archivo.readlines()
    except FileNotFoundError:
        return "El archivo no existe"
    else:
        for line in archivo:
            numeros.append(re.findall(r'\d+|\d+.\d+', line))
        numeros=sum(numeros,[])
        numeros=[int(i) for i in numeros ]
        return sum(numeros)/len(numeros)

if __name__ == "__main__":
    while True:
        archivo = input("Introduce el archivo a buscar:\t")
        if archivo != "":
            if decimales(archivo) == "El archivo no existe":
                print("El archivo no existe")
            else:
                print(f"La media es {decimales(archivo)}")
                break
        else:
            print("No has introducido ningun archivo")