import sys
def escribir(ciudad):
    pass
    archivo=open()

def leer (archivo):
    diccionario={}
    with open(archivo) as f: 
        lis = [x.split() for x in f] 
    claves = lis.pop(0)
    for i in claves:
        diccionario[i] = []
    for i in lis:
        for j in range(len(i)):
            diccionario[claves[j]].append(i[j])
    f.close
    return (diccionario)

if __name__ == "__main__":
    while True:
        diccionario=leer(".\Archivos\ListadoEstaciones2018-08.csv")
        for estacion, temperatura in diccionario.items():
            print(f"{estacion}: ", end="")
            for i in temperatura:
                print(f"{i}",end=" ")
            print("")
        ciudad = input("Introduce la estacion a guardar o salir:\t")
        if ciudad == 'salir':
            break
        elif diccionario[ciudad]:
            with open("Archivos\Aemet2018-12-31.csv",'w') as archivo:
                archivo.write(str(ciudad)+" \t")
                archivo.write(str(diccionario[ciudad]))
                archivo.close