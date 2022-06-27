"""
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

color="#F3F3F3"
D=np.genfromtxt("datos.txt")

class Raiz (Tk): #raiz principal
    def __init__(self):
        
        super().__init__()                                      #llama la clase tkinter y la inicia
        self.geometry("1280x720")                               #tamaño de la ventana
        self.title("Problema n-cuerpos")                        #titulo de la ventana
        self.iconbitmap("sol.ico")                              #icono de la ventana
        self.config(relief="sunken",cursor="trek",bg=color)     #borde y cursor
        self.inicio()                                           #inicia los widgets de la ventana
    
    def inicio(self): #titulo principal
        
        self.titulo=Label(self,text="Simulador de n-cuerpos")   # Crea el titulo principal
        self.titulo.pack()                                      # Muestra el titulo en pantalla
        self.titulo.config(font=("Funsized",32),pady=20,bg=color)        # Configura el tamaño y la fuente de la letra
        
class MainFrame(Frame): #Frame principal
    def __init__(self,contenedor):
        
        super().__init__(contenedor)                         #llama la clase tkinter y la inicia
        self.M = 10000 #Numero de datos para cada cuerpo
        self.C = 9 #Numero de cuerpos
        self.tt = 300 #dts que se grafican
        self.config(bg=color)
                                               
        self.Boton(3,2,"Personalizar",1)        
        self.Boton(3,3,"Iniciar simulacion",2)  
        self.Boton(3,4,"pausar",3)                           # Grafica botones
        self.pack(side="top")                                # Muestra en pantalla     
        self.fig=plt.figure() #figsize=(12,12)
        self.ax=self.fig.add_subplot(111,projection='3d')
        self.size=400
        self.min_display_size = 10
        self.display_log_base = 1.3
        plt.rcParams['axes.facecolor'] = color
        plt.rcParams['figure.figsize'] = (9,8)
        self.canvas= FigureCanvasTkAgg(self.fig,master=self)
        self.canvas.get_tk_widget().grid(row=2,column=2,columnspan=3)
        self.fig.patch.set_facecolor(color)
        self.Crear_planetas()
        
        
        
    def Etiqueta(self,f,c,Texto_label):     
        
        # Grafica las etiquetas 
        self.label = ttk.Label(self, text=Texto_label).grid(row=f,column=c,padx=5)
        
   
    def Boton(self,f,c,Texto_boton,command):
        
        #Estilo del boton
        
        self.style = ttk.Style(self)
        self.style.theme_use('alt') 
        self.style.configure('TButton', background = '#9C9C9C', 
                             foreground = 'white', width = 20, 
                             borderwidth=1, focusthickness=3, focuscolor='white')
        self.style.map('TButton', background=[('active','#757575')])
        
        # Botón ok
        
        self.boton = ttk.Button(self, text=Texto_boton)  # Boton ok
        self.boton.grid(row=f,column=c,padx=5)           # Ubica el boton en pantalla   
        
        # Comando de los botonones
        if command==1:
            self.boton['command'] = self.Nueva_ventana
            self.boton.bind("<Return>",self.Nueva_ventana)  # permite usar el boton con enter            
        elif command==2:
            self.boton["command"] = self.reanudar
            self.boton.bind("<Return>",self.reanudar)  # permite usar el boton con enter
        elif command==3:
            self.boton["command"] = self.pausa
            self.boton.bind("<Return>",self.pausa)  # permite usar el boton con enter
            
    def animacion(self):
        
        self.ani=animation.FuncAnimation(self.fig,self.actualizar,range(self.M),interval=0.0000001,repeat=True)
        self.canvas.draw()
    
    def Crear_planetas(self):
        
        self.Ds = np.empty(self.M*3,dtype=float)
        self.Dm = np.empty(self.M*3,dtype=float)
        self.Dv = np.empty(self.M*3,dtype=float)
        self.Dt = np.empty(self.M*3,dtype=float)
        self.Dma = np.empty(self.M*3,dtype=float)
        self.Dj = np.empty(self.M*3,dtype=float)
        self.Dsa = np.empty(self.M*3,dtype=float)
        self.Du = np.empty(self.M*3,dtype=float)
        self.Dn = np.empty(self.M*3,dtype=float)
        self.Pasar_datos()
    
    def Pasar_datos(self):
        for i in range(self.M):
        	for j in range(3):
        		self.Ds[3*i+j] = D[i*self.C,j]
        		self.Dm[3*i+j] = D[i*self.C+1,j]
        		self.Dv[3*i+j] = D[i*self.C+2,j]
        		self.Dt[3*i+j] = D[i*self.C+3,j]
        		self.Dma[3*i+j] = D[i*self.C+4,j]
        		self.Dj[3*i+j] = D[i*self.C+5,j]
        		self.Dsa[3*i+j] = D[i*self.C+6,j]
        		self.Du[3*i+j] = D[i*self.C+7,j]
        		self.Dn[3*i+j] = D[i*self.C+8,j]
        self.cambiar_tamaño()
        
    def cambiar_tamaño(self):    
        self.Ds = np.reshape(self.Ds,(self.M,3))
        self.Dm = np.reshape(self.Dm,(self.M,3))
        self.Dv = np.reshape(self.Dv,(self.M,3))
        self.Dt = np.reshape(self.Dt,(self.M,3))
        self.Dma = np.reshape(self.Dma,(self.M,3))
        self.Dj = np.reshape(self.Dj,(self.M,3))
        self.Dsa = np.reshape(self.Dsa,(self.M,3))
        self.Du = np.reshape(self.Du,(self.M,3))
        self.Dn = np.reshape(self.Dn,(self.M,3))
        self.animacion()
    
    def actualizar(self,i):  
       self.ax.clear()
       plt.title('tiempo='+str(int(i*0.1))+'meses')
       plt.xlim(min(self.Dsa[:,0]),max(self.Dsa[:,0]))
       plt.ylim(min(self.Dsa[:,1]),max(self.Dsa[:,1]))
    
       self.ax.scatter(self.Ds[i][0],self.Ds[i][1],self.Ds[i][2],s=max(2000*math.exp(-max(self.Dsa[:,0])/2),2),c='#F4D03F')
    
       self.ax.plot3D(self.Dm[:50,0],self.Dm[:50,1],self.Dm[:50,2],'gray')
       self.ax.plot3D(self.Dv[:150,0],self.Dv[:150,1],self.Dv[:150,2],'gray')
       self.ax.plot3D(self.Dt[:150,0],self.Dt[:150,1],self.Dt[:150,2],'gray')
       self.ax.plot3D(self.Dma[:250,0],self.Dma[:250,1],self.Dma[:250,2],'gray')
       self.ax.plot3D(self.Dj[:1500,0],self.Dj[:1500,1],self.Dj[:1500,2],'gray')
       self.ax.plot3D(self.Dsa[:4000,0],self.Dsa[:4000,1],self.Dsa[:4000,2],'gray')
       self.ax.plot3D(self.Du[:11000,0],self.Du[:11000,1],self.Du[:11000,2],'gray')
       self.ax.plot3D(self.Dn[:22000,0],self.Dn[:22000,1],self.Dn[:22000,2],'gray')

       self.ax.scatter(self.Dm[i][0],self.Dm[i][1],self.Dm[i][2],s=max(10*math.exp(-max(self.Dsa[:,0])/2),1),c='#C0392B')
       self.ax.scatter(self.Dv[i][0],self.Dv[i][1],self.Dv[i][2],s=max(28*math.exp(-max(self.Dsa[:,0])/2),1),c='#3498DB')
       self.ax.scatter(self.Dt[i][0],self.Dt[i][1],self.Dt[i][2],s=max(32*math.exp(-max(self.Dsa[:,0])/2),1),c='#3498DB')
       self.ax.scatter(self.Dma[i][0],self.Dma[i][1],self.Dma[i][2],s=max(20*math.exp(-max(self.Dsa[:,0])/2),1),c='#B03A2E')
       self.ax.scatter(self.Dj[i][0],self.Dj[i][1],self.Dj[i][2],s=max(217*math.exp(-max(self.Dsa[:,0])/2),1),c='#F5CBA7')
       self.ax.scatter(self.Dsa[i][0],self.Dsa[i][1],self.Dsa[i][2],s=max(155*math.exp(-max(self.Dsa[:,0])/2),1))
       self.ax.scatter(self.Du[i][0],self.Du[i][1],self.Du[i][2],s=max(55*math.exp(-max(self.Dsa[:,0])/2),1))
       self.ax.scatter(self.Dn[i][0],self.Dn[i][1],self.Dn[i][2],s=max(48*math.exp(-max(self.Dsa[:,0])/2),1))
    
    def pausa(self):
        self.ani.event_source.stop()
        
    def reanudar(self):
        self.ani.event_source.start()
        
        
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
        self.label_masa=self.Etiqueta(1,0,"Masa:")
        self.label_posicion=self.Etiqueta(2,0,"Posición:")
        self.label_velocidad=self.Etiqueta(3,0,"Velocidad")
        
        #variables de entrada de datos
        self.n=StringVar()  
        self.masa=StringVar()
        self.posicion=StringVar()
        self.velocidad=StringVar()
        
        #cajas de texto donde  se ingresan los datos
        self.N=ttk.Entry(self,textvariable=self.n,justify=CENTER)
        self.N.grid(row=f,column=c,pady=5,padx=5)   
        self.MASA=ttk.Entry(self,textvariable=self.masa,justify=CENTER)
        self.MASA.grid(row=f+1,column=c,pady=5,padx=5)
        self.POSICION=ttk.Entry(self,textvariable=self.posicion,justify=CENTER)
        self.POSICION.grid(row=f+2,column=c,pady=5,padx=5)
        self.VELOCIDAD=ttk.Entry(self,textvariable=self.velocidad,justify=CENTER)
        self.VELOCIDAD.grid(row=f+3,column=c,pady=5,padx=5)
    
    def Etiqueta(self,f,c,Texto_label): # etiquetas    
    
        self.label = ttk.Label(self, text=Texto_label).grid(row=f,column=c,padx=5) #Escribe en pantalla y el .grid ubica el texto
        
    def Botones(self):
        f=4 #filas 
        c=0 #Columnas
        
        self.boton_guardar = ttk.Button(self, text="Guardar")        # Botón guardar
        self.boton_guardar['command'] = self.Guardar                 # comando que ejecuta el boton al presionarlo
        self.boton_guardar.grid(row=f,column=c,padx=5,pady=(0,5))    # graficar el boton en la posición 
        self.boton_guardar.bind("<Return>")                          # el comando se ejecuta al presionar enter   
       
        self.boton_salir = ttk.Button(self, text="Salir")          # Botón Salir
        self.boton_salir['command'] = self.Salir                   # comando que ejecuta el boton al presionarlo
        self.boton_salir.grid(row=f,column=c+1,padx=5,pady=(0,5))  # graficar el boton en la posición 
        self.boton_guardar.bind("<Return>")  
        
        
    def Salir(self):
        
        self.destroy()    
        
        
    
    def Guardar(self):
      
        # obtener los datos de las variables StringVar()
        m=self.n.get()
        masa=self.masa.get()            
        velocidad=self.velocidad.get()
        posicion=self.posicion.get()
        print(masa,"\t",velocidad,"\t", posicion, "\t",m)
        
        #escribir las variables en un archivo txt
        
        with open("Entry.txt","a") as datos:
            datos.write(masa)
            datos.write(",")
            datos.write(posicion)
            datos.write(",")
            datos.write(velocidad)
            datos.write("\n")
        self.masa.set("")
        self.velocidad.set("")
        self.posicion.set("")
        self.MASA.focus()
        
        
        
        
def main():
    app=Raiz()                 # Raiz principal del programa
    mainframe=MainFrame(app)   # Frame principal del programa 
    app.mainloop()             # Bucle del programa 
    return 0

if __name__=="__main__":       #Hace que solo se pueda ejecutar el programa solo si se llama directamente y no desde otro código
    main()   
