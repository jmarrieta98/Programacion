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
        print(leer(".\Archivos\ListadoEstaciones2018-08.csv"))
        break