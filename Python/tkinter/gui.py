import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkf
import tkinter.ttk as ttk
import random
import os
import time
from agenda import Agenda, Contacto, ErrorSQL

#Toda aplicación de Tkinter debe ser englobada en una clase que siempre tiene el mismo aspecto
class Application(tk.Frame):
    #Inicializador. En él inicializamos, la pantalla principal (frame), el grid que vamos a utilizar, las imagenes, la informacion y los widgets.
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.loadResources()
        self.loadData()
        self.createWidgets()
        self.lista_contactos 

    #Aquí cargamos las imagenes y otros archivos
    def loadResources(self):
        '''
        self.images = {}
        self.images['entrar_50'] = tk.PhotoImage(file="entrar_50.png")
        self.images['salir_50'] = tk.PhotoImage(file="salir_50.png")
        self.images['cambiar_50'] = tk.PhotoImage(file="cambiar_50.png")
        '''
        self.images = { ".".join(archivo.name.split(".")[:-1]):tk.PhotoImage(file=archivo.path) for archivo in os.scandir() if archivo.name.endswith(".png") }
        self.font = tkf.Font(family="Comic Sans", size=20)

    #Aquí cargamos la información, llamando a la clase agenda que está en agenda.py!
    def loadData(self):
        self.agenda = Agenda()

    #Aquí los widgets. Esto pueden ser cuadros de texto o lo que queramos. 
    def createWidgets(self):
        self.numeroLabel = tk.Label(self, text="Introduce algo:", font=self.font) #Esto es texto
        self.numeroLabel.grid(row=0, column=0) #Y tras crearlo, lo colocamos en una fila y columna de la tabla, en este caso pues arriba a la izquierda.
        ###
        # Crea control
        self.numeroEntry = tk.Entry(self, font=self.font) #Esto es un cuadro de datos, para introducir algo por parte del usuario.
        # Lo incorpora en el layout
        self.numeroEntry.grid(row=0, column=1, columnspan=2)  #Se coloca al lado del label anterior

        self.resultadoLabel = tk.Label(self, text="Nada todavía", font=self.font) #Esto es un label donde devolveremos el resultado, en principio le ponemos cualquier cosa
        self.resultadoLabel.grid(row=1, column=0, columnspan=3) #Lo colocamos debajo de lo demás

        self.contactosList = tk.Listbox(self, activestyle=tk. NONE, selectmode='multiple', exportselection=0) #Esto es una selección multiple en forma de lista
        self.lista_contactos = self.agenda.lista_contactos() #como en el inicializador ya cogimos la agenda y la guardamos, entonces podemos listar los contactos!
        for contacto in self.lista_contactos: #Y recorrerlos para ir añadiendolos a la lista de seleccion multiple de la linea 48
            self.contactosList.insert(tk.END, contacto)
        self.contactosList.bind("<<ListboxSelect>>", self.selecciona_lista) #Esto es un bindeo. Es decir, le decimos que lo que seleccionemos en la lista, se ejecute self.selecciona_lista.
        self.contactosList.grid(row=2, column=0, columnspan=3) #Y lo añadimos en la inferfaz en la tercera fila (porque empezamos a contar por 0)
        
        self.contactosCombo = ttk.Combobox(self, state="readonly", font=self.font) #Similar a la forma de lista. Lo que pasa que este se despliega.
        self.contactosCombo.bind("<<ComboboxSelected>>", self.selecciona) #Lo mismo que en la linea 52.        self.lista_contactos = self.agenda.lista_contactos() #Cogemos los contactos
        self.contactosCombo['values'] = self.lista_contactos #Y como veis, en caso de los combos, tiene forma de diccionario.
        self.contactosCombo.grid(row=3, column=0, columnspan=3) 

        #Introducimos botones
        self.entrarButton = tk.Button(self, text='', command=self.entrar, 
            image=self.images['entrar_50'], relief=tk.FLAT, bd=0, compound=tk.CENTER, fg="#ff0000")
        self.entrarButton.grid(row=4, column=0) #Dónde va el botón

        self.cambiarButton = tk.Button(self, text='Cambiar', command=self.cambiar, 
            image=self.images['cambiar_50'], relief=tk.FLAT, bd=0, compound=tk.CENTER, fg="#ff0000")
        self.cambiarButton.grid(row=4, column=1) 

        self.quitButton = tk.Button(self, text='', command=self.quit, 
            image=self.images['salir_50'], relief=tk.FLAT, bd=0, compound=tk.CENTER, fg="#ff0000")
        self.quitButton.grid(row=4, column=2)
    #Acción del botón entrar
    def entrar(self):
        self.resultadoLabel['text'] = self.numeroEntry.get()

    #Acción del botón  cambiar
    def cambiar(self):
        digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        color = "#"
        for _ in range(6):
            color+= random.choice(digitos)
        self.resultadoLabel['fg'] = color
        self.cambiarButton['fg'] = color
    
    #Lo que hace cuando usamos el combo de la linea 55. A esto hacía referencia el bindeo. Así lo puede guardar una vez seleccionado
    def selecciona(self, evento):
        contacto = self.lista_contactos[self.contactosCombo.current()]
        self.dialogo = Dialogo(self, self.agenda, contacto, self.images, self.font)

    #Mismo funcionamiento que selecciona pero para la lista.
    def selecciona_lista(self, evento):
        contactos = [ self.lista_contactos[seleccionado] for seleccionado in self.contactosList.curselection() ]
        print("# Nueva seleccion #")
        for contacto in contactos:
            print(contacto)

        #self.dialogo = Dialogo(self, self.agenda, contacto, self.images, self.font)

