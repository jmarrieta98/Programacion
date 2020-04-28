import tkinter as tk
import tkinter.font as tkf
import tkinter.ttk as ttk
import random
import os
import time
from clases_8_2 import *

class Application(tk.Frame):
    #Inicializador. En él inicializamos, la pantalla principal (frame), el grid que vamos a utilizar, las imagenes, la informacion y los widgets.
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.font = tkf.Font(family="Comic Sans", size=17)
        self.createWidgets()
        self.agenda = Agenda()
        
    
    def createWidgets(self):
        # Crea control del label
        self.Labelnombre = tk.Label(self, text="Introduce el nombre:", font=self.font) #Esto es texto
        # Lo incorpora en el layout
        self.Labelnombre.grid(row=0, column=0, columnspan=2) #Y tras crearlo, lo colocamos en una fila y columna de la tabla, en este caso pues arriba a la izquierda.
        
        # Crea control del texto
        self.textonombre = tk.Entry(self, font=self.font) #Esto es un cuadro de datos, para introducir algo por parte del usuario.
        # Lo incorpora en el layout
        self.textonombre.grid(row=0, column=2, columnspan=3)  #Se coloca al lado del label anterior

        # Crea control del label
        self.Labelvacio = tk.Label(self, text="", ) #Esto es texto
        # Lo incorpora en el layout
        self.Labelvacio.grid(row=1, column=0, columnspan=5) #Y tras crearlo, lo colocamos en una fila y columna de la tabla, en este caso pues arriba a la izquierda.

        #Introducimos el boton de Consulta
        self.botonconsulta = tk.Button(self, text='Consulta', command=self.consulta)
        self.botonconsulta.grid(row=2, column=0) #Dónde va el botón

        #Introducimos el boton de Insertar
        self.botoninsertar = tk.Button(self, text='Insertar', command=self.insertar)
        self.botoninsertar.grid(row=2, column=1) #Dónde va el botón

        #Introducimos el boton de Borrar
        self.botonborrar = tk.Button(self, text='Borrar', command=self.borrar)
        self.botonborrar.grid(row=2, column=2) #Dónde va el botón

        #Introducimos el boton de modificar
        self.botonmodificar = tk.Button(self, text='Editar', command=self.editar)
        self.botonmodificar.grid(row=2, column=3) #Dónde va el botón

        #Introducimos el boton de Salir
        self.botonsalir = tk.Button(self, text='Salir', command=self.quit)
        self.botonsalir.grid(row=2, column=4) #Dónde va el botón
        
    def consulta(self):
        if self.textonombre.get() == "":
            self.Labelvacio['text'] = 'No ha introducido ningun nombre'
        else:
            self.Labelvacio['text']= self.agenda.consulta(self.textonombre.get())
            
    def insertar(self):
        if self.textonombre.get() == "":
            self.Labelvacio['text'] = 'No ha introducido ningun nombre'
        else:
            self.ventanaInsertar = VentanaInsertar(self,self.agenda,self.textonombre.get(),self.font)
    
    def borrar(self):
        if self.textonombre.get() == "":
            self.Labelvacio['text'] = 'No ha introducido ningun nombre'
        else:
            self.Labelvacio['text'] = self.agenda.borrar(self.textonombre.get())

    def editar(self):
        if self.textonombre.get() == "":
            self.Labelvacio['text'] = 'No ha introducido ningun nombre'
        else:
            self.ventanaEditar = VentanaEditar(self,self.agenda,self.textonombre.get(),self.font)

