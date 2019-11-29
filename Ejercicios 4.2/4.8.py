def palindromo(lista):
    lista2=[]
    for i in lista:
        if i == i[::-1]:
            lista2.append(i)
    return lista2

if __name__=="__main__":
    l=['eje','camaleon','valle','sugus','arrieta']
    lista=palindromo(l)
    if not lista:
        print("No hay ningun palindromo")
    else:
        for i in lista:
            print(i)