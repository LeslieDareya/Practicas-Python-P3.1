from tkinter import * 
from tkinter import messagebox
from ValidacionP3 import Validar 
import numpy as np

class Principal():
    def __init__(self):
        self.val = Validar()  # Crea un objeto para validaciones / Create validation object
        self.ven = Tk()       # Crea la ventana principal / Create main window
        self.ven.title("Practica 3")
        
        # Configuración de tamaño y centrado / Window size and centering
        ancho = 350
        alto = 250
        ventana_alto = self.ven.winfo_screenwidth()
        ventana_ancho = self.ven.winfo_screenheight()
        x = (ventana_alto // 2) - (ancho // 2)
        y = (ventana_ancho // 2) - (alto // 2)
        self.ven.geometry(f"{ancho}x{alto}+{x}+{y-100}")

    # -------- FUNCIONES PARA PLACEHOLDER (texto guía en cajas) / Placeholder functions --------
    def quitar_placeholder1(self,event):
        # Elimina el texto guía cuando el usuario hace clic / Remove placeholder when focused
        if self.nombre.get() == self.placeholder1:
            self.nombre.delete(0, END)
            self.nombre.config(fg="black")

    def quitar_placeholder2(self,event):        
        if self.telefono.get() == self.placeholder2:
            self.telefono.delete(0, END)
            self.telefono.config(fg="black")

    def quitar_placeholder3(self,event):     
        if self.domicilio.get() == self.placeholder3:
            self.domicilio.delete(0, END)
            self.domicilio.config(fg="black")    

    def poner_placeholder1(self,event):
        # Si está vacío, vuelve a poner el texto guía / If empty, restore placeholder
        if self.nombre.get() == "":
            self.nombre.insert(0, self.placeholder1)
            self.nombre.config(fg="gray") 

    def poner_placeholder2(self, event):        
        if self.telefono.get() == "":
            self.telefono.insert(0, self.placeholder2)
            self.telefono.config(fg="gray") 

    def poner_placeholder3(self,event):        
        if self.domicilio.get() == "":
            self.domicilio.insert(0, self.placeholder3)
            self.domicilio.config(fg="gray")            

    # -------- INTERFAZ PRINCIPAL / MAIN INTERFACE --------
    def inicio(self):  
        # Caja de texto: Nombre / Entry box: Name
        self.placeholder1 = "Nombre"
        self.nombre = Entry(self.ven, fg="gray")
        self.nombre.insert(0, self.placeholder1)
        self.nombre.bind("<FocusIn>", self.quitar_placeholder1)
        self.nombre.bind("<FocusOut>", self.poner_placeholder1)
        #self.nombre.bind("<Return>", self.validarCaja)
        self.nombre.place(x=10, y=10, width=100)

        # Caja de texto: Teléfono / Entry box: Phone
        self.placeholder2 = "Telefno"
        self.telefono = Entry(self.ven, fg="gray")
        self.telefono.insert(0, self.placeholder2)
        self.telefono.bind("<FocusIn>", self.quitar_placeholder2)
        self.telefono.bind("<FocusOut>", self.poner_placeholder2)
        #self.telefono.bind("<Return>", self.validarCaja)
        self.telefono.place(x=120, y=10, width=100)

        # Caja de texto: Domicilio / Entry box: Address
        self.placeholder3 = "Domicilio"
        self.domicilio = Entry(self.ven, fg="gray")
        self.domicilio.insert(0, self.placeholder3)
        self.domicilio.bind("<FocusIn>", self.quitar_placeholder3)
        self.domicilio.bind("<FocusOut>", self.poner_placeholder3)
        self.domicilio.bind("<Return>", self.validarCaja)
        self.domicilio.place(x=230, y=10, width=100)

        # Etiqueta para el sexo / Label for gender
        Label(self.ven, text="Sexo").place(x=10, y=30)

        # Radio buttons para seleccionar sexo / Radio buttons for gender selection
        self.modo = StringVar(value="F")
        Radiobutton(self.ven, text="F", variable=self.modo, value="F").place(x=10, y=50)
        Radiobutton(self.ven, text="M", variable=self.modo, value="M").place(x=10, y=70)
         
        # Listbox donde se muestran los registros / Listbox to show records
        self.lista= Listbox(self.ven, height=6, width=40, bg="white", font=("Helvetica",12))
        self.lista.place(x=10, y=100)

        # Botón para agregar registro / Button to add record
        Button(self.ven, text="Agregar", command=self.validarCaja, width=10).place(x=100, y=50, height=50, width=100)

        # Mantener ventana activa / Keep window open
        self.ven.mainloop()

    # -------- VALIDACIÓN Y REGISTRO / VALIDATION AND RECORD INSERTION --------
    def validarCaja(self,event=0):
        # Verifica si faltan datos / Check if any field is empty
        if (self.nombre.get() == self.placeholder1 or self.telefono.get() == self.placeholder2
            or self.domicilio == self.placeholder3):
            messagebox.showinfo("Error", "Faltan datos / Missing data")
        else:
            # Obtiene los valores de las cajas / Get entry values
            nombre = self.nombre.get()
            telefono = self.telefono.get()
            domicilio = self.domicilio.get()

            # Determina el sexo seleccionado / Determine selected gender
            if self.modo.get() ==  "F":
                Sexo = "Femenino"
            else:
                Sexo = "Masculino"

            # Crea una clave única a partir de las iniciales / Create unique key from initials
            Clave = nombre[0] + telefono[0] + domicilio[0]    

            # Combina todos los datos en un registro / Combine data into one record
            Persona = Clave + "-" + nombre + "-" + telefono + "-" + domicilio + "-" + Sexo 
            
            # Agrega el registro al Listbox / Add record to listbox
            self.lista.insert(self.lista.size()+1, Persona) 

# -------- PROGRAMA PRINCIPAL / MAIN PROGRAM --------
if __name__ == '__main__':
    app = Principal()
    app.inicio()

# validar para que nombre no numeros, telefono no letras
# validate so name cannot contain numbers and phone cannot contain letters