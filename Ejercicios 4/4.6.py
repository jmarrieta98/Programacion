import random
def hay_duplicados(lista):
    for i in lista:
        if lista.count(i) >=2:
            return False
    return True

def numeroslista (lista):
    while len(lista)!=20:
        lista.append(random.randrange(1,100))
        if not hay_duplicados(lista):
            lista.pop(len(lista)-1)
    return lista

if __name__=="__main__":
    lista=[]
    print(numeroslista(lista))