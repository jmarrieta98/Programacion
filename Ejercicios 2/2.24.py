ahora = input('Ingrese la fecha de ahora: ')
nacimiento = input('Ingrese la fecha de su nacimiento: ')
ahora = ahora.split(sep='/')
nacimiento = nacimiento.split(sep='/')
if int(ahora[2])-int(nacimiento[2]) < 20:
    print("No es mayor de 20 años")
elif int(ahora[2]) - int(nacimiento[2]) > 20:
    print("Es mayor de 20 años")
elif int(ahora[1]) > int(nacimiento[1]) :
    print("Es mayor de 20 años")
elif int(ahora[1]) == int(nacimiento[1]) and int(ahora[0]) >= int(nacimiento[0]):
    print("Es mayor de 20 años")
else:
    print("Es menor de 20 años")