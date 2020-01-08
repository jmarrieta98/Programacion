import operator
#Urgencia, tiempo de espera, gravedad, edad
urgencias = {'Juan': [-17,0,5,23],
           'Luis': [-43,15,2,60],
           'Joaquin': [-18,30,4,52]
}

def listar(diccionario):
    lista_diccionario = sorted(diccionario.items(), key=operator.itemgetter(1), reverse=True)
    return lista_diccionario
def citar(diccionario):
    lista=listar(diccionario)
    nombre = lista[0][0]
    del diccionario[lista[0][0]]
    media=0
    for i in lista:
        print(i[1][1])
        media+=i[1][1]
    return diccionario, nombre, media/len(lista)

def introducir(lista,urgencias):
    for i in urgencias:
        urgencias[i][1]+=15
        urgencias[i][0]=urgencias.get(i)[1]+urgencias.get(i)[2]-urgencias.get(i)[3]
    urgencias[lista[0]]=[0+int(lista[2])-int(lista[1]),0,int(lista[2]),int(lista[1])]
    return urgencias

if __name__ == "__main__":
    while True:
        opcion=input("¿Que desea hacer?:\t")
        opcion=opcion.split()
        if opcion[0] == 'salir' and len(opcion) == 1:
            break
        elif opcion[0] == 'lista' and len(opcion) == 1:
            contador=0
            for i in listar(urgencias):
                contador+=1
                print (f"{contador}.- {i[0]} {i[1][0]}")
        elif opcion[0] == 'cita' and len(opcion) == 1:
            urgencias,nombre,media=citar(urgencias)
            print(f"Se atiende a {nombre}")
            print(f"Espera media: {media} minutos")
        elif len(opcion)== 3:
            if int(opcion[1]) >=0 and int(opcion[1]) <= 150:
                if int(opcion[2]) >=0 and int(opcion[2]) <=10:
                    urgencias=introducir(opcion,urgencias)
                    contador=0
                    for i in listar(urgencias):
                        contador+=1
                        print (f"{contador}.- {i[0]} {i[1][0]}")
                else:
                    print("La gravedad no es correcta debe estar entre 0 y 10")
            else:
                print("La edad no es correcta debe estar entre 0 y 150")
        else:
            print("Error no ha introducido los datos necesarios")