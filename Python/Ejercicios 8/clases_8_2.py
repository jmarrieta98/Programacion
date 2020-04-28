from pymysql import *


class Agenda():
    def __init__(self):
        self.conexion = connect("localhost", "root", "root", "agenda2")
        self.cursor = self.conexion.cursor()

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

    def alta(self, nombre, telefono, grupo):
        if self.existe(nombre):
            return (f"Contacto {nombre} ya existente")
        else:
            try:
                if grupo.lower() == 'none':
                    self.cursor.execute(
                        "insert into contacto(nombre, telefono) values (%s, %s)", (nombre, telefono,))
                else:
                    self.cursor.execute(
                        "insert into contacto values (%s, %s, %s)", (nombre, telefono, grupo,))
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

    def modificar(self, contacto, nombre, telefono, grupo):
        if not self.existe(contacto.nombre):
            return (f"Contacto {nombre} no existente")
        else:
            try:
                self.cursor.execute('Update contacto set nombre = %s, telefono = %s, grupo = %s Where nombre = %s and telefono = %s ', (
                    nombre, telefono, grupo, contacto.nombre, contacto.telefono,))
                self.conexion.commit()
            except MySQLError:
                return("Error de sql")
            else:
                return (f"Contacto {contacto.nombre} ha sido modificado por {nombre} - {telefono} - {grupo}")

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
