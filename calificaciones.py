from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import numpy as np

class Principal():
    def __init__(self):
        self.ven = Tk()
        self.ven.title("Control de Calificaciones")

        ancho = 600
        alto = 400
        pantalla_ancho = self.ven.winfo_screenwidth()
        pantalla_alto = self.ven.winfo_screenheight()
        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)
        self.ven.geometry(f"{ancho}x{alto}+{x}+{y-100}")

        self.cont = 0
        self.promedios = []

    def agregar(self):
        # Validar campos vacíos
        if (len(self.materia.get()) == 0 or len(self.c1.get()) == 0 or 
            len(self.c2.get()) == 0 or len(self.c3.get()) == 0):
            messagebox.showerror("Error", "Faltan datos")
        else:
            try:
                cal1 = float(self.c1.get())
                cal2 = float(self.c2.get())
                cal3 = float(self.c3.get())

                prom = round((cal1 + cal2 + cal3) / 3, 2)
                self.promedios.append(prom)
                self.cont += 1

                # Insertar en tabla
                self.tabla.insert("", "end", values=(self.cont, self.materia.get(), cal1, cal2, cal3, prom))
                # Insertar promedio en listbox
                self.listbox.insert(END, f"{self.materia.get()} - {prom}")

                # Limpiar campos
                self.materia.delete(0, END)
                self.c1.delete(0, END)
                self.c2.delete(0, END)
                self.c3.delete(0, END)

                # Si ya se agregaron 5 materias, calcular promedio general
                if len(self.promedios) == 5:
                    promedio_general = round(np.mean(self.promedios), 2)
                    self.lblProm.config(text=f"Promedio general: {promedio_general}")
                    messagebox.showinfo("Listo", "Se agregaron las 5 materias y se calculó el promedio general.")
            except ValueError:
                messagebox.showerror("Error", "Las calificaciones deben ser numéricas")

    def inicio(self):
        Label(self.ven, text="Materia:").place(x=20, y=20)
        self.materia = Entry(self.ven, fg="blue")
        self.materia.place(x=90, y=20, width=120)

        Label(self.ven, text="Calificación 1:").place(x=230, y=20)
        self.c1 = Entry(self.ven, fg="green")
        self.c1.place(x=330, y=20, width=50)

        Label(self.ven, text="Calificación 2:").place(x=390, y=20)
        self.c2 = Entry(self.ven, fg="green")
        self.c2.place(x=490, y=20, width=50)

        Label(self.ven, text="Calificación 3:").place(x=20, y=60)
        self.c3 = Entry(self.ven, fg="green")
        self.c3.place(x=120, y=60, width=50)

        Button(self.ven, text="Agregar", command=self.agregar).place(x=200, y=55, width=100, height=30)

        # Tabla
        columnas = ("No.", "Materia", "C1", "C2", "C3", "Promedio")
        self.tabla = ttk.Treeview(self.ven, columns=columnas, show="headings")
        self.tabla.place(x=20, y=100, width=550, height=150)

        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, anchor="center", width=80)

        # Listbox de promedios
        Label(self.ven, text="Promedios individuales:").place(x=20, y=260)
        self.listbox = Listbox(self.ven)
        self.listbox.place(x=20, y=280, width=200, height=80)

        # Label de promedio general
        self.lblProm = Label(self.ven, text="Promedio general: ", font=("Arial", 12, "bold"), fg="gray")
        self.lblProm.place(x=250, y=300)

        self.ven.mainloop()

if __name__ == '__main__':
    app = Principal()
    app.inicio()
