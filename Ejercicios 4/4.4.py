def eliminar_extremos(lista):
    lista.remove(lista[0])
    lista.remove(lista[len(lista)-1])
    return lista

def valoracion(lista):
    media = 0
    lista=eliminar_extremos(sorted(lista))
    for i in lista:
        media+=i
    return media/len(lista)

if __name__=="__main__":
    lista=[3,2,1,4,8,7,6,5]
    print(eliminar_extremos(lista))
