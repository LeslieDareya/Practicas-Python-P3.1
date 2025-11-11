#Hacer un programa que le nombre, apellido paterno y materno en tres cajas separadas, ademas leer dia, mes y año en 3 cajas
#de texto separadas.  si presiona un boton se agregara a un listbox el rfc de la persona, ademas tendra 
#dos botones para eliminar elementos del list box mediante pilas o colas
from tkinter import *
from tkinter import messagebox, ttk
from valRFC import Validar
from collections import deque

class Principal:
    def __init__(self):
        # Inicializa la ventana principal y variables / Initialize main window and variables
        self.val = Validar()
        self.ven = Tk()
        self.ven.title("Generador de RFC")

        # Configuración del tamaño de ventana / Window size setup
        ancho = 550
        alto = 400
        pantalla_ancho = self.ven.winfo_screenwidth()
        pantalla_alto = self.ven.winfo_screenheight()
        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)
        self.ven.geometry(f"{ancho}x{alto}+{x}+{y-100}")

        # Estructuras de datos / Data structures
        self.pila = []          # Pila (LIFO) / Stack
        self.cola = deque()     # Cola (FIFO) / Queue
        self.modo = StringVar(value="PILA")  # Modo de eliminación por defecto / Default deletion mode

    def generarRFC(self):
        # Lee los datos de las cajas de texto / Reads data from text fields
        nombre = self.nom.get().strip()
        ap_pat = self.ap.get().strip()
        ap_mat = self.am.get().strip()
        dia = self.dia.get().strip()
        mes = self.mes.get().strip()
        anio = self.anio.get().strip()

        # Validaciones de entrada / Input validations
        if not (nombre and ap_pat and ap_mat and dia and mes and anio):
            messagebox.showerror("Error", "Faltan datos / Missing data")
            return

        if not (self.val.ValidarLetras(nombre) and self.val.ValidarLetras(ap_pat) and self.val.ValidarLetras(ap_mat)):
            messagebox.showerror("Error", "Nombre y apellidos deben contener solo letras / Name and surnames must contain only letters")
            return

        if not self.val.ValidarFecha(dia, mes, anio):
            messagebox.showerror("Error", "Fecha inválida / Invalid date")
            return

        # Genera el RFC con formato simple / Generates RFC in simple format
        rfc = ap_pat[0:2].upper() + ap_mat[0].upper() + nombre[0].upper() + anio[-2:] + mes.zfill(2) + dia.zfill(2)

        # Agrega a pila o cola dependiendo del modo / Adds to stack or queue depending on mode
        if self.modo.get() == "PILA":
            self.pila.append(rfc)
        else:
            self.cola.append(rfc)

        # Agrega al listbox / Adds to listbox
        self.lista.insert(END, rfc)
        messagebox.showinfo("Correcto", "RFC agregado correctamente / RFC added successfully")

        # Limpia las cajas de texto / Clears text boxes
        for caja in [self.nom, self.ap, self.am, self.dia, self.mes, self.anio]:
            caja.delete(0, END)

    def eliminarElemento(self):
        # Elimina un elemento según el modo (pila o cola) / Removes an element depending on mode (stack or queue)
        if self.modo.get() == "PILA":
            if not self.pila:
                messagebox.showerror("Error", "Pila vacía / Stack is empty")
                return
            eliminado = self.pila.pop()
        else:
            if not self.cola:
                messagebox.showerror("Error", "Cola vacía / Queue is empty")
                return
            eliminado = self.cola.popleft()

        # Actualiza el listbox / Updates listbox
        self.lista.delete(0, END)
        for elem in (self.pila if self.modo.get() == "PILA" else list(self.cola)):
            self.lista.insert(END, elem)

        messagebox.showinfo("Eliminado", f"Se eliminó: {eliminado} / Deleted: {eliminado}")

    def inicio(self):
        # Etiquetas y cajas de texto / Labels and text boxes
        Label(self.ven, text="Nombre / Name").place(x=10, y=10)
        self.nom = Entry(self.ven, fg="blue")
        self.nom.place(x=10, y=35, width=150)

        Label(self.ven, text="Apellido paterno / Last name (father)").place(x=180, y=10)
        self.ap = Entry(self.ven, fg="blue")
        self.ap.place(x=180, y=35, width=150)

        Label(self.ven, text="Apellido materno / Last name (mother)").place(x=350, y=10)
        self.am = Entry(self.ven, fg="blue")
        self.am.place(x=350, y=35, width=150)

        # Campos de fecha / Date fields
        Label(self.ven, text="Día / Day").place(x=10, y=80)
        self.dia = Entry(self.ven, fg="green", width=5)
        self.dia.place(x=10, y=105, width=60)

        Label(self.ven, text="Mes / Month").place(x=90, y=80)
        self.mes = Entry(self.ven, fg="green", width=5)
        self.mes.place(x=90, y=105, width=60)

        Label(self.ven, text="Año / Year").place(x=170, y=80)
        self.anio = Entry(self.ven, fg="green", width=6)
        self.anio.place(x=170, y=105, width=80)

        # Botones principales / Main buttons
        Button(self.ven, text="Agregar RFC / Add RFC", command=self.generarRFC).place(x=270, y=100, width=100, height=25)
        Button(self.ven, text="Eliminar / Delete", command=self.eliminarElemento).place(x=390, y=100, width=100, height=25)

        # Radio buttons para elegir modo / Radio buttons to choose mode
        Label(self.ven, text="Modo de eliminación / Deletion mode:").place(x=10, y=150)
        Radiobutton(self.ven, text="Pila (LIFO)", variable=self.modo, value="PILA").place(x=10, y=175)
        Radiobutton(self.ven, text="Cola (FIFO)", variable=self.modo, value="COLA").place(x=120, y=175)

        # Listbox para mostrar RFCs / Listbox to show RFCs
        Label(self.ven, text="RFC Generados / Generated RFCs").place(x=10, y=210)
        self.lista = Listbox(self.ven)
        self.lista.place(x=10, y=235, width=520, height=130)

        # Inicia la interfaz / Starts the interface
        self.ven.mainloop()


# Ejecutar el programa principal / Run main program
if __name__ == "__main__":
    app = Principal()
    app.inicio()
