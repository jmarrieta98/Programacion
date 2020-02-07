def eliminar_duplicados(lista):
    for i in lista:
        while lista.count(i) >=2:
            lista.pop(lista.index(i))
    print(lista)

if __name__=="__main__":
    lista=[2,3,3,2,"hola","adios","hola"]
    eliminar_duplicados(lista)