import mysql.connector

cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='academia')
cursor = cnx.cursor()
query = ("SELECT nombre, nombre_curso apellido1 FROM alumnos, cursos WHERE alumnos.curso = cursos.cod_curso")
cursor.execute(query)

for nombre, curso in cursor:
  print(f"{nombre} {curso}")
cursor.close()
cnx.close()