def en_orden_ascendente(lista):
    if lista == sorted(lista):
        return True
    else:
        return False

def esta_ordenada(lista):
    if lista == sorted(lista) or lista==sorted(lista,reverse=True):
        return True
    else:
        return False

if __name__=="__main__":
    lista=[3,2,1]
    print(esta_ordenada(lista))