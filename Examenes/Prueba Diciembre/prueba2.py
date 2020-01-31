import operator
#Creamos el diccionario para guardar las puntuaciones, ya unas metidas para poder hacer otras opciones
saltos={
    'Louganis': {'salto1':23,   'salto2':24,    'salto3':28,    'salto4':22,    'salto5':19},
    'Xiao':     {'salto1':27,   'salto2':26,    'salto3':24,    'salto4':28,    'salto5':23},
    'Perez':    {'salto1':23,   'salto2':22,    'salto3':21,    'salto4':19,    'salto5':20},
    'Gordon':   {'salto1':19,   'salto2':18,    'salto3':19,    'salto4':19,    'salto5':17},
    'Chan':     {'salto1':23,   'salto2':23,    'salto3':23,    'salto4':23,    'salto5':23}
}       
#Creamos una lista con los nombres de los participantes
saltadores_l=('Louganis','Liao','Perez','Gordon','Chan')
#Funcion para eliminar la puntuacion mas chica y mas grande
def eliminar_extremos(lista):
    lista.remove(lista[0])
    lista.remove(lista[len(lista)-1])
    return lista

#Funcion que calcula la media de todos los saltadores quitando la puntuacion 
#mas mas chicha y mas grande
def saltos_media():
    lista=[]
    for key in saltos:
        sumatorio=0
        lista2=[]
        for key2 in saltos[key]:
            lista2.append(float(saltos[key].get(key2)))
        lista2=eliminar_extremos(sorted(lista2))
        for j in lista2:
            sumatorio+=j
        lista.append(round(sumatorio/len(lista2),2))
    return lista   
#Funcion que me inserta en el diccionario las 5 puntuaciones del participante que se eliga
def saltadores(eleccion):
    for i in range(1,6):
        intento='salto'+str(i)
        saltos[eleccion].update({intento:opcion[i]})
#Funcion que calcula la media y la ordena segun la puntuacion de mas grande a mas chico
def clasificaciones():
    clasificacion={
        'Louganis':0,
        'Xiao':    0,
        'Perez':   0,
        'Gordon':  0,
        'Chan':    0
        }
    lista=[]
    for key in saltos:
        sumatorio=0
        lista=[]
        for key2 in saltos[key]:
            lista.append(int(saltos[key].get(key2)))
        lista=eliminar_extremos(sorted(lista))
        for j in lista:
            sumatorio+=j
        clasificacion[key]=round(sumatorio/len(lista),2)
        #Esta parte hacemos que se cree una lista con la clave del diccionario (nombre del competidor) 
        # y su media juntos, de cada competidor, ademas de ordenarla de mas grande a mas chica la media
    return sorted(clasificacion.items(), key=operator.itemgetter(1), reverse=True)

if __name__ == "__main__":
    eleccion=''
    while eleccion != 'salir':
        opcion=input("¿Que desea hacer?\t").split(' ')
        eleccion=opcion[0]
        if eleccion in saltadores_l:
            #Comprobamos que las puntuaciones sean correctas, el try para que sean numero, 
            # el elif para que este la puntuacion entre 0 y 40 y el else para que se meta5 puntuaciones
            try:
                print(int(opcion[1])>=0, int(opcion[1])<=40, int(opcion[2])>=0, int(opcion[2])<=40, int(opcion[3]) >=0, int(opcion[3])<=40, int(opcion[4])>=0, int(opcion[4])<=40, int(opcion[5])>=0, int(opcion[5])<=40)
                if len(opcion) == 6 and int(opcion[1])>=0 and int(opcion[1])<=40 and int(opcion[2])>=0 and int(opcion[2])<=40 and int(opcion[3]) >=0 and int(opcion[3])<=40 and int(opcion[4])>=0 and int(opcion[4])<=40 and int(opcion[5])>=0 and int(opcion[5])<=40:
                    saltadores()
                elif len(opcion)==6: 
                    print("La puntuacion debe estar entre 0 y 40")
                else:
                    print("Error no has introducido la puntuacion de los 5 saltos")
            except:
                print("Error no has introducido numeros")
        elif eleccion == 'saltos':
            lista=saltos_media()
            for i in range(0,len(lista)):
                print(saltadores_l[i],lista[i])
        elif eleccion == 'clasificacion':
            clas=clasificaciones()    
            puntuacion=1
            for name in enumerate(clas):
                print(puntuacion,'- ',name[1][0],name[1][1])
                puntuacion+=1
        elif eleccion != 'salir':
            print('Introducción no valida')