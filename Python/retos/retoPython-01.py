# Sin ejecutarlo, ¿qué hace este código?

#Transforma el string en lista con el separador por defecto que es el espacio y va metiendo en un dicicionario como claves todas las palabras 
#y luego cuenta cuantas palabras metiendolo como valor en el diciconario

# Encuentra y arregla el fallito.
#Se arregla añadiendo dos replace uno para quitar la como y otro para reemplazar los puntos por espacio

strng = "Hello Hello, Welcome Welcome to python.advance.projects and start learning python"
strng = strng.replace(",", "")
strng = strng.replace(".", " ")

words = strng.split()
d = {}.fromkeys(words, 0)
for w in words:
    d[w] += 1
print(d)
