# En este texto hay 7 países escondidos. Encuéntralos.
import unidecode

texto="Por tu galante compañía no ruega más Norita. Liada está: vende y cobra sillas. No se estanca nada y piensa en su buen vivir antes que en otra cosa. ¿Y sabes qué? ¡No se deja ponderar!"
texto = texto.replace("." , "")
texto = texto.replace(":" , "")
texto = texto.replace("¿" , "")
texto = texto.replace("?" , "")
texto = texto.replace("¡" , "")
texto = texto.replace("!" , "")
texto = texto.replace(" " , "")
paises = []

with open("retos\paises.csv", encoding="utf8") as fichero:
    lineas = [i for i in fichero.readlines()]
    lineas.pop(0)
    lineas2=[]
    for linea in lineas:
        lineas2.append(linea.split('"'))
    for linea in lineas2:
        paises.append(unidecode.unidecode(linea[3][0:-1].lower()))

for pais in paises:
    aciertos=0
    for letra in texto:
        if letra.lower() == pais[aciertos]:
            aciertos += 1
        else:
            aciertos = 0
        if len(pais) == aciertos:
            print(pais)
            break