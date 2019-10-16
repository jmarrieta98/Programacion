#Dado un mes del año y el día de la semana en que comienza, mostrar por pantalla una representación del
#calendario

mes=input("Introduzca el mes: ")
mes31=['Enero', 'Marzo', 'Mayo', 'Julio','Agosto', 'Octubre', 'Diciembre']
mes30=['Abril', 'Junio', 'Septiembre', 'Noviembre']
if mes in mes31:
    a=32
elif mes in mes30:
    a=31
elif mes=="Febrero":
    a=29

if mes=="Enero" or mes=="Febrero" or mes=="Marzo" or mes=="Abril" or mes=="Mayo" or mes=="Junio" or mes=="Julio" or mes=="Agosto" or mes=="Septiembre" or mes=="Octubre" or mes=="Noviembre" or mes=="Diciembre":
    dia=input("Introduzca el dia de la semana en el que empieza este mes: ")
    print(mes, '\nL\tM\tX\tJ\tV\tS\tD')
    if dia=="Lunes" or dia=="lunes" or dia=="L":
        for i in range(1,a):
            if i==7 or i==14 or i==21 or i==28:
                print (i, end='\n')
            else:
                print(i, end='\t')
    elif dia=="Martes" or dia=="martes" or dia=="M":
        print ('\t', end="")
        for i in range(1,a):
            if i==7-1 or i==14-1 or i==21-1 or i==28-1:
                print (i, end='\n')
            else:
                print(i, end='\t')
    elif dia=="Miercoles" or dia=="miercoles" or dia=="X":
        print ('\t \t', end="")
        for i in range(1,a):
            if i==7-2 or i==14-2 or i==21-2 or i==28-2:
                print (i, end='\n')
            else:
                print(i, end='\t')
    elif dia=="Jueves" or dia=="jueves" or dia=="J":
        print ('\t \t \t', end="")
        for i in range(1,a):
            if i==7-3 or i==14-3 or i==21-3 or i==28-3:
                print (i, end='\n')
            else:
                print(i, end='\t')
    elif dia=="Viernes" or dia=="viernes" or dia=="V":
        print ('\t \t \t \t', end="")
        for i in range(1,a):
            if i==7-4 or i==14-4 or i==21-4 or i==28-4:
                print (i, end='\n')
            else:
                print(i, end='\t')
    elif dia=="Sabado" or dia=="sabado" or dia=="S":
        print ('\t \t \t \t \t', end="")
        for i in range(1,a):
            if i==7-5 or i==14-5 or i==21-5 or i==28-5:
                print (i, end='\n')
            else:
                print(i, end='\t')
    elif dia=="Domingo" or dia=="domingo" or dia=="D":
        print ('\t \t \t \t \t \t', end="")
        for i in range(1,a):
            if i==7-6 or i==14-6 or i==21-6 or i==28-6:
                print (i, end='\n')
            else:
                print(i, end='\t')
    else:
        print("Eso no")
else:
    print("No")