#Esto es una ventana de aviso o dialogo que se abre al pulsar los botones, por ejemplo
class VentanaInsertar(tk.Toplevel):
    def __init__(self, master, agenda, contacto, font):
        tk.Toplevel.__init__(self, master)
        self.grid()
        self.agenda = agenda
        self.contacto = contacto
        self.font = font
        self.createWidgets()
    def createWidgets(self):
        self.LabelNombre = tk.Label(self, text=f"Contacto a insertar: {self.contacto}", font=self.font)
        self.LabelNombre.grid(row=0, column=0, columnspan=4)

        self.LabelNombreTelefono = tk.Label(self, text="Introduce el telefono:", font=self.font)
        self.LabelNombreTelefono.grid(row=1, column=0,columnspan=2 )

        self.textoTelefono = tk.Entry(self, font=self.font)
        self.textoTelefono.grid(row=1, column=2,columnspan=2 )

        self.LabelGrupo = tk.Label(self, text="Introduce si pertenece a algun grupo:", font=self.font)
        self.LabelGrupo.grid(row=2, column=0,columnspan=2 )

        self.textoGrupo = tk.Entry(self, font=self.font)
        self.textoGrupo.grid(row=2,column=2,columnspan=2)

        self.botonInsertar = tk.Button(self, text='Insertar', command=self.insertar, relief=tk.FLAT, bd=0, compound=tk.CENTER, fg="#000000")
        self.botonInsertar.grid(row=3, column=1)

        self.botonSalir = tk.Button(self, text='Salir', command=self.destroy, relief=tk.FLAT, bd=0, compound=tk.CENTER, fg="#000000")
        self.botonSalir.grid(row=3, column=3)

    def insertar(self):
        if self.textoTelefono.get() == "":
            self.LabelNombre['text'] = "Telefono no insertado"
        else:
            if self.textoGrupo.get() == "":
                self.LabelNombre['text'] = self.agenda.alta(self.contacto,self.textoTelefono.get(),"None")
            else:
                self.LabelNombre['text'] = self.agenda.alta(self.contacto,self.textoTelefono.get(),self.textoGrupo.get())
            self.textoTelefono['state'] = 'disabled'
            self.botonInsertar['state'] = 'disabled'
            self.textoGrupo['state'] = 'disabled'

class VentanaEditar(tk.Toplevel):
    def __init__(self, master, agenda, nombre, font):
        tk.Toplevel.__init__(self, master)
        self.grid()
        self.agenda = agenda
        self.font = font
        telefono, grupo = self.agenda.contacto(nombre)
        self.contacto = Contacto(nombre,telefono,grupo)
        self.createWidgets()
    def createWidgets(self):
        self.LabelNombre = tk.Label(self, text="Contacto:", font=self.font)
        self.LabelNombre.grid(row=0, column=0, columnspan=2)

        varnombre = tk.StringVar()
        varnombre.set(self.contacto.nombre)
        self.textoNombre = tk.Entry(self, textvariable=varnombre, font=self.font)
        self.textoNombre.grid(row=0, column=2, columnspan=2)

        self.LabelNombreTelefono = tk.Label(self, text="Telefono", font=self.font)
        self.LabelNombreTelefono.grid(row=1, column=0,columnspan=2 )

        vartelefono = tk.StringVar()
        vartelefono.set(self.contacto.telefono)
        self.textoTelefono = tk.Entry(self, textvariable=vartelefono, font=self.font)
        self.textoTelefono.grid(row=1, column=2,columnspan=2 )

        self.LabelGrupo = tk.Label(self, text="Grupo:", font=self.font)
        self.LabelGrupo.grid(row=2, column=0,columnspan=2 )

        vargrupo = tk.StringVar()
        vargrupo.set(self.contacto.grupo)
        self.textoGrupo = tk.Entry(self, textvariable=vargrupo, font=self.font)
        self.textoGrupo.grid(row=2,column=2,columnspan=2)

        self.botonEditar = tk.Button(self, text='Editar', command=self.editar, relief=tk.FLAT, bd=0, compound=tk.CENTER, fg="#000000")
        self.botonEditar.grid(row=4, column=1)

        self.botonSalir = tk.Button(self, text='Salir', command=self.destroy, relief=tk.FLAT, bd=0, compound=tk.CENTER, fg="#000000")
        self.botonSalir.grid(row=4, column=3)

        self.LabelVacio = tk.Label(self, font=self.font)
        self.LabelVacio.grid(row=3,column=1, columnspan=4)

    def editar(self):
        if self.textoTelefono.get() == "" or self.textoNombre.get() == "":
            self.LabelVacio['text'] = "Contacto mal editado, por favor introduzca los campos de nombre y telefono"
        else:
            if self.textoGrupo.get() == "":
                self.LabelVacio['text'] = self.agenda.modificar(self.contacto,self.textoNombre.get(), self.textoTelefono.get(),None)
            else:
                self.LabelVacio['text'] = self.agenda.modificar(self.contacto,self.textoNombre.get(), self.textoTelefono.get(), self.textoGrupo.get())
            self.textoTelefono['state'] = 'disabled'
            self.textoNombre['state'] = 'disabled'
            self.textoGrupo['state'] = 'disabled'
            self.botonEditar['state'] = 'disabled'
app = Application()                       
app.master.title('Agenda')    
app.master.geometry("600x300")
app.mainloop() 