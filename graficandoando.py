import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import math
#se suben los archivos de entrada, y los datos calculados por c++
D = np.genfromtxt("datos.txt")
G=np.genfromtxt('entrada.txt')
N = 20000 #Numero de datos para cada cuerpo
C = int(G[-1][8]) #Numero de cuerpos
L = G[-1][12]     #velocidad a la que se aleja la grafica
Li=G[-1][11]      #tamaño de la grafica inicial o por defecto
print(L)

#arreglo que contiene el numero de cuerpos; numero de datos; y numero de ejes
DD=np.ones((C,N,3))

#separa todos los datos de entrada, en un arreglo para cada cuerpo
for k in range(C):
  DD[k,:,:] = D[k::C,:]

#volumenes de los planetas cuando estan a una distancia 1
t=[2000,10,28,32,20,217,155,55,48]
#colores de los planetas
co=['#F4D03F','#C0392B','#3498DB','#3498DB','#B03A2E','#F5CBA7','#F5CBA7','#F5CBA7','#F5CBA7']
#pasos hasta detenerce para graficar la linea de orbita
orb=[1,550,550,1550,2750,1500,4000,11000,22000]

#crea la grafica done se dibujara
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
#posicion inicial camara
ax.view_init(-140,-20)

lim=L #pasos a los que se va agrandando la grafica
lim2=Li   #tamaño grafica por defecto
def actualizar(i):
 ax.clear()  #limpia la grafica en cada iteracion
 plt.title('tiempo='+str(int(i*0.2))+'meses')     #escribe el tiempo transcurrido en la grafica
 #escalas de la grafica
 plt.xlim(-(lim2+lim*i),(lim2+lim*i))
 plt.ylim(-(lim2+lim*i),(lim2+lim*i))

 for k in range(C):
  #dibuja las orbitas
  #ax.plot3D(DD[k,:orb[k],0],DD[k,:orb[k],1],DD[k,:orb[k],2],'gray')
  ax.scatter(DD[k,:orb[k],0],DD[k,:orb[k],1],DD[k,:orb[k],2],marker="x",s=0.1,c='gray')
  if(k==0):
     #dibuja el sol
      ax.scatter(DD[k][i*10][0],DD[k][i*10][1],DD[k][i*10][2],s=max(t[k]*math.exp(-(lim2+lim*i)/1.5),1),c=co[k])
  elif(k<=5):
    #dibuja los planetas hasta marte
    ax.scatter(DD[k][i*10][0],DD[k][i*10][1],DD[k][i*10][2],s=max(t[k]*math.exp(-(lim2+lim*i)/2),1),c=co[k])
  else:
    #dibuja los planetas desde jupiter en adelante
    ax.scatter(DD[k][i*1][0],DD[k][i*1][1],DD[k][i*1][2],s=max(t[k]*math.exp(-(lim2+lim*i)/2),1),c=co[k])

ani=animation.FuncAnimation(fig,actualizar,range(N),interval=500,repeat=True)

plt.show()
