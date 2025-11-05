from tkinter import * 
from tkinter import messagebox
from ValidacionP3 import Validar 
import numpy as np

class Principal():
    def __init__(self):
        self.val = Validar()
        self.ven = Tk()
        self.ven.title("Practica 3")
        ancho = 350
        alto = 250
        ventana_alto = self.ven.winfo_screenwidth()
        ventana_ancho = self.ven.winfo_screenheight()
        x = (ventana_alto // 2) - (ancho // 2)
        y = (ventana_ancho // 2) - (alto // 2)
        self.ven.geometry(f"{ancho}x{alto}+{x}+{y-100}")

    def quitar_placeholder1(self,event):
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

    def inicio(self):  
        #caja de texto nombre
        self.placeholder1 = "Nombre"
        self.nombre = Entry(self.ven, fg="gray")
        self.nombre.insert(0, self.placeholder1)
        self.nombre.bind("<FocusIn>", self.quitar_placeholder1)
        self.nombre.bind("<FocusOut>", self.poner_placeholder1)
        #self.nombre.bind("<Return>", self.validarCaja)
        self.nombre.place(x=10, y=10, width=100)
        #caja de texto telefono
        self.placeholder2 = "Telefno"
        self.telefono = Entry(self.ven, fg="gray")
        self.telefono.insert(0, self.placeholder2)
        self.telefono.bind("<FocusIn>", self.quitar_placeholder2)
        self.telefono.bind("<FocusOut>", self.poner_placeholder2)
        #self.telefono.bind("<Return>", self.validarCaja)
        self.telefono.place(x=120, y=10, width=100)
        # caja de texto domicilio  
        self.placeholder3 = "Domicilio"
        self.domicilio = Entry(self.ven, fg="gray")
        self.domicilio.insert(0, self.placeholder3)
        self.domicilio.bind("<FocusIn>", self.quitar_placeholder3)
        self.domicilio.bind("<FocusOut>", self.poner_placeholder3)
        self.domicilio.bind("<Return>", self.validarCaja)
        self.domicilio.place(x=230, y=10, width=100)

        Label(self.ven, text="Sexo").place(x=10, y=30)

        #Radion button
        self.modo = StringVar(value="F")
        Radiobutton(self.ven, text="F", variable=self.modo, value="F").place(x=10, y=50)
        Radiobutton(self.ven, text="M", variable=self.modo, value="M").place(x=10, y=70)
         
        #Listbox
        self.lista= Listbox(self.ven, height=6, width=40, bg="white", font=("Helvetica",12))
        self.lista.place(x=10, y=100)

        #Boton
        Button(self.ven, text="Agregar", command=self.validarCaja, width=10).place(x=100, y=50, height=50, width=100)


        self.ven.mainloop()

    def validarCaja(self,event=0):
        if (self.nombre.get() == self.placeholder1 or self.telefono.get() == self.placeholder2
            or self.domicilio == self.placeholder3):
            messagebox.showinfo("Error", "Faltan datos")
        else:
            #messagebox.showinfo('Ventana', 'Hola Mundo') 
            nombre = self.nombre.get()
            telefono = self.telefono.get()
            domicilio = self.domicilio.get()
            if self.modo.get() ==  "F":
                Sexo = "Femenino"
            else:
                Sexo = "Masculino"
                #para tomar los datos que necesites eje: [0:2]
            Clave= nombre[0] +telefono[0] +domicilio[0]    
            Persona = Clave+ "-" +nombre+ "-" +telefono+"-"+domicilio+"-"+Sexo 
            self.lista.insert(self.lista.size()+1, Persona) 

              

#Validar

if __name__ == '__main__':
    app = Principal()
    app.inicio()
   
 #validar para que nombre no numeros, telefono no letras
        