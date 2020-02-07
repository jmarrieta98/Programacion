palabra = input("Introduzca una palabra:\t")
palabra2 = list(palabra)
letras = []
for i in palabra2:
    if i not in letras:
        print(i,": ",palabra.count(i))
        letras.append(i)

