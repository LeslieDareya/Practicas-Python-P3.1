# buebuja y seleccion de ordenamiento conceptos
#agregar 2 radio buton arriba de ordenar abajo de radio button eliminar y 
from tkinter import *
from tkinter import messagebox
from Validaciones import Validar
import numpy as np

class Principal():
    def __init__(self):
        self.val = Validar()
        # ejecuto el método que ya definiste para inicializar 'con' (no modifiqué Validar)
        self.ven = Tk()
       # self.ven.geometry("350x200")
        ancho = 320
        alto = 210
        ventana_alto = self.ven.winfo_screenwidth()
        ventana_ancho = self.ven.winfo_screenheight()
        x = (ventana_alto // 2) - (ancho // 2)
        y = (ventana_ancho // 2) - (alto // 2)
        self.ven.geometry(f'{ancho}x{alto}+{x}+{y-100}')
        

    
       
        self.lis = []

    def validarCaja(self):
        valor = self.dato.get()
        
        if (self.val.ValidarNumeros(valor)):
            if (self.val.ValidarEntradas(valor)):
                self.lista.insert(self.lista.size()+1, valor)
                self.dato.delete(0,END)
            else: 
                messagebox.showerror("Error","Solo se permite dos digitos") 
                self.dato.delete(0,END)  
        else: 
            messagebox.showerror("Error","No son numeros")
            self.dato.delete(0,END)

        #print(f'La cadena tiene {str(self.val.ValidarEntradas(valor))}')
        #self.label.config(text=str(self.val.ValidarEntradas(valor)))
        self.label.config(text=f'Elementos en la lista: {str(self.lista.size())}')

    def eliminarDato(self):
        if self.lista.size() <= 0:
            messagebox.showerror("Error","La lista esta vacia")
            return
        if self.modo.get() == 'Pilas':
            #Ultimo que entra, primero que sale
            self.lista.delete(self.lista.size()-1)
        else:
            #Primero que entra, primero que sale
            self.lista.delete(0)
        self.label.config(text=f'Elementos en la lista: {str(self.lista.size())}')

    def ordenar(self):
        self.lis = list(self.lista.get(0,END))
        if len(self.lista) <= 0:
            messagebox.showerror("Error", "Lista Vacia")
        else:

        #BURBUJA 
         for i in range(0, len(self.lis)):
          for x in range(0, len(self.lis)-1):
           if self.lis[x] > self.lis[x+1]:
             aux = self.lis[x]
             self.lis[x] = self.lis[x+1]
             self.lis[x+1] = aux

         print(self.lis)
         self.lista.delete(0,END)
        for i in self.lis:
                 self.lista.insert(self.lista.size()+1, i)

         












            #self.arreglo = np.array(self.lis)
            #for i in self.arreglo:
            #  print(i)
        '''     p = 0
               for i in range(0, len(self.lis)):
                    aux = int(self.lis[i])
                    p = i
                    for x in range(i,len(self.list)):
                    # print(self.lis[x])
                     if aux < int(self.lis[x]):
                        aux = int(self.lis[x])
                        p = x
                    self.lis[p] = self.lis[i]
                    self.lis[i] = str(aux)
                print(self.lis)
                self.lista.delete(0,END)
                for i in self.lis:
                 self.lista.insert(self.lista.size()+1, str(i))'''

        #SELECCION
        

    def inicio(self):
        self.dato = Entry(self.ven)
        self.dato.place(x=50, y=10)

        self.modo = StringVar(value="Pilas")
        Radiobutton(self.ven, text="Pilas", variable=self.modo, value="Pilas").place(x=50, y=40)
        Radiobutton(self.ven, text="Colas", variable=self.modo, value="Colas").place(x=100, y=40)
        

        Button(self.ven, text="Validar", command=self.validarCaja, width=10).place(x=100, y=100)
        Button(self.ven, text="Eliminar", command=self.eliminarDato, width=10).place(x=100, y=130)
        Button(self.ven, text="Ordenar", command=self.ordenar, width=10).place(x=100, y=160)

        self.label = Label(text="Numero")
        self.label.place(x=5, y=70)
        self.lista= Listbox(self.ven, height=10, width=10, bg="white", font=("Helvetica",12))
        self.lista.place(x=190, y=10)

        self.ven.mainloop()

if __name__ == '__main__':
    app = Principal()
    app.inicio()
   