diccionario={}
if __name__ == "__main__":    
    with open('archivo2.csv') as f: 
        lis = [x.split() for x in f] 
    claves = lis.pop(0)
    print(claves)
    
    for i in claves:
        diccionario[i] = []
    
    for i in lis:
        for j in range(len(i)):
            diccionario[claves[j]].append(i[j])
    print(diccionario)