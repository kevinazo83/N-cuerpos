"""
@author: Keven
"""
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


class Raiz (Tk): #raiz principal
    def __init__(self):
        
        super().__init__()                              #llama la clase tkinter y la inicia
        self.geometry("1280x720")                       #tamaño de la ventana
        self.title("Problema n-cuerpos")                #titulo de la ventana
        self.iconbitmap("sol.ico")                      #icono de la ventana
        self.config(relief="sunken",cursor="trek")      #borde y cursor
        self.inicio()                                   #inicia los widgets de la ventana
    
    def inicio(self): #titulo principal
        
        self.titulo=Label(self,text="Simulador de n-cuerpos")   # Crea el titulo principal
        self.titulo.pack()                                      # Muestra el titulo en pantalla
        self.titulo.config(font=("Funsized",32),pady=20)        # Configura el tamaño y la fuente de la letra
        
class MainFrame(Frame): #Frame principal
    def __init__(self,contenedor):
        
        super().__init__(contenedor)                        #llama la clase tkinter y la inicia
        self.Etiqueta(2,2,"ingrese el numero de cuerpos")   # Grafica las etiquetas
        self.Entrada(2,3)                                   # Declara las variables de entrada y sus respectivas entradas                    
        self.Boton(2,4,"Ok")                                # Grafica botones
        self.pack()                                         # Muestra en pantalla     
        
    def Etiqueta(self,f,c,Texto_label):     
        
        # etiqueta 
        self.label = ttk.Label(self, text=Texto_label).grid(row=f,column=c,padx=5)
        
    def Entrada(self,f,c):
       
        self.n=StringVar()                                                            # Variable Entrada
        self.N=Entry(self,textvariable=self.n,justify=CENTER).grid(row=f,column=c)    # Caja que permite ingresar la variable 

    def Boton(self,f,c,Texto_boton):
        
        #Estilo del boton
        
        self.style = ttk.Style(self)
        self.style.theme_use('alt') 
        self.style.configure('TButton', background = '#9C9C9C', 
                             foreground = 'white', width = 20, 
                             borderwidth=1, focusthickness=3, focuscolor='none')
        self.style.map('TButton', background=[('active','#757575')])
        
        # Botón ok
        
        self.boton = ttk.Button(self, text=Texto_boton)  # Boton ok
        self.boton['command'] = self.Nueva_ventana       # Comando del boton
        self.boton.grid(row=f,column=c,padx=5)           # Ubica el boton en pantalla   
        self.boton.bind("<Return>",self.Nueva_ventana)   # permite usar el boton con enter
        
    def Nueva_ventana(self,event=None): #funcion que llama a la ventana emergente para ingresar los datos
        
        new_frame=Ingreso_datos()
        new_frame.grab_set()
                
class Ingreso_datos(Toplevel):   #ventana donde se ingresan los datos
    def __init__(self):
        super().__init__()
        
        self.title("Datos")         # Titulo de la ventana
        self.iconbitmap("sol.ico")  # Icono de la ventana
        self.entradas()             # Llama a la funcion que muestra los widgets 
        self.Botones()              # Llama a la función que muestra los botones
    
    def entradas(self):      
        #etiquetas de datos
        
        self.label_masa=self.Etiqueta(0,0,"Masa:")
        self.label_posicion=self.Etiqueta(1,0,"Posición:")
        self.label_velocidad=self.Etiqueta(2,0,"Velocidad")
        
        #variables de entrada de datos
        
        self.masa=StringVar()
        self.posicion=StringVar()
        self.velocidad=StringVar()
        
        #cajas de texto donde  se ingresan los datos
        
        self.MASA=Entry(self,textvariable=self.masa,justify=CENTER).grid(row=0,column=1,pady=5,padx=5)
        self.POSICION=Entry(self,textvariable=self.posicion,justify=CENTER).grid(row=1,column=1,pady=5,padx=5)
        self.VELOCIDAD=Entry(self,textvariable=self.velocidad,justify=CENTER).grid(row=2,column=1,pady=5,padx=5)
    
    def Etiqueta(self,f,c,Texto_label): # etiquetas    
    
        self.label = ttk.Label(self, text=Texto_label).grid(row=f,column=c,padx=5) #Escribe en pantalla y el .grid ubica el texto
        
    def Botones(self):
        f=3 #filas 
        c=0 #Columnas
        
        self.boton_guardar = ttk.Button(self, text="Guardar")        # Botón guardar
        self.boton_guardar['command'] = self.Guardar                 # comando que ejecuta el boton al presionarlo
        self.boton_guardar.grid(row=f,column=c,padx=5,pady=(0,5))    # graficar el boton en la posición 
        self.boton_guardar.bind("<Return>")                          # el comando se ejecuta al presionar enter   
       
        self.boton_guardar = ttk.Button(self, text="Salir")          # Botón Salir
        self.boton_guardar['command'] = self.Salir()                 # comando que ejecuta el boton al presionarlo
        self.boton_guardar.grid(row=f,column=c+1,padx=5,pady=(0,5))  # graficar el boton en la posición 
        
        
    def Salir(self):
            pass
        
    
    def Guardar(self):
      
        # obtener los datos de las variables StringVar()    
        
        masa=self.masa.get()            
        velocidad=self.velocidad.get()
        posicion=self.posicion.get()
        #print(masa,"\t",velocidad,"\t", posicion)
        
        #escribir las variables en un archivo txt
        
        with open("datos.txt","a") as datos:
            datos.write(masa)
            datos.write(",")
            datos.write(posicion)
            datos.write(",")
            datos.write(velocidad)
            datos.write("\n")
        
        
        
        
        
def main():
    app=Raiz()                 # Raiz principal del programa
    mainframe=MainFrame(app)   # Frame principal del programa 
    app.mainloop()             # Bucle del programa 
    return 0

if __name__=="__main__":       #Hace que solo se pueda ejecutar el programa solo si se llama directamente y no desde otro código
    main()   
    
