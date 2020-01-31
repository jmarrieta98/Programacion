from datetime import datetime, timedelta 
fecha=datetime.strftime(datetime.strptime(input("Introduza una fecha: "),'%d/%m/%Y'),'%A')
print(fecha)

