import tkinter as tk

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