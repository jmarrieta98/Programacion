import tkinter as tk
import tkinter.font as tkf
import tkinter.ttk as ttk
import random
import os
import time
from clases_8_2 import *


class Application(tk.Frame):
    # Inicializador. En él inicializamos, la pantalla principal (frame), el grid que vamos a utilizar, las imagenes, la informacion y los widgets.
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.font = tkf.Font(family="Comic Sans", size=17)
        self.agenda = Agenda()
        self.contactos = self.agenda.contactos
        self.createWidgets()

    def createWidgets(self):
        # Crea control del texto
        # Esto es un cuadro de datos, para introducir algo por parte del usuario.
        self.textoBusqueda = tk.Entry(self, font=self.font)
        # Lo incorpora en el layout
        # Se coloca al lado del label anterior
        self.textoBusqueda.grid(row=0, column=0, columnspan=4)

        # Introducimos el boton de Consulta
        self.botonconsulta = tk.Button(
            self, text='Buscar', command=self.consulta)
        self.botonconsulta.grid(row=0, column=4)  # Dónde va el botón

        # Crea el control de la tabla
        self.tabla = ttk.Treeview(self)
        # Cremamos la columna inicial
        self.tabla['columns'] = ["Nombre", "Telefono", "Grupo"]
        # Mostramos la columna inicial "heading" y le añadimos el texto
        self.tabla["show"] = "headings"
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Telefono", text="Telefono")
        self.tabla.heading("Grupo", text="Grupo")
        # Insertamos los datos de todos los contactos fila por fila
        index = 0
        for contacto in self.contactos:
            self.tabla.insert("", index, index, values=(
                contacto.nombre, contacto.telefono, contacto.grupo))
            index += 1
        # Lo incorporamos en el layout
        self.tabla.grid(row=1, column=0, columnspan=5)

        # Crea control del label
        self.Labelvacio = tk.Label(self, text="", )  # Esto es texto
        # Lo incorpora en el layout
        # Y tras crearlo, lo colocamos en una fila y columna de la tabla, en este caso pues arriba a la izquierda.
        self.Labelvacio.grid(row=2, column=0, columnspan=5)

        # Introducimos el boton de Insertar
        self.botoninsertar = tk.Button(
            self, text='Insertar', command=self.insertar)
        self.botoninsertar.grid(row=3, column=1)  # Dónde va el botón

        # Introducimos el boton de Borrar
        self.botonborrar = tk.Button(self, text='Borrar', command=self.borrar)
        self.botonborrar.grid(row=3, column=2)  # Dónde va el botón

        # Introducimos el boton de modificar
        self.botonmodificar = tk.Button(
            self, text='Editar', command=self.editar)
        self.botonmodificar.grid(row=3, column=3)  # Dónde va el botón

        # Introducimos el boton de Salir
        self.botonsalir = tk.Button(self, text='Salir', command=self.quit)
        self.botonsalir.grid(row=3, column=4)  # Dónde va el botón

    def consulta(self):
        if self.textoBusqueda.get() == "":
            self.Labelvacio['text'] = 'No ha introducido ningun nombre'
        else:
            self.Labelvacio['text'] = self.agenda.consulta(
                self.textoBusqueda.get())

    def insertar(self):
        self.ventanaInsertar = VentanaInsertar(self, self.agenda, self.font)

    def borrar(self):
        try:
            self.Labelvacio['text'] = self.agenda.borrar(
                self.contactos[int("".join(self.tabla.selection()))].nombre)
        except ValueError:
            self.Labelvacio['text'] = 'No has seleccionado ningun contacto'

    def editar(self):
        try:
            self.ventanaEditar = VentanaEditar(self, self.agenda, self.contactos[int(
                "".join(self.tabla.selection()))], self.font)
        except ValueError:
            self.Labelvacio['text'] = 'No has seleccionado ningun contacto'


