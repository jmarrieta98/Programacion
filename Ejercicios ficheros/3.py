#Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
numero = int(input('Introduce un número entero entre 1 y 10: '))
m = int(input('Introduce otro número entero entre 1 y 10: '))
nombre_fichero = 'tabla-' + str(numero) + '.txt'
try: 
    fichero = open(nombre_fichero, 'r')
except FileNotFoundError:
    print(f'No existe el fichero con la tabla del {numero}')
else:
    linea = fichero.readlines()
    print(f"{numero} x {m} = {linea[m - 1]}")