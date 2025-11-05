from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from valISR import Validar
import random

class Principal():
    def __init__(self):
        self.val = Validar()
        self.ven = Tk()
        self.ven.title('Cálculo de Sueldos')

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
            messagebox.showerror("Error", "Elige una fila")
        else:
            valores = self.tabla.item(self.renglon, "values")
            self.index = valores[0]
            self.sueldo.delete(0, END)
            self.dias.delete(0, END)
            self.sueldo.insert(0, valores[1])
            self.dias.insert(0, valores[2])
            self.bandera = True

    def agregarElemento(self):
        if len(self.sueldo.get()) == 0 or len(self.dias.get()) == 0:
            messagebox.showerror("Error", "Faltan datos")
            return

        sueldo = self.sueldo.get()
        dias = self.dias.get()

        # Validaciones usando valP4
        if not self.val.ValidarSueldo(sueldo):
            messagebox.showerror("Error", "El sueldo debe ser un número positivo")
            return

        if not self.val.ValidarDias(dias):
            messagebox.showerror("Error", "Los días trabajados deben ser un número entre 1 y 31")
            return

        sueldo = float(sueldo)
        dias = int(dias)

        # Cálculos
        sueldo_total = sueldo * dias
        isr = sueldo_total * 0.16
        neto = sueldo_total - isr

        if not self.bandera:
            self.cont += 1
            clave = str(self.cont) + str(random.randint(10, 99))
            self.tabla.insert("", "end", values=(
                clave,
                f"{sueldo:.2f}",
                f"{dias}",
                f"{sueldo_total:.2f}",
                f"{isr:.2f}",
                f"{neto:.2f}"
            ))
            messagebox.showinfo("Correcto", "Registro agregado correctamente")
        else:
            clave = self.index
            self.tabla.item(self.renglon, values=(
                clave,
                f"{sueldo:.2f}",
                f"{dias}",
                f"{sueldo_total:.2f}",
                f"{isr:.2f}",
                f"{neto:.2f}"
            ))
            self.bandera = False
            self.renglon = -1
            messagebox.showinfo("Correcto", "Registro actualizado")

        self.sueldo.delete(0, END)
        self.dias.delete(0, END)

    def eliminar(self):
        renglon = self.tabla.selection()
        if not renglon:
            messagebox.showerror("Error", "Elige una fila")
        else:
            self.tabla.delete(renglon)
            messagebox.showinfo("Correcto", "Fila eliminada")

    def inicio(self):
        Label(self.ven, text="Sueldo base").place(x=10, y=10)
        self.sueldo = Entry(self.ven, fg="blue")
        self.sueldo.place(x=10, y=40, width=100)

        Label(self.ven, text="Días trabajados").place(x=130, y=10)
        self.dias = Entry(self.ven, fg="green")
        self.dias.place(x=130, y=40, width=100)

        Button(self.ven, text="Agregar", command=self.agregarElemento).place(x=250, y=40, width=90, height=25)
        Button(self.ven, text="Eliminar", command=self.eliminar).place(x=350, y=40, width=90, height=25)
        Button(self.ven, text="Seleccionar", command=self.validarCaja).place(x=250, y=80, width=190, height=25)

        # Tabla
        columnas = ("Clave", "Sueldo base", "Días", "Total", "ISR", "Neto")
        self.tabla = ttk.Treeview(self.ven, columns=columnas, show="headings")
        self.tabla.place(x=10, y=120, width=480, height=160)

        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, anchor="center", width=70)

        scrolly = ttk.Scrollbar(self.ven, orient="vertical", command=self.tabla.yview)
        scrolly.place(x=490, y=120, height=160)
        self.tabla.configure(yscroll=scrolly.set)

        self.ven.mainloop()

if __name__ == '__main__':
    app = Principal()
    app.inicio()