# Esto es una ventana de aviso o dialogo que se abre al pulsar los botones, por ejemplo
class VentanaInsertar(tk.Toplevel):
    def __init__(self, master, agenda, font):
        tk.Toplevel.__init__(self, master)
        self.grid()
        self.agenda = agenda
        self.font = font
        self.createWidgets()

    def createWidgets(self):
        self.LabelNombre = tk.Label(
            self, text=f"Contacto a insertar:", font=self.font)
        self.LabelNombre.grid(row=0, column=0, columnspan=2)

        self.textoNombre = tk.Entry(self, font=self.font)
        self.textoNombre.grid(row=0, column=2, columnspan=2)

        self.LabelNombreTelefono = tk.Label(
            self, text="Introduce el telefono:", font=self.font)
        self.LabelNombreTelefono.grid(row=1, column=0, columnspan=2)

        self.textoTelefono = tk.Entry(self, font=self.font)
        self.textoTelefono.grid(row=1, column=2, columnspan=2)

        self.LabelVacio = tk.Label(self, text="", font=self.font)
        self.LabelVacio.grid(row=2,column=0,columnspan=4)

        self.botonInsertar = tk.Button(
            self, text='Insertar', command=self.insertar, relief=tk.FLAT, bd=0, compound=tk.CENTER, fg="#000000")
        self.botonInsertar.grid(row=3, column=1)

        self.botonSalir = tk.Button(self, text='Salir', command=self.destroy,
                                    relief=tk.FLAT, bd=0, compound=tk.CENTER, fg="#000000")
        self.botonSalir.grid(row=3, column=3)

    def insertar(self):
        if self.textoTelefono.get() == "" :
            self.LabelVacio['text'] = "Telefono no insertado"
        else:
            if self.textoNombre.get() == "":
                self.LabelVacio['text'] = 'Nombre no insertado'
            else:
                self.LabelNombre['text'] = self.agenda.alta(self.textoNombre.get(), self.textoTelefono.get())
                self.textoNombre['state'] = 'disabled'
                self.textoTelefono['state'] = 'disabled'
                self.botonInsertar['state'] = 'disabled'


class VentanaEditar(tk.Toplevel):
    def __init__(self, master, agenda, contacto, font):
        tk.Toplevel.__init__(self, master)
        self.grid()
        self.agenda = agenda
        self.font = font
        self.contacto = contacto
        self.createWidgets()

    def createWidgets(self):
        self.LabelNombre = tk.Label(self, text="Contacto:", font=self.font)
        self.LabelNombre.grid(row=0, column=0, columnspan=2)

        varnombre = tk.StringVar()
        varnombre.set(self.contacto.nombre)
        self.textoNombre = tk.Entry(
            self, textvariable=varnombre, font=self.font)
        self.textoNombre.grid(row=0, column=2, columnspan=2)

        self.LabelTelefono = tk.Label(
            self, text="Telefono", font=self.font)
        self.LabelTelefono.grid(row=1, column=0, columnspan=2)

        vartelefono = tk.StringVar()
        vartelefono.set(self.contacto.telefono)
        self.textoTelefono = tk.Entry(self, textvariable=vartelefono, font=self.font)
        self.textoTelefono.grid(row=1, column=2, columnspan=2)

        self.botonEditar = tk.Button(self, text='Editar', command=self.editar,
                                    relief=tk.FLAT, bd=0, compound=tk.CENTER, fg="#000000")
        self.botonEditar.grid(row=4, column=1)

        self.botonSalir = tk.Button(self, text='Salir', command=self.destroy,
                                    relief=tk.FLAT, bd=0, compound=tk.CENTER, fg="#000000")
        self.botonSalir.grid(row=4, column=3)

        self.LabelVacio = tk.Label(self, font=self.font)
        self.LabelVacio.grid(row=3, column=1, columnspan=4)

    def editar(self):
        if self.textoTelefono.get() == "" or self.textoNombre.get() == "":
            self.LabelVacio['text'] = "Contacto mal editado, por favor introduzca los campos de nombre y telefono"
        else:
            self.LabelVacio['text'] = self.agenda.modificar(self.contacto, self.textoNombre.get(), 
                                                            self.textoTelefono.get())
            self.textoTelefono['state'] = 'disabled'
            self.textoNombre['state'] = 'disabled'
            self.botonEditar['state'] = 'disabled'


app = Application()
app.master.title('Agenda')
app.master.geometry("650x350")
app.mainloop()
