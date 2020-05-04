from pymysql import *


class Agenda():
    def __init__(self):
        self.conexion = connect("localhost", "root", "root", "agenda2",port=3307)
        self.cursor = self.conexion.cursor()
        self.contactos = []
        self.cursor.execute("Select nombre, telefono, count(G.nombre_p) From contacto C Left join grupo G On C.nombre = G.nombre_p Group by nombre;")
        self.conexion.commit()
        for linea in self.cursor:
            self.contactos.append(Contacto(linea[0],linea[1],linea[2]))

    def mostrar(self):
        self.cursor.execute("Select * From contacto")
        self.conexion.commit()
        consulta = ''
        for nombre, telefono, grupo in self.cursor:
            consulta += f"{nombre}, {telefono}, {grupo}\n"
        return(consulta)

    def existe(self, nombre):
        self.cursor.execute("Select nombre from contacto")
        self.conexion.commit()
        lista_nombres = ["".join(i) for i in self.cursor]
        if nombre in lista_nombres:
            return True
        else:
            return False

    def consulta(self, texto):
        try:
            self.cursor.execute(
                "Select * From contacto Where nombre REGEXP %s or  telefono REGEXP %s ", (texto.lower(), texto.lower(),))
            self.conexion.commit()
        except MySQLError:
            return("Error, fallo sql")
        else:
            listacontacto = ''
            for nombre, telefono, grupo in self.cursor:
                listacontacto += f"{nombre}  -->  {telefono}\tG - {grupo}\n"
            return listacontacto

    def alta(self, nombre, telefono):
        if self.existe(nombre):
            return (f"Contacto {nombre} ya existente")
        else:
            try:
                self.cursor.execute("insert into contacto values (%s, %s)", (nombre, telefono,))
                self.conexion.commit()
            except MySQLError:
                return("Error de sql")
            else:
                return (f"Contacto {nombre} añadido")

    def borrar(self, nombre):
        if not self.existe(nombre):
            return (f"Contacto {nombre} no existente")
        else:
            try:
                self.cursor.execute(
                    "delete from contacto where lower(nombre) = %s", (nombre.lower(),))
                self.conexion.commit()
            except MySQLError:
                return ("Error de sql")
            else:
                return (f"Contacto {nombre} ha sido borrado")

    def modificar(self, contacto, nombre, telefono):
        if not self.existe(contacto.nombre):
            return (f"Contacto {nombre} no existente")
        else:
            try:
                self.cursor.execute('Update contacto set nombre = %s, telefono = %s Where nombre = %s and telefono = %s;', (
                    nombre, telefono, contacto.nombre, contacto.telefono,))
                self.conexion.commit()
            except MySQLError:
                return("Error de sql")
            else:
                return (f"Contacto {contacto.nombre} ha sido modificado por {nombre} - {telefono}")

    def contacto(self, nombre):
        self.cursor.execute(
            "Select telefono, grupo From contacto Where nombre REGEXP %s ", (nombre.lower(),))
        self.conexion.commit()
        telefono = ''
        grupo = ''
        for t, g in self.cursor:
            telefono = t
            grupo = g
        return telefono, grupo


class Contacto(object):
    def __init__(self, nombre, telefono, grupo=None):
        self.nombre = nombre
        self.telefono = telefono
        self.grupo = grupo

    def __str__(self):
        return f"{self.nombre} : {self.telefono}"
