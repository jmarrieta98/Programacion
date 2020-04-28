from pymysql import connect

class Agenda():
    def __init__(self):
        self.conexion = connect("localhost", "root", "root", "agenda")
        self.cursor = self.conexion.cursor()
        self.agenda = []
        self.nombres = []
        self.iniciar()
        

    def __str__(self):
        string = ""
        for contacto in self.agenda:
            string += contacto.__str__() + "\n"
        return string

    def mostrar(self):
        for contacto in self.agenda:
            print(f"{contacto}")

    def existe(self, nombre):
        if nombre in self.nombres:
            return True
        else:
            return False


    def iniciar(self):
        self.cursor.execute("SELECT * FROM contactos")
        self.agenda = []
        self.nombres = []
        for nombre, telefono in self.cursor:
            self.agenda.append(Contacto(nombre, telefono))
            self.nombres.append(nombre)

    def consulta(self, texto):
        try:
            self.cursor.execute(
                "Select * From contactos Where nombre REGEXP %s or  telefono REGEXP %s ", (texto.lower(), texto.lower(),))
        except MySQLError:
            return("Error, fallo sql")
        else:
            listacontacto = ''
            for nombre, telefono in self.cursor:
                listacontacto += f"{nombre} --> {telefono}\n"
            return listacontacto

    def alta(self, nombre, telefono):
        if self.existe(nombre):
            return (f"Contacto {nombre} ya existente")
        else:
            try:
                self.cursor.execute(
                    "insert into contactos values (%s, %s)", (nombre, telefono,))
                self.conexion.commit()
                self.iniciar()
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
                    "delete from contactos where lower(nombre) = %s", (nombre,))
                self.conexion.commit()
                self.iniciar()
            except MySQLError:
                return ("Error de sql")
            else:
                return (f"Contacto {nombre} ha sido borrado")

    def modificar(self, nombre, telefono):
        if not self.existe(nombre):
            return (f"Contacto {nombre} no existente")
        else:
            try:
                self.cursor.execute(
                    "Update contactos set telefono = %s Where nombre = %s ", (telefono, nombre,))
                self.conexion.commit()
                self.iniciar()
            except MySQLError:
                return("Error de sql")
            else:
                return (f"Contacto {nombre} ha sido modificado por {telefono}")


class Contacto(object):
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} : {self.telefono}"