#Esto es una ventana de aviso o dialogo que se abre al pulsar los botones, por ejemplo
class Dialogo(tk.Toplevel):
    def __init__(self, master, agenda, contacto, images, font): #Se inicializa igual que el frame
        tk.Toplevel.__init__(self, master)
        self.grid()
        # Hacer el dialogo modal
        self.grab_set_global()
        self.agenda = agenda
        self.images = images
        self.font = font
        self.contacto = contacto
        #self.loadResources()
        self.createWidgets()
    
    def createWidgets(self): #Al igual que en Frame, colocamos los elementos.
        variable1 = tk.StringVar()
        self.nombreLabel = tk.Label(self, text="Nombre:", font=self.font)
        self.nombreLabel.grid(row=0, column=0)
        variable1.set(self.contacto.nombre)
        self.nombreEntry = tk.Entry(self, textvariable=variable1, font=self.font) 
        self.nombreEntry.grid(row=0, column=1) 

        variable2 = tk.StringVar()
        self.telefonoLabel = tk.Label(self, text="Teléfono:", font=self.font)
        self.telefonoLabel.grid(row=1, column=0)
        variable2.set(self.contacto.telefono)
        self.telefonoEntry = tk.Entry(self, textvariable=variable2, font=self.font) 
        self.telefonoEntry.grid(row=1, column=1) 

        self.quitButton = tk.Button(self, text='Editar', command=self.editar)
        self.quitButton.grid(row=2, column=0)
        self.otroButton = tk.Button(self, text='Salir', command=self.destroy)
        self.otroButton.grid(row=2, column=1)

    def editar(self): #Esto sucede cuando editamos un contacto.
        try:
            new = Contacto(self.nombreEntry.get(), self.telefonoEntry.get())
            self.agenda.modifica_contacto(self.contacto, new)
            self.destroy() #En caso de que se edite correctamente, el cuadro de dialogo se cierra.
        except ErrorSQL:
            messagebox.showerror("Editar contacto", "Nombre ya existe") #Y en caso contrario devuelve error.
    
#Ejecución de la aplicación, el main.
app = Application()                       
app.master.title('Tkinter by example')    
#app.master.geometry("600x400")
app.mainloop() 