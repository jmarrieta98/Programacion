#Primero introducimos la fecha
#Sumamos 1 al dia, si el dia es superior a los que tiene ese mes 
# se pone a uno el dia y el mes se le suma 1, si el mes pasa de 12 se pone a uno y se le suma un año
#Imprimimos la fecha
from datetime import datetime, timedelta
fecha = datetime.strptime(input('Ingrese fecha ==> "d/m/a": '), '%d/%m/%Y') + timedelta(days=1) 
print(fecha.day,'/',fecha.month,'/',fecha.year, sep='')
