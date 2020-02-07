import random
lista=["cerillas","patrulla","papel","azor","alerones","conversar","sollozo","manzana"]
palabra = random.choice(lista)
intentos = 5
palabras=[]
while intentos != 0:
    letra=input("Introduce una letra:\t")
    if letra not in list(palabra):
        intentos-=1
        print("Te quedan ",intentos,"intentos")
    else:
        palabras.append(letra)
        for i in list(palabra):
            if i in palabras:
                print(i,end=" ")
            else:
                print("_",end=" ")
        if 'si' == input("\nSabes la palabra si/no:\t"):
            if palabra==input("Introduce la palabra:\t"):
                print("Enhorabuena has acertado la palabra :)")
                break
            else:
                print("Has fallado :(")
                intentos-=1
                print("Te quedan ",intentos,"intentos")
