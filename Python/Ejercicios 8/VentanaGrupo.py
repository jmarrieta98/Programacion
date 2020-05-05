import tkinter as tk

class VentanaGrupo(tk.Toplevel):
    def __init__(self, master, agenda, contacto, font):
        tk.Toplevel.__init__(self, master)
        self.grid()
        self.agenda = agenda
        self.font = font
        self.contacto = contacto
        self.createWidgets()

    def createWidgets(self):
        self.LabelNombre = tk.Label(self, text="Contacto Principal:", font=self.font)
        self.LabelNombre.grid(row=0, column=0, columnspan=2)

        varnombre = tk.StringVar()
        varnombre.set(self.contacto.nombre)
        self.textoNombre = tk.Entry(
            self, textvariable=varnombre, font=self.font)
        self.textoNombre["state"] = "disabled"
        self.textoNombre.grid(row=0, column=2, columnspan=2)

        self.LabelNombre2 = tk.Label(self, text="Contacto a enlazar:", font=self.font)
        self.LabelNombre2.grid(row=1, column=0, columnspan=2)
  
        self.textoNombre2 = tk.Entry(self, font=self.font)
        self.textoNombre2.grid(row=1, column=2, columnspan=2)

        self.LabelVacio = tk.Label(self, font=self.font)
        self.LabelVacio.grid(row=2,column=0,columnspan=4)

        # Introducimos el boton de Insertar
        self.botoninsertar = tk.Button(
            self, text='Insertar', command=self.insertar)
        self.botoninsertar.grid(row=3, column=1)  # Dónde va el botón

        # Introducimos el boton de Borrar
        self.botonborrar = tk.Button(self, text='Borrar', command=self.borrar)
        self.botonborrar.grid(row=3, column=2)  # Dónde va el botón

        # Introducimos el boton de Salir
        self.botonsalir = tk.Button(self, text='Salir', command=self.destroy)
        self.botonsalir.grid(row=3, column=4)  # Dónde va el botón
    
    def insertar(self):
        if self.textoNombre2.get() == "":
            self.LabelVacio['text'] = "No has introducido un segundo contacto"
        else:

            self.LabelVacio['text'] = self.agenda.add_grupo(self.textoNombre.get(), self.textoNombre2.get())

    def borrar(self):
        if self.textoNombre2.get() == "":
            self.LabelVacio['text'] = "No has introducido un segundo contacto"
        else:
            self.LabelVacio['text'] = self.agenda.del_grupo(self.textoNombre.get(), self.textoNombre2.get())