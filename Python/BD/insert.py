import mysql.connector

cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='academia')
cursor = cnx.cursor()


add_maestro = ("INSERT INTO profesores VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

data_maestro = ("Jose Manuel", "Arrieta", "Soto", "49303647L", "Valle Inclan", "Ingeniero Informático", 8000,21)

# Insert new employee
cursor.execute(add_maestro, data_maestro)
emp_no = cursor.lastrowid
print(emp_no)
# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()