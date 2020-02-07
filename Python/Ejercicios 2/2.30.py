#Dado un mes del año y el día de la semana en que comienza, mostrar por pantalla una representación del
#calendario

mes=input("Introduzca el mes: ")
m31=['enero', 'marzo', 'mayo', 'julio','agosto', 'octubre', 'diciembre']
m30=['abril', 'junio', 'septiembre', 'noviembre']
try:
    if str.lower(mes) in m31:
        d=31
    elif str.lower(mes) in m30:
        d=30
    elif str.lower(mes) =="febrero":
        d=28
    else: 
        d=int(mes)
except ValueError:
    print("Error al introducir el mes")
else:
    dia=input("Introduzca el dia de la semana en el que empieza este mes: ")
    print(mes, '\nL\tM\tX\tJ\tV\tS\tD')
    if str.lower(dia) == 'lunes' or str.lower(dia)=="l":
        for i in range(1,d+1):
            if i==7 or i==14 or i==21 or i==28:
                print (i, end='\n')
            else:
                print(i, end='\t')
    elif str.lower(dia)=="martes" or str.lower(dia)=="m":
        print ('\t', end="")
        for i in range(1,d+1):
            if i==7-1 or i==14-1 or i==21-1 or i==28-1:
                print (i, end='\n')
            else:
                print(i, end='\t')
    elif str.lower(dia)=="miercoles" or str.lower(dia)=="x":
        print ('\t \t', end="")
        for i in range(1,d+1):
            if i==7-2 or i==14-2 or i==21-2 or i==28-2:
                print (i, end='\n')
            else:
                print(i, end='\t')
    elif str.lower(dia)=="jueves" or str.lower(dia)=="j":
        print ('\t \t \t', end="")
        for i in range(1,d+1):
            if i==7-3 or i==14-3 or i==21-3 or i==28-3:
                print (i, end='\n')
            else:
                print(i, end='\t')
    elif str.lower(dia)=="viernes" or str.lower(dia)=="v":
        print ('\t \t \t \t', end="")
        for i in range(1,d+1):
            if i==7-4 or i==14-4 or i==21-4 or i==28-4:
                print (i, end='\n')
            else:
                print(i, end='\t')
    elif str.lower(dia)=="sabado" or str.lower(dia)=="s":
        print ('\t \t \t \t \t', end="")
        for i in range(1,d+1):
            if i==7-5 or i==14-5 or i==21-5 or i==28-5:
                print (i, end='\n')
            else:
                print(i, end='\t')
    elif str.lower(dia)=="domingo" or str.lower(dia)=="d":
        print ('\t \t \t \t \t \t', end="")
        for i in range(1,d+1):
            if i==7-6 or i==14-6 or i==21-6 or i==28-6:
                print (i, end='\n')
            else:
                print(i, end='\t')
    else:
            print("Error al introducir el dia")