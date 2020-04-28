import pymysql

#Clase Agenda. No almacena información, pues no tendría sentido, para eso está la base de datos. Sólo realiza la conexión y devuelve una lista
class Agenda:
    def __init__(self, database="agenda", user="root", password="root"): #Conexión
        self.connection = pymysql.connect("localhost", user, password, database) #Debe existir
    
    def lista_contactos(self): #Devuelve la lista para ser tratada.
        resultado = []
        with self.connection.cursor() as cursor: #Se crea un cursor. A traves de este elemento, podemos ejecutar sentencias SQL. Es una especie de buffer
            cursor.execute("SELECT * FROM contactos") #Una vez teniendo el cursor, ejecutamos lo que queramos. En este caso, coger todos los contactos. ¿Es efectivo? No mucho, pero sabiendo cómo ejecutar una sentencia, ya sabéis que podéis hacer lo que queráis.
            #for nombre, telefono in cursor:
            #    resultado.append(Contacto(nombre, telefono))
            resultado = [ Contacto(nombre, telefono) for nombre,telefono in cursor ] #guardamos en resultado toda la información adquirida por el cursor. Creando un Contacto por cada nombre y telefono devuelto en linea 11
        return resultado 
    
    def modifica_contacto(self, old, new):
        cursor = self.connection.cursor() #Hacemos funcionar el cursor
        try:
            cursor.execute("update contactos set nombre=%s, telefono=%s where nombre=%s", (new.nombre,new.telefono,old.nombre )) #sentencia SQL para actualizar un contacto. Como veis, execute permite paso de variables que corresponden en orden con los %s
        except pymysql.err.IntegrityError: #Si salta un error, llamaría a la clase de la linea 24 con un codigo de error que diga que el nombre ya existe.
            raise ErrorSQL("Nombre ya existe")

class ErrorSQL(pymysql.err.IntegrityError): #Tratamiento de errores SQL.
    def __init__(self, texto):
        pymysql.err.IntegrityError.__init__(self, texto)

class Contacto: #Cómo almacenamos los contactos devueltos en linea 10.
    def __init__(self, nombre, telefono): #Esto es lo que recibe en linea 14, nombre y telefono.
        self.nombre = nombre
        self.telefono = telefono 

    def __str__(self): #Para imprimir los contactos.
        return f"{self.nombre} : {self.telefono}"


#El main del programa para probar el funcionamiento. Simple control de errores.
if __name__ == "__main__":
    agenda = Agenda() #creo la agenda, osea la conexion con la bbdd
    lista = agenda.lista_contactos() #guardo los contactos en lista
    for c in lista:
        print(c) # imprimo todos los contactos
    correcto = True
    if isinstance(lista, list): #y aqui voy a probar si se han creado los contactos de manera correcta.
        for elemento in lista:
            if not isinstance(elemento, Contacto): #comprobando que todos los elementos son de la clase Contacto linea 28.
                correcto=False
                break
    else:
        correcto = False
    if not correcto:
        print("Algo falla en agenda...")
    else:
        print("Todo correcto")
