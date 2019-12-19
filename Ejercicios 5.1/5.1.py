import sys
def opcion_l(lista):
    try:
        archivo=open(lista[1])
    except FileNotFoundError:
        print("El archivo no existe")
    else:
        con_l=1
        for linea in archivo:
            if linea.find(lista[0]) == -1:
                con_l+=1
                continue
            print(f"{linea[:-1]}")
        
            

def opcion_t(lista):
    try:
        archivo=open(lista[1])
    except FileNotFoundError:
        print("El archivo no existe")
    else:
        lista_pos = []
        con_l=0
        contador=0
        for linea in archivo:
            if linea.find(lista[0]) == -1:
                con_l+=1
                continue
            contador+=1
            con_l+=1
            lista_pos.append(con_l)
        lista_pos.append(contador)
        return(lista_pos)

if __name__ == "__main__":
    opcion = sys.argv[1:]
    if len(opcion) == 3:
        if opcion[-1] == '-t':
            lista=opcion_t(opcion)
            print (f"La busqueda {opcion[0]} se ha encontrado {lista[-1]} veces, en las posicones:\t")
            for i in lista[:-1]:
                print(i, end=" ")
        elif opcion[-1] == '-l':
            opcion_l(opcion)
    else:
        print("Error datos no introducidos correctamente")