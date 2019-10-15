from datetime import datetime, timedelta
fecha = input('Ingrese fecha ==> "d/m/a": ')
fecha = datetime.strptime(fecha, '%d/%m/%Y')
print(fecha + timedelta(days=1))