import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import math
#se suben los archivos de entrada, y los datos calculados por c++
D = np.genfromtxt("datos.txt")
G=np.genfromtxt('entrada.txt')
N = 1000 #Numero de datos para cada cuerpo
C = int(G[-1][-1]) #Numero de cuerpos
#L = G[-1][12]     #velocidad a la que se aleja la grafica
#Li=G[-1][11]      #tamaño de la grafica inicial o por defecto
#print(L)

#arreglo que contiene el numero de cuerpos; numero de datos; y numero de ejes
DD=np.ones((C,N,3))

#separa todos los datos de entrada, en un arreglo para cada cuerpo
for k in range(C):
  DD[k,:,:] = D[k::C,:]

#crea la grafica done se dibujara
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
#posicion inicial camara
ax.view_init(-140,-20)
lim=100
def actualizar(i):
 ax.clear()  #limpia la grafica en cada iteracion
 plt.title('tiempo='+str(int(i*0.5))+'meses')     #escribe el tiempo transcurrido en la grafica
 #escalas de la grafica
 plt.xlim(-(lim),(lim))
 plt.ylim(-(lim),(lim))

 for k in range(C):
     ax.scatter(DD[k][i][0],DD[k][i][1],DD[k][i][2],s=G[k][0]/4,c='blue')

ni=animation.FuncAnimation(fig,actualizar,range(N),interval=500,repeat=True)

plt.show()
