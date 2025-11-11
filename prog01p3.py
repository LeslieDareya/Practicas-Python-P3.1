# buebuja y seleccion de ordenamiento conceptos
# Bubble and selection sort concepts
# agregar 2 radio button arriba de ordenar abajo de radio button eliminar y 
# add 2 radio buttons above "ordenar" and below "eliminar" button

from tkinter import *
from tkinter import messagebox
from Validaciones import Validar
import numpy as np

class Principal():
    def __init__(self):
        self.val = Validar()  # Inicializa la clase de validaciones / Initialize validation class
        self.ven = Tk()       # Crea la ventana principal / Create main window
        
        # Configuración de tamaño y centrado / Set window size and center it
        ancho = 320
        alto = 210
        ventana_alto = self.ven.winfo_screenwidth()
        ventana_ancho = self.ven.winfo_screenheight()
        x = (ventana_alto // 2) - (ancho // 2)
        y = (ventana_ancho // 2) - (alto // 2)
        self.ven.geometry(f'{ancho}x{alto}+{x}+{y-100}')
        
        # Lista vacía donde se guardan los datos / Empty list to store data
        self.lis = []

    def validarCaja(self):
        # Obtiene el valor del cuadro de texto / Get value from entry box
        valor = self.dato.get()
        
        # Verifica si el valor es un número y cumple con las reglas / Check if value is numeric and valid
        if (self.val.ValidarNumeros(valor)):
            if (self.val.ValidarEntradas(valor)):
                # Agrega el valor a la lista visual / Add value to visual list
                self.lista.insert(self.lista.size()+1, valor)
                self.dato.delete(0,END)
            else: 
                # Error si no cumple con el límite de dígitos / Error if exceeds digit limit
                messagebox.showerror("Error","Solo se permite dos digitos") 
                self.dato.delete(0,END)  
        else: 
            # Error si no es un número / Error if not numeric
            messagebox.showerror("Error","No son numeros")
            self.dato.delete(0,END)

        # Actualiza el contador de elementos / Update element counter
        self.label.config(text=f'Elementos en la lista: {str(self.lista.size())}')

    def eliminarDato(self):
        # Verifica si la lista está vacía / Check if list is empty
        if self.lista.size() <= 0:
            messagebox.showerror("Error","La lista esta vacia")
            return
        
        # Elimina según el modo seleccionado (Pila o Cola) / Delete according to mode (Stack or Queue)
        if self.modo.get() == 'Pilas':
            # Último que entra, primero que sale (LIFO) / Last in, first out
            self.lista.delete(self.lista.size()-1)
        else:
            # Primero que entra, primero que sale (FIFO) / First in, first out
            self.lista.delete(0)
        
        # Actualiza contador de elementos / Update counter
        self.label.config(text=f'Elementos en la lista: {str(self.lista.size())}')

    def ordenar(self):
        # Obtiene todos los elementos de la lista / Get all elements from list
        self.lis = list(self.lista.get(0,END))
        
        # Verifica si la lista está vacía / Check if list is empty
        if len(self.lista) <= 0:
            messagebox.showerror("Error", "Lista Vacia")
        else:
            # Algoritmo de ordenamiento burbuja / Bubble sort algorithm
            for i in range(0, len(self.lis)):
                for x in range(0, len(self.lis)-1):
                    if self.lis[x] > self.lis[x+1]:
                        aux = self.lis[x]
                        self.lis[x] = self.lis[x+1]
                        self.lis[x+1] = aux

            # Muestra la lista ordenada en consola / Show sorted list in console
            print(self.lis)

            # Limpia y actualiza la lista visual / Clear and update visual list
            self.lista.delete(0,END)
            for i in self.lis:
                self.lista.insert(self.lista.size()+1, i)

            # Código comentado de ordenamiento por selección (alternativo)
            '''
            # SELECCION / SELECTION SORT
            p = 0
            for i in range(0, len(self.lis)):
                aux = int(self.lis[i])
                p = i
                for x in range(i, len(self.lis)):
                    if aux < int(self.lis[x]):
                        aux = int(self.lis[x])
                        p = x
                self.lis[p] = self.lis[i]
                self.lis[i] = str(aux)
            print(self.lis)
            self.lista.delete(0,END)
            for i in self.lis:
                self.lista.insert(self.lista.size()+1, str(i))
            '''

    def inicio(self):
        # Caja de texto para ingresar números / Entry box to input numbers
        self.dato = Entry(self.ven)
        self.dato.place(x=50, y=10)

        # Radio buttons para seleccionar modo (Pilas o Colas) / Radio buttons to select mode
        self.modo = StringVar(value="Pilas")
        Radiobutton(self.ven, text="Pilas", variable=self.modo, value="Pilas").place(x=50, y=40)
        Radiobutton(self.ven, text="Colas", variable=self.modo, value="Colas").place(x=100, y=40)
        
        # Botones principales / Main buttons
        Button(self.ven, text="Validar", command=self.validarCaja, width=10).place(x=100, y=100)
        Button(self.ven, text="Eliminar", command=self.eliminarDato, width=10).place(x=100, y=130)
        Button(self.ven, text="Ordenar", command=self.ordenar, width=10).place(x=100, y=160)

        # Etiqueta que muestra cantidad de elementos / Label showing number of elements
        self.label = Label(text="Numero")
        self.label.place(x=5, y=70)

        # Listbox para mostrar los datos / Listbox to display data
        self.lista= Listbox(self.ven, height=10, width=10, bg="white", font=("Helvetica",12))
        self.lista.place(x=190, y=10)

        # Inicia la ventana principal / Start main window loop
        self.ven.mainloop()

if __name__ == '__main__':
    app = Principal()
    app.inicio()