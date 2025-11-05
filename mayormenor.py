from tkinter import *
from tkinter import messagebox, ttk

class Principal():
    def __init__(self):
        self.ven = Tk()
        self.ven.title("Promedio de Números")
        self.ven.geometry("500x350")

        self.numeros = []

        Label(self.ven, text="Número:").place(x=30, y=20)
        self.num = Entry(self.ven, fg="blue")
        self.num.place(x=100, y=20, width=100)

        Button(self.ven, text="Agregar número", command=self.agregar_numero).place(x=220, y=17, width=120, height=30)
        Button(self.ven, text="Eliminar", command=self.eliminar_fila).place(x=360, y=17, width=100, height=30)

        Label(self.ven, text="Números agregados:").place(x=30, y=60)
        self.lista = Listbox(self.ven)
        self.lista.place(x=30, y=80, width=150, height=100)

        # Tabla (Treeview)
        columnas = ("Números", "Promedio", "Mayor", "Menor")
        self.tabla = ttk.Treeview(self.ven, columns=columnas, show="headings")
        self.tabla.place(x=200, y=80, width=270, height=200)

        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, anchor="center", width=60)

        scrolly = ttk.Scrollbar(self.ven, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscroll=scrolly.set)
        scrolly.place(x=470, y=80, height=200)

        self.ven.mainloop()

    def agregar_numero(self):
        valor = self.num.get()
        if valor == "":
            messagebox.showerror("Error", "Ingrese un número")
            return

        if not valor.isdigit():
            messagebox.showerror("Error", "Solo se permiten números enteros positivos")
            self.num.delete(0, END)
            return

        valor = int(valor)
        self.numeros.append(valor)
        self.lista.insert(END, valor)
        self.num.delete(0, END)

        if len(self.numeros) == 3:
            promedio = sum(self.numeros) / 3
            mayor = max(self.numeros)
            menor = min(self.numeros)
            numeros_str = f"{self.numeros[0]}, {self.numeros[1]}, {self.numeros[2]}"

            self.tabla.insert("", "end", values=(numeros_str, promedio, mayor, menor))

            self.numeros.clear()
            self.lista.delete(0, END)
            messagebox.showinfo("Registro completado", "Los datos fueron agregados correctamente")

    def eliminar_fila(self):
        renglon = self.tabla.selection()
        if not renglon:
            messagebox.showerror("Error", "Elige una fila para eliminar")
        else:
            self.tabla.delete(renglon)
            messagebox.showinfo("Correcto", "Fila eliminada")

if __name__ == "__main__":
    app = Principal()

