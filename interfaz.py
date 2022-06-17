"""
Created on Mon Jun 13 14:50:39 2022

@author: Keven
"""
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


class Raiz (Tk): #raiz principal
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("Problema n-cuerpos")
        self.iconbitmap("sol.ico")
        self.config(bd=10,relief="ridge",cursor="trek")
        self.inicio()
    
    def inicio(self):#titulo principal
        self.titulo=ttk.Label(self,text="Simulador de n-cuerpos")
        self.titulo.pack()
        self.titulo.config(font=("Funsized",32))
        
        
        
        
class MainFrame(Frame):#Frame principal
    def __init__(self,contenedor):
        super().__init__(contenedor)
        # etiqueta de botón ok
        self.label = ttk.Label(self, text="Ingrese el número de cuerpos")
        self.label.grid(row=2,column=2,padx=5)
        #Entrada
        self.n=StringVar()
        self.N=Entry(self,textvariable=self.n).grid(row=2,column=3)
        # Botón ok
        self.boton = ttk.Button(self, text='Ok')
        self.boton['command'] = self.Nueva_ventana
        self.boton.grid(row=2,column=5,padx=5)

        # Mostrar el frame
        self.pack()
        
    def Nueva_ventana(self):
        new_frame=Ingreso_datos()
        new_frame.grab_set()
    
class Ingreso_datos(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Datos")
        self.iconbitmap("sol.ico")
        self.entrada()
    
    def entrada(self):
        #etiquetas de datos
        self.label_masa=ttk.Label(self,text="Masa:")
        self.label_masa.grid(row=0,column=0,padx=5,pady=5,sticky="e")
        self.label_posicion=ttk.Label(self,text="Posición:")
        self.label_posicion.grid(row=1,column=0,padx=5,pady=5,sticky="e")
        self.label_velocidad=ttk.Label(self,text="Velocidad:")
        self.label_velocidad.grid(row=2,column=0,padx=5,pady=5,sticky="e")
        #entrada de datos
        self.masa=StringVar()
        self.MASA=Entry(self,textvariable=self.masa).grid(row=0,column=1,pady=5,padx=5)
        self.posicion=StringVar()
        self.POSICION=Entry(self,textvariable=self.posicion).grid(row=1,column=1,pady=5,padx=5)
        self.velocidad=StringVar()
        self.VELOCIDAD=Entry(self,textvariable=self.velocidad).grid(row=2,column=1,pady=5,padx=5)
        
def main():
    app=Raiz()
    mainframe=MainFrame(app)
    app.mainloop()
    return 0

if __name__=="__main__":
    main()
