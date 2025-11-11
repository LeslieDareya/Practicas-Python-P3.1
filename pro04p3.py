from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from valP4 import Validar
import numpy as np
import random

class Principal():
    def __init__(self):
        # Se crea el objeto de validación / Create validation object
        self.val = Validar()
        # Se crea la ventana principal / Create main window
        self.ven = Tk()
        self.ven.title('Practica 4')

        # Configuración de tamaño y posición de la ventana / Window size and position
        ancho = 500
        alto = 300
        ventana_alto = self.ven.winfo_screenwidth()
        ventana_ancho = self.ven.winfo_screenheight()
        x = (ventana_alto // 2) - (ancho // 2)
        y = (ventana_ancho // 2) - (alto // 2)
        self.ven.geometry(f"{ancho}x{alto}+{x}+{y-100}")

        # Variables de control / Control variables
        self.cont = 0          # Contador para generar claves únicas / Counter for unique keys
        self.bandera = False   # Indica si se está editando un registro / Indicates edit mode
        self.renglon = -1      # Guarda el índice del renglón seleccionado / Selected row index
        self.index = ""        # Clave base para edición / Base key for editing

    def validarCaja(self):
        # Obtiene el renglón seleccionado en la tabla / Get selected row in table
        self.renglon = self.tabla.selection()
        if not self.renglon:
            messagebox.showerror("Error","Elige una fila")  # Mensaje si no hay selección / No selection message
        else:
            # Obtiene los valores de la fila / Get row values
            valores = self.tabla.item(self.renglon, "values")
            print(valores)
            # Extrae el índice base de la clave / Extract base index from key
            self.index = valores[0]
            self.index = self.index[:len(self.index)-2]
            print(self.index)
            # Carga los valores en las cajas de texto / Load values into textboxes
            self.nombre.insert(0,valores[1])
            self.edad.insert(0,valores[3])
            self.correo.insert(0,valores[2])
            # Activa modo edición / Enable edit mode
            self.bandera= True

    def agregarElemento(self):
        # Validación de campos vacíos / Check for empty fields
        if(len(self.nombre.get())==0 or len(self.edad.get())==0 or len(self.correo.get())==0):
            messagebox.showerror("Error","Faltan datos")
        else:
            # Validaciones de nombre, edad y correo / Validate name, age, and email
            if (self.val.ValidarNombre(self.nombre.get()) and 
                self.val.ValidarEdad(self.edad.get()) and 
                self.val.ValidarCorreo(self.correo.get())):

                # Obtiene los valores / Get values
                nombre = self.nombre.get()
                edad = self.edad.get()
                correo = self.correo.get()

                # Si no está en modo edición / If not in edit mode
                if self.bandera == False:
                    self.cont += 1
                    # Genera una clave única / Generate unique key
                    clave = str(self.cont)+str(random.randint(1,100))+self.nombre.get()[0:2].upper()
                    # Inserta los datos en la tabla / Insert data into table
                    self.tabla.insert("","end",values=(clave,nombre,correo,edad))
                    # Limpia las cajas de texto / Clear textboxes
                    self.nombre.delete(0,END)
                    self.edad.delete(0,END)
                    self.correo.delete(0,END)
                else:
                    # Modo edición activado / Edit mode active
                    clave = self.index+self.nombre.get()[0:2].upper()
                    print("Modo edición activado")
                    # Actualiza los datos en la tabla / Update data in table
                    self.tabla.item(self.renglon, values=(clave,nombre,correo,edad))
                    # Limpia campos y restablece variables / Clear inputs and reset flags
                    self.nombre.delete(0,END)
                    self.edad.delete(0,END)
                    self.correo.delete(0,END)
                    self.bandera = False
                    self.renglon = -1
                    messagebox.showinfo("Correcto","Datos Actualizados")
            else:
                # Mensaje de error en validación / Validation error message
                messagebox.showinfo("Incorrecto",
                    "Verifica los datos:\n- Nombre: solo letras\n- Edad: solo números\n- Correo: debe contener '@'")

    def eliminar(self):
        # Obtiene la fila seleccionada / Get selected row
        renglon = self.tabla.selection()
        if not renglon:
            messagebox.showerror("Error","Elige una fila")
        else:
            # Elimina la fila seleccionada / Delete selected row
            self.tabla.delete(renglon)
            messagebox.showinfo("Correcto","Fila eliminada")

    def inicio(self):
        # Etiquetas y cajas de texto / Labels and input fields
        Label(self.ven, text="Nombre").place(x=10,y=10)
        self.nombre = Entry(self.ven, fg="blue")
        self.nombre.place(x=10, y=40, width=100)

        Label(self.ven, text="Edad").place(x=130,y=10)
        self.edad = Entry(self.ven, fg="green")
        self.edad.place(x=125, y=40, width=100)

        Label(self.ven, text="Correo").place(x=250,y=10)
        self.correo = Entry(self.ven, fg="purple")
        self.correo.place(x=240, y=40, width=100)

        # Botones de acción / Action buttons
        Button(self.ven, text="Agregar", command=self.agregarElemento, width=10).place(x=380,y=50, width=100,height=30)
        Button(self.ven, text="Eliminar", command=self.eliminar, width=10).place(x=380,y=90, width=100,height=30)
        Button(self.ven, text="Selecionar", command=self.validarCaja, width=10).place(x=380,y=130, width=100,height=30)

        # Tabla para mostrar datos / Table to display data
        columnas = ("Clave","Nombre","Correo","Edad")
        self.tabla = ttk.Treeview(self.ven, columns= columnas, show="headings")
        self.tabla.place(x=10, y=100, width=350,height=190)

        # Configura encabezados de tabla / Configure table headers
        for col in columnas:
            self.tabla.heading(col,text=col)
            self.tabla.column(col, anchor="center", width=30)

        # Barras de desplazamiento / Scrollbars
        scrolly = ttk.Scrollbar(self.ven,orient="vertical", command=self.tabla.yview)
        scrollx = ttk.Scrollbar(self.ven, orient="horizontal", command=self.tabla.xview)
        scrolly.place(x=360,y=90,height=200)
        scrollx.place(x=10,y=280, width=350)

        self.ven.mainloop()

# Programa principal / Main program
if __name__=='__main__':
    app = Principal()
    app.inicio()