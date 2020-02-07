import random
def numero_aleatorio():
    lista=[]
    while len(lista)!=5:
        num=random.randrange(0,9)
        if num not in lista:
            lista.append(str(random.randrange(1,9)))
    numero="".join(lista)
    return numero

def comprueba(secreto,numero):
    #Creamos diccionario para guardar los valores    
    comprobar={
            'muertos': 0,
            'heridos': 0
        }
    #Si los dos numeros son iguales hemos ganado
    if secreto==numero:
        comprobar['muertos']=5
    else:
        muertos=heridos=0
        #for i in range(0,5):
        #    if lista_s[i]==lista[i]:
        #        muertos+=1
        #for i in lista:
        #    for j in range(0,5):
        #        if i in lista_s and lista_s[j]==i and lista[j]!=lista_s[j]:
        #            heridos+=1
        #Guardamos los resultados en el diccionario
        comprobar['muertos']=muertos
        comprobar['heridos']=heridos
    #Devolvemos el diccionario con los muertos y heridos        
    return comprobar

if __name__ == "__main__":
    #Contador de intentos
    intentos=0
    #Condicion para seguir en el bucle
    acierto=False
    #Sacamos el numero aleatorio
    n_ale=numero_aleatorio()
    #Mientras no acertemos sigue el bucle
    while acierto!=True:
        numero=input("introduzca un numero:\t")
        #Comprobamos que el numero tengo 5 cifras
        if len(numero)!=5:
            print("Ese numero no tiene cinco cifras")
        else:
            #Comprobamos el numero
            diccionario=comprueba(n_ale,numero)
            #Sumamos 1 al intento
            intentos+=1
            #Si los muertos da 5 significa que hemos acertado
            if diccionario['muertos']==5:
                print('Acertaste en',intentos,'intentos')
                #Cambiamos la condicion para que termine el bucle
                acierto=True
            else:
                print(diccionario['muertos'],'muertos',diccionario['heridos'],'heridos')     