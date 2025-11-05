from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from valP4 import Validar
import numpy as np
import random

class Principal():
    def __init__(self):
        self.val = Validar()
        self.ven = Tk()
        self.ven.title('Practica 4')

        ancho = 500
        alto = 300
        ventana_alto = self.ven.winfo_screenwidth()
        ventana_ancho = self.ven.winfo_screenheight()
        x = (ventana_alto // 2) - (ancho // 2)
        y = (ventana_ancho // 2) - (alto // 2)
        self.ven.geometry(f"{ancho}x{alto}+{x}+{y-100}")

        self.cont = 0
        self.bandera = False
        self.renglon = -1
        self.index = ""

    def validarCaja(self):
        self.renglon = self.tabla.selection()
        if not self.renglon:
            messagebox.showerror("Error","Elige una fila")
        else:
            valores = self.tabla.item(self.renglon, "values")
            print(valores)
            self.index = valores[0]
            self.index = self.index[:len(self.index)-2]
            print(self.index)
            self.nombre.insert(0,valores[1])
            self.edad.insert(0,valores[3])
            self.correo.insert(0,valores[2])
            self.bandera= True

    def agregarElemento(self):
        if(len(self.nombre.get())==0 or len(self.edad.get())==0 or len(self.correo.get())==0):
            messagebox.showerror("Error","Faltan datos")
        else:
            # Validaciones de nombre, edad y correo
            if (self.val.ValidarNombre(self.nombre.get()) and 
                self.val.ValidarEdad(self.edad.get()) and 
                self.val.ValidarCorreo(self.correo.get())):

                nombre = self.nombre.get()
                edad = self.edad.get()
                correo = self.correo.get()

                if self.bandera == False:
                    self.cont += 1
                    clave = str(self.cont)+str(random.randint(1,100))+self.nombre.get()[0:2].upper()
                    self.tabla.insert("","end",values=(clave,nombre,correo,edad))
                    self.nombre.delete(0,END)
                    self.edad.delete(0,END)
                    self.correo.delete(0,END)
                else:
                    clave = self.index+self.nombre.get()[0:2].upper()
                    print("Modo edición activado")
                    self.tabla.item(self.renglon, values=(clave,nombre,correo,edad))
                    self.nombre.delete(0,END)
                    self.edad.delete(0,END)
                    self.correo.delete(0,END)
                    self.bandera = False
                    self.renglon = -1
                    messagebox.showinfo("Correcto","Datos Actualizados")
            else:
                messagebox.showinfo("Incorrecto",
                    "Verifica los datos:\n- Nombre: solo letras\n- Edad: solo números\n- Correo: debe contener '@'")

    def eliminar(self):
        renglon = self.tabla.selection()
        if not renglon:
            messagebox.showerror("Error","Elige una fila")
        else:
            self.tabla.delete(renglon)
            messagebox.showinfo("Correcto","Fila eliminada")

    def inicio(self):
        Label(self.ven, text="Nombre").place(x=10,y=10)
        self.nombre = Entry(self.ven, fg="blue")
        self.nombre.place(x=10, y=40, width=100)

        Label(self.ven, text="Edad").place(x=130,y=10)
        self.edad = Entry(self.ven, fg="green")
        self.edad.place(x=125, y=40, width=100)

        Label(self.ven, text="Correo").place(x=250,y=10)
        self.correo = Entry(self.ven, fg="purple")
        self.correo.place(x=240, y=40, width=100)

        Button(self.ven, text="Agregar", command=self.agregarElemento, width=10).place(x=380,y=50, width=100,height=30)
        Button(self.ven, text="Eliminar", command=self.eliminar, width=10).place(x=380,y=90, width=100,height=30)
        Button(self.ven, text="Selecionar", command=self.validarCaja, width=10).place(x=380,y=130, width=100,height=30)

        # Tabla
        columnas = ("Clave","Nombre","Correo","Edad")
        self.tabla = ttk.Treeview(self.ven, columns= columnas, show="headings")
        self.tabla.place(x=10, y=100, width=350,height=190)

        for col in columnas:
            self.tabla.heading(col,text=col)
            self.tabla.column(col, anchor="center", width=30)

        scrolly = ttk.Scrollbar(self.ven,orient="vertical", command=self.tabla.yview)
        scrollx = ttk.Scrollbar(self.ven, orient="horizontal", command=self.tabla.xview)
        scrolly.place(x=360,y=90,height=200)
        scrollx.place(x=10,y=280, width=350)

        self.ven.mainloop()

if __name__=='__main__':
    app = Principal()
    app.inicio()
