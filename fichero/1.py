#Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido.
try:
    numero=input("Introduce un numero del 1 al 10 para guardar su tabla de multiplicar:\t")
    num=int(numero)
except ValueError:
    print("No has introducido un numero ")
else:
    fichero=open('tabla-'+numero+'.txt',"wt")
    for i in range(1,11):
        x=num*i
        fichero.write(str(x)+'\n')
    fichero.close()
    print('Mostrando tabla')
    f = open('tabla-'+numero+'.txt', "r")
    print(f.read())