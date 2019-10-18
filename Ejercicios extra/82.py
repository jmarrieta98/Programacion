
def introducir(x):
    for _ in range(5):
        x.append(str.lower(input("Introduzca la palabra:\t")))
    return(x)

def minimo(lista):
    return min(lista)

if __name__=="__main__":
    lista = []
    lista=introducir(lista)
    print(minimo(lista))
