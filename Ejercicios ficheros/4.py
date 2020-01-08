#Escribir un programa que acceda a un fichero de internet mediante su url y muestre por pantalla el número de palabras que contiene.
from urllib import request
from urllib.error import URLError
def palabras_archivo(url):
    try:
        file = request.urlopen(url)
    except URLError:
        return(f'¡La url {url} no existe!')
    else:
        contenido = file.read()
        return len(contenido.split())

print(palabras_archivo('https://www.marca.com/'))
print(palabras_archivo('https://txts.es/'))