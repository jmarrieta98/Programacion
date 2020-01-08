diccionario={}

def leer (archivo):
    with open(archivo) as f: 
        lis = [x.split() for x in f] 
    claves = lis.pop(0)
    for i in claves:
        diccionario[i] = []
    for i in lis:
        for j in range(len(i)):
            diccionario[claves[j]].append(i[j])
    return (diccionario)

if __name__ == "__main__":    
    print(leer('.\Archivos\\archivo.csv'))