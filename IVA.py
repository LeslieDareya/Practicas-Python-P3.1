from tkinter import *
from tkinter import messagebox, ttk
from valIVA import Validar
import random

class Principal():
    def __init__(self):
        self.val = Validar()
        self.ven = Tk()
        self.ven.title('Inventario de Productos')

        ancho = 600
        alto = 400
        ventana_ancho = self.ven.winfo_screenwidth()
        ventana_alto = self.ven.winfo_screenheight()
        x = (ventana_ancho // 2) - (ancho // 2)
        y = (ventana_alto // 2) - (alto // 2)
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
            self.nombre.delete(0, END)
            self.precio.delete(0, END)
            self.cantidad.delete(0, END)
            self.nombre.insert(0, valores[1])
            self.precio.insert(0, valores[2])
            self.cantidad.insert(0, valores[3])
            self.bandera = True

    def agregarElemento(self):
        nombre = self.nombre.get()
        precio = self.precio.get()
        cantidad = self.cantidad.get()

        if len(nombre) == 0 or len(precio) == 0 or len(cantidad) == 0:
            messagebox.showerror("Error", "Faltan datos")
            return

        # Validaciones
        if not self.val.ValidarNombre(nombre):
            messagebox.showerror("Error", "El nombre solo debe contener letras y espacios")
            return
        if not self.val.ValidarPrecio(precio):
            messagebox.showerror("Error", "El precio debe ser un número positivo (puede tener decimales)")
            return
        if not self.val.ValidarCantidad(cantidad):
            messagebox.showerror("Error", "La cantidad debe ser un número entero positivo")
            return

        precio = float(precio)
        cantidad = int(cantidad)

        # Cálculos
        subtotal = precio * cantidad
        iva = subtotal * 0.16
        total = subtotal + iva

        if not self.bandera:
            self.cont += 1
            clave = str(self.cont) + str(random.randint(10, 99))
            self.tabla.insert("", "end", values=(
                clave,
                nombre,
                f"{precio:.2f}",
                cantidad,
                f"{subtotal:.2f}",
                f"{iva:.2f}",
                f"{total:.2f}"
            ))
            self.listbox.insert(END, f"{nombre} (${total:.2f})")
            messagebox.showinfo("Correcto", "Producto agregado correctamente")
        else:
            clave = self.index
            self.tabla.item(self.renglon, values=(
                clave,
                nombre,
                f"{precio:.2f}",
                cantidad,
                f"{subtotal:.2f}",
                f"{iva:.2f}",
                f"{total:.2f}"
            ))
            self.listbox.delete(self.renglon)
            self.listbox.insert(END, f"{nombre} (${total:.2f})")
            self.bandera = False
            self.renglon = -1
            messagebox.showinfo("Correcto", "Producto actualizado")

        self.nombre.delete(0, END)
        self.precio.delete(0, END)
        self.cantidad.delete(0, END)

    def eliminar(self):
        renglon = self.tabla.selection()
        if not renglon:
            messagebox.showerror("Error", "Elige una fila para eliminar")
        else:
            index = self.tabla.index(renglon)
            self.tabla.delete(renglon)
            self.listbox.delete(index)
            messagebox.showinfo("Correcto", "Producto eliminado")

    def calcularInventario(self):
        total_inventario = 0
        for fila in self.tabla.get_children():
            valores = self.tabla.item(fila, "values")
            total_inventario += float(valores[6])
        messagebox.showinfo("Total del Inventario", f"Valor total del inventario: ${total_inventario:.2f}")

    def inicio(self):
        Label(self.ven, text="Nombre del producto").place(x=10, y=10)
        self.nombre = Entry(self.ven, fg="blue")
        self.nombre.place(x=10, y=40, width=150)

        Label(self.ven, text="Precio").place(x=180, y=10)
        self.precio = Entry(self.ven, fg="green")
        self.precio.place(x=180, y=40, width=100)

        Label(self.ven, text="Cantidad").place(x=300, y=10)
        self.cantidad = Entry(self.ven, fg="purple")
        self.cantidad.place(x=300, y=40, width=100)

        Button(self.ven, text="Agregar", command=self.agregarElemento).place(x=420, y=40, width=80, height=25)
        Button(self.ven, text="Eliminar", command=self.eliminar).place(x=510, y=40, width=80, height=25)
        Button(self.ven, text="Seleccionar", command=self.validarCaja).place(x=420, y=75, width=170, height=25)
        Button(self.ven, text="Calcular Inventario", command=self.calcularInventario).place(x=420, y=110, width=170, height=25)

        # Tabla
        columnas = ("Clave", "Nombre", "Precio", "Cantidad", "Subtotal", "IVA", "Total")
        self.tabla = ttk.Treeview(self.ven, columns=columnas, show="headings")
        self.tabla.place(x=10, y=150, width=480, height=200)

        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, anchor="center", width=70)

        scrolly = ttk.Scrollbar(self.ven, orient="vertical", command=self.tabla.yview)
        scrolly.place(x=490, y=150, height=200)
        self.tabla.configure(yscroll=scrolly.set)

        # Listbox
        Label(self.ven, text="Productos agregados:").place(x=420, y=150)
        self.listbox = Listbox(self.ven)
        self.listbox.place(x=420, y=180, width=160, height=170)

        self.ven.mainloop()

if __name__ == '__main__':
    app = Principal()
    app.inicio()
