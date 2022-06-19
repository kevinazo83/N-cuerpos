import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

D = np.genfromtxt("datos.txt")
N = 10000 #Numero de datos para cada cuerpo
C = 9 #Numero de cuerpos
tt = 300 #dts que se grafican
Ds = np.empty(N*3,dtype=float)
Dm = np.empty(N*3,dtype=float)
Dv = np.empty(N*3,dtype=float)
Dt = np.empty(N*3,dtype=float)
Dma = np.empty(N*3,dtype=float)
Dj = np.empty(N*3,dtype=float)
Dsa = np.empty(N*3,dtype=float)
Du = np.empty(N*3,dtype=float)
Dn = np.empty(N*3,dtype=float)



for i in range(N):
	for j in range(3):
		Ds[3*i+j] = D[i*C,j]
		Dm[3*i+j] = D[i*C+1,j]
		Dv[3*i+j] = D[i*C+2,j]
		Dt[3*i+j] = D[i*C+3,j]
		Dma[3*i+j] = D[i*C+4,j]
		Dj[3*i+j] = D[i*C+5,j]
		Dsa[3*i+j] = D[i*C+6,j]
		Du[3*i+j] = D[i*C+7,j]
		Dn[3*i+j] = D[i*C+8,j]

Ds = np.reshape(Ds,(N,3))
Dm = np.reshape(Dm,(N,3))
Dv = np.reshape(Dv,(N,3))
Dt = np.reshape(Dt,(N,3))
Dma = np.reshape(Dma,(N,3))
Dj = np.reshape(Dj,(N,3))
Dsa = np.reshape(Dsa,(N,3))
Du = np.reshape(Du,(N,3))
Dn = np.reshape(Dn,(N,3))


#print(Dn)
#print(Ds[2][1])
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
plt.rcParams['axes.facecolor'] = 'm'
def actualizar(i):
 ax.clear()
 ax.scatter(Ds[i][0],Ds[i][1],Ds[i][2],s=800,c='#F4D03F')
 ax.scatter(Dm[i][0],Dm[i][1],Dm[i][2],s=5,c='#C0392B')
 ax.scatter(Dv[i][0],Dv[i][1],Dv[i][2],s=5, c='#717D7E')
 ax.scatter(Dt[i][0],Dt[i][1],Dt[i][2],s=10,c='#3498DB')
 ax.scatter(Dma[i][0],Dma[i][1],Dma[i][2],s=7,c='#B03A2E')
 ax.scatter(Dj[i][0],Dj[i][1],Dj[i][2],s=117,c='#F5CBA7')
 ax.scatter(Dsa[i][0],Dsa[i][1],Dsa[i][2],s=55)
 ax.scatter(Du[i][0],Du[i][1],Du[i][2],s=6)
 ax.scatter(Dn[i][0],Dn[i][1],Dn[i][2],s=6)
 plt.xlim(min(Dma[:,0]),max(Dma[:,0]))
 plt.ylim(min(Dma[:,1]),max(Dma[:,1]))
ani=animation.FuncAnimation(fig,actualizar,range(N),interval=0.0001,repeat=True)
plt.show()
