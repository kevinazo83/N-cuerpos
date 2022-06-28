"""
Created on Sun Jun 19 13:27:12 2022

@author: Keven
"""
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation
import math
import Entrada

color="#F3F3F3"
D = np.genfromtxt("datos.txt")
G=np.genfromtxt('entrada.txt')

class Raiz (Tk): #raiz principal
    def __init__(self):
        
        super().__init__()                                      #llama la clase tkinter y la inicia
        self.geometry("1280x720")                               #tamaño de la ventana
        self.title("Problema n-cuerpos")                        #titulo de la ventana
        self.iconbitmap("sol.ico")                              #icono de la ventana
        self.config(relief="sunken",cursor="trek",bg=color)     #borde y cursor
        self.inicio()                                           #inicia los widgets de la ventana
    
    def inicio(self): #titulo principal
        
        self.titulo=Label(self,text="Simulador de n-cuerpos")            # Crea el titulo principal
        self.titulo.pack()                                               # Muestra el titulo en pantalla
        self.titulo.config(font=("Funsized",32),pady=20,bg=color)        # Configura el tamaño y la fuente de la letra
        
class MainFrame(Frame): #Frame principal
    def __init__(self,contenedor):
        
        super().__init__(contenedor)                         #llama la clase tkinter y la inicia
        self.config(bg=color)                                        
        self.Boton(2,2,"Personalizar",1)        
        self.Boton(2,3,"Iniciar simulacion",2)  
        self.Boton(2,4,"Parar",3)                           # Grafica botones
        self.Boton(2,5,"Siguiente paso",4)
        self.pack(side="top")                                # Muestra en pantalla     
        self.fig=plt.figure()# dpi=80,figsize=(9,8)
        self.ax=self.fig.add_subplot(111,projection='3d')
        self.ax.axis("off")
        self.M = 20000                              #Numero de datos para cada cuerpo
        self.C = int(G[-1][8])                      #Numero de cuerpos
        self.L = G[-1][12]                          #velocidad a la que se aleja la grafica
        self.Li=G[-1][11]                           #tamaño de la grafica inicial o por defecto
        self.fig.patch.set_facecolor(color)
        self.fig.patch.set_alpha(1)
        #plt.rcParams['axes.facecolor'] = color
        plt.rcParams['figure.figsize'] = (10,9)
        self.canvas= FigureCanvasTkAgg(self.fig,master=self)
        self.canvas.get_tk_widget().grid(row=3,column=2,columnspan=4)
        
        
        
        
    def Etiqueta(self,f,c,Texto_label):     
        
        # Grafica las etiquetas 
        self.label = ttk.Label(self, text=Texto_label).grid(row=f,column=c,padx=5)
        
   
    def Boton(self,f,c,Texto_boton,command):
        
        #Estilo del boton
        
        self.style = ttk.Style(self)
        self.style.theme_use('alt') 
        self.style.configure('TButton', background = '#9C9C9C', 
                             foreground = 'white', width = 20, 
                             borderwidth=1, focusthickness=3,     )
        self.style.map('TButton', background=[('active','#757575')])
        
        # Botón ok
        
        self.boton = ttk.Button(self, text=Texto_boton)  # Boton ok
        self.boton.grid(row=f,column=c,padx=5)           # Ubica el boton en pantalla   
        
        # Comando de los botonones
        if command==1:
            self.boton['command'] = self.Nueva_ventana
            self.boton.bind("<Return>",self.Nueva_ventana)  # permite usar el boton con enter            
        elif command==2:
            self.boton["command"] = self.Iniciar_simulacion
            self.boton.bind("<Return>",self.Iniciar_simulacion)  # permite usar el boton con enter
        elif command==3:
            self.boton["command"] = self.Parar
            self.boton.bind("<Return>",self.Parar)  # permite usar el boton con enter
        elif command==4:
            self.boton["command"] = self.Pasos
            self.boton.bind("<Return>",self.Pasos)  # permite usar el boton con enter
              
    
    def actualizar(self,i):  
       self.ax.clear()                                  #limpia la grafica en cada iteracion
       plt.title('tiempo='+str(int(i*0.2))+'meses')     #escribe el tiempo transcurrido en la grafica
       #escalas de la grafica
       plt.xlim(-(self.lim2+self.lim*i),(self.lim2+self.lim*i))
       plt.ylim(-(self.lim2+self.lim*i),(self.lim2+self.lim*i))
       
       self.ax.axis("off")
       for k in range(self.C):
        #dibuja las orbitas

        self.ax.scatter(self.DD[k,:self.orb[k],0],self.DD[k,:self.orb[k],1],self.DD[k,:self.orb[k],2],marker="x",s=0.1,c='gray')
        if(k==0):
            #dibuja el sol
            self.ax.scatter(self.DD[k][i*10][0],self.DD[k][i*10][1],self.DD[k][i*10][2],s=max(self.t[k]*math.exp(-(self.lim2+self.lim*i)/1.5),1),c=self.co[k])
        elif(k<=5):
            #dibuja los planetas hasta marte
            self.ax.scatter(self.DD[k][i*10][0],self.DD[k][i*10][1],self.DD[k][i*10][2],s=max(self.t[k]*math.exp(-(self.lim2+self.lim*i)/2),1),c=self.co[k])
        else:
            #dibuja los planetas desde jupiter en adelante
            self.ax.scatter(self.DD[k][i*1][0],self.DD[k][i*1][1],self.DD[k][i*1][2],s=max(self.t[k]*math.exp(-(self.lim2+self.lim*i)/2),1),c=self.co[k])
   
        
    def Parar(self):
        try:
            self.ani._stop()
        except:
            pass
    
    def Pasos(self):
        try:
            self.ani._step()
        except:
            pass
        
    def Iniciar_simulacion(self):
        self.DD=np.ones((self.C,self.M,3))

        #separa todos los datos de entrada, en un arreglo para cada cuerpo
        for k in range(self.C):
          self.DD[k,:,:] = D[k::self.C,:]
        
        #volumenes de los planetas cuando estan a una distancia 1
        self.t=[2000,10,28,32,20,217,155,55,48]
        #colores de los planetas
        self.co=['#F4D03F','#C0392B','#3498DB','#3498DB','#B03A2E','#F5CBA7','#F5CBA7','#F5CBA7','#F5CBA7']
        #pasos hasta detenerce para graficar la linea de orbita
        self.orb=[1,550,550,1550,2750,1500,4000,11000,22000]
        
        #posicion inicial camara
        #self.ax.view_init(-140,-20)
        
        
        self.lim=self.L     #pasos a los que se va agrandando la grafica
        self.lim2=self.Li   #tamaño grafica por defecto
        
        self.ani=animation.FuncAnimation(self.fig,self.actualizar,range(self.M),interval=500,repeat=True)
        self.canvas.draw()
        
        
    def Nueva_ventana(self,event=None): #funcion que llama a la ventana emergente para ingresar los datos
      
        new_frame=Ingreso_datos()
        new_frame.grab_set()
                
