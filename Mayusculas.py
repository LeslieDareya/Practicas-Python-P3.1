from tkinter import *
from tkinter import messagebox
from valMay import Validar  # importamos la clase de validación

class PalabrasApp:
    def __init__(self):
        self.val = Validar()
        self.ven = Tk()
        self.ven.title("Separar Mayúsculas y Minúsculas")
        self.ven.geometry("600x350")

        Label(self.ven, text="Palabra:").place(x=20, y=20)
        self.txt_palabra = Entry(self.ven, width=30)
        self.txt_palabra.place(x=90, y=20)

        Button(self.ven, text="Agregar", command=self.agregar).place(x=350, y=18, width=80)
        Button(self.ven, text="Modificar", command=self.modificar).place(x=440, y=18, width=80)
        Button(self.ven, text="Eliminar", command=self.eliminar).place(x=530, y=18, width=60)

        Label(self.ven, text="Original").place(x=60, y=60)
        Label(self.ven, text="Mayúsculas").place(x=250, y=60)
        Label(self.ven, text="Minúsculas").place(x=440, y=60)

        self.lst_original = Listbox(self.ven, width=20, height=12)
        self.lst_original.place(x=20, y=90)

        self.lst_mayus = Listbox(self.ven, width=20, height=12)
        self.lst_mayus.place(x=210, y=90)

        self.lst_minus = Listbox(self.ven, width=20, height=12)
        self.lst_minus.place(x=400, y=90)

        self.ven.mainloop()

    def agregar(self):
        palabra = self.txt_palabra.get().strip()

        if not palabra:
            messagebox.showerror("Error", "Ingresa una palabra.")
            return

        # Validar que solo tenga letras
        if not self.val.solo_letras(palabra):
            messagebox.showerror("Error", "Solo se permiten letras mayúsculas y minúsculas.")
            return

        mayus = ''.join([c for c in palabra if c.isupper()])
        minus = ''.join([c for c in palabra if c.islower()])

        self.lst_original.insert(END, palabra)
        self.lst_mayus.insert(END, mayus if mayus else "(Ninguna)")
        self.lst_minus.insert(END, minus if minus else "(Ninguna)")

        self.txt_palabra.delete(0, END)
        messagebox.showinfo("Correcto", "Registro agregado correctamente.")

    def eliminar(self):
        index = self.lst_original.curselection()
        if not index:
            messagebox.showerror("Error", "Selecciona un registro para eliminar.")
            return

        idx = index[0]
        self.lst_original.delete(idx)
        self.lst_mayus.delete(idx)
        self.lst_minus.delete(idx)
        messagebox.showinfo("Correcto", "Registro eliminado correctamente.")

    def modificar(self):
        index = self.lst_original.curselection()
        if not index:
            messagebox.showerror("Error", "Selecciona un registro para modificar.")
            return

        idx = index[0]
        nueva = self.txt_palabra.get().strip()
        if not nueva:
            messagebox.showerror("Error", "Ingresa la nueva palabra.")
            return

        # Validar letras
        if not self.val.solo_letras(nueva):
            messagebox.showerror("Error", "Solo se permiten letras mayúsculas y minúsculas.")
            return

        mayus = ''.join([c for c in nueva if c.isupper()])
        minus = ''.join([c for c in nueva if c.islower()])

        self.lst_original.delete(idx)
        self.lst_mayus.delete(idx)
        self.lst_minus.delete(idx)

        self.lst_original.insert(idx, nueva)
        self.lst_mayus.insert(idx, mayus if mayus else "(Ninguna)")
        self.lst_minus.insert(idx, minus if minus else "(Ninguna)")

        self.txt_palabra.delete(0, END)
        messagebox.showinfo("Correcto", "Registro modificado correctamente.")

if __name__ == "__main__":
    PalabrasApp()
