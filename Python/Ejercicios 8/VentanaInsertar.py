import tkinter as tk

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
                self.LabelVacio['text'] = self.agenda.alta(self.textoNombre.get(), self.textoTelefono.get())
                self.textoNombre['state'] = 'disabled'
                self.textoTelefono['state'] = 'disabled'
                self.botonInsertar['state'] = 'disabled'