class Ingreso_datos(Toplevel):   #ventana donde se ingresan los datos
    def __init__(self):
        super().__init__()
        
        self.title("Datos")         # Titulo de la ventana
        self.iconbitmap("sol.ico")  # Icono de la ventana
        self.entradas(0,1)          # Llama a la funcion que muestra los widgets 
        self.Botones()              # Llama a la función que muestra los botones
        #self.MASA.focus()
        self.N.focus()
        
    def entradas(self,f,c):      
        #etiquetas de datos  
        
        self.label_n=self.Etiqueta(0, 0, "Número de cuerpos")
        self.label_masa=self.Etiqueta(1,0,"Alejar animación(0 para no):")
        self.label_posicion=self.Etiqueta(2,0,"Tamaño de la gráfica")
        
        
        #variables de entrada de datos
        self.n=StringVar()  
        self.acercar=StringVar()
        self.tamaño=StringVar()
        
        
        #cajas de texto donde  se ingresan los datos
        self.N=ttk.Entry(self,textvariable=self.n,justify=CENTER)
        self.N.grid(row=f,column=c,pady=5,padx=5)   
        self.ACERCAR=ttk.Entry(self,textvariable=self.acercar,justify=CENTER)
        self.ACERCAR.grid(row=f+1,column=c,pady=5,padx=5)
        self.TAMAÑO=ttk.Entry(self,textvariable=self.tamaño,justify=CENTER)
        self.TAMAÑO.grid(row=f+2,column=c,pady=5,padx=5)
        
    
    def Etiqueta(self,f,c,Texto_label): # etiquetas    
    
        self.label = ttk.Label(self, text=Texto_label).grid(row=f,column=c,padx=5) #Escribe en pantalla y el .grid ubica el texto
        
    def Botones(self):
        f=4 #filas 
        c=0 #Columnas
        
        self.boton_guardar = ttk.Button(self, text="Guardar")        # Botón guardar
        self.boton_guardar['command'] = self.Guardar                 # comando que ejecuta el boton al presionarlo
        self.boton_guardar.grid(row=f,column=c,padx=5,pady=(0,5))    # graficar el boton en la posición 
        self.boton_guardar.bind("<Return>")                          # el comando se ejecuta al presionar enter   
       
        self.boton_cancelar = ttk.Button(self, text="Cancelar")       # Botón cancelar
        self.boton_cancelar['command'] = self.Salir                   # comando que ejecuta el boton al presionarlo
        self.boton_cancelar.grid(row=f,column=c+1,padx=5,pady=(0,5))  # graficar el boton en la posición 
        self.boton_cancelar.bind("<Return>")  
        
        
    def Salir(self):
        
        self.destroy()    
        
        
    
    def Guardar(self):
        
        # obtener los datos de las variables StringVar()
        m=self.n.get()
        acercar=self.acercar.get()            
        tamaño=self.tamaño.get()

        
        #escribir las variables en un archivo txt
        
        with open("N_planetas.txt","w") as datos:
            datos.write(m)
            datos.write(",")
            datos.write(acercar)
            datos.write(",")
            datos.write(tamaño)
            
        Entrada
        self.Salir()
        
        
def main():
    app=Raiz()                 # Raiz principal del programa
    mainframe=MainFrame(app)   # Frame principal del programa 
    app.mainloop()             # Bucle del programa 
    return 0

if __name__=="__main__":       #Hace que solo se pueda ejecutar el programa solo si se llama directamente y no desde otro código
    main()   
