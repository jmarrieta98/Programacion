#Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, done n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
numero = input('Introduce un número entero entre 1 y 10: ')
try: 
    fichero = open('tabla-'+numero+'.txt', 'r')
except FileNotFoundError:
    print(f'No existe el fichero con la tabla del {numero}')
else:
    print(fichero.read())