import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import math

D = np.genfromtxt("datos.txt")
N = 20000 #Numero de datos para cada cuerpo
C = 9 #Numero de cuerpos
tt = 300 #dts que se grafican
#DD=np.ones(9)
#for k in range(9):
  #  DD[k]=np.empty(N*3,dtype=float)

   # for i in range(N):
#	for j in range(3):
###		DD[3*i+j] = D[i*C+k,j]
#for k in range(9):
 #       DD[k]=np.reshape(DD[k],(N,3))


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

size=400
#print(Dn)
#print(Ds[2][1])
min_display_size = 10
display_log_base = 1.3
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
#ax.view_init(0, 0)
#ax.plot3D(Dt[:][0],Dt[:][1],Dt[:][2],'gray')
#plt.rcParams['axes.facecolor'] = 'm'
#lim=max(Dma[:,0])
lim=0.05  #pasos a los que se va agrandando la grafica
lim2=0.5     #tamaño grafica por defecto
def actualizar(i):
 ax.clear()
 plt.title('tiempo='+str(int(i*0.1))+'meses')

 plt.xlim(-(lim2+lim*i),(lim2+lim*i))
 plt.ylim(-(lim2+lim*i),(lim2+lim*i))

 #for i in range(9):
        #ax.plot3D(DD[i][:50,0],DD[i][:50,1],DD[i][:50,2],'gray')
        #ax.scatter(Ds[i][0],Ds[i][1],Ds[i][2],s=max(2000*math.exp(-max(Dma[:,0])/2),2),c='#F4D03F')


 ax.scatter(Ds[i][0],Ds[i][1],Ds[i][2],s=max(2000*math.exp(lim/2),2),c='#F4D03F')

 ax.scatter(Dm[:550,0],Dm[:550,1],Dm[:550,2],marker="x",s=0.1,c='gray')
 ax.plot3D(Dv[:550,0],Dv[:550,1],Dv[:550,2],'gray')
 ax.plot3D(Dt[:1550,0],Dt[:1550,1],Dt[:1550,2],'gray')
 ax.plot3D(Dma[:2750,0],Dma[:2750,1],Dma[:2750,2],'gray')
 ax.plot3D(Dj[:1500,0],Dj[:1500,1],Dj[:1500,2],'gray')
 ax.plot3D(Dsa[:4000,0],Dsa[:4000,1],Dsa[:4000,2],'gray')
 ax.plot3D(Du[:11000,0],Du[:11000,1],Du[:11000,2],'gray')
 ax.plot3D(Dn[:22000,0],Dn[:22000,1],Dn[:22000,2],'gray')

 #ax.scatter(Ds[i][0],Ds[i][1],Ds[i][2],s=max(2000*math.exp(-lim/2),2),c='#F4D03F')


 ax.scatter(Dm[i][0],Dm[i][1],Dm[i][2],s=max(10*math.exp(-(lim2+lim*i)/2),1),c='#C0392B')
 ax.scatter(Dv[i][0],Dv[i][1],Dv[i][2],s=max(28*math.exp(-(lim2+lim*i)/2),1),c='#3498DB')
 ax.scatter(Dt[i][0],Dt[i][1],Dt[i][2],s=max(32*math.exp(-(lim2+lim*i)/2),1),c='#3498DB')
 ax.scatter(Dma[i][0],Dma[i][1],Dma[i][2],s=max(20*math.exp(-(lim2+lim*i)/2),1),c='#B03A2E')
 ax.scatter(Dj[i][0],Dj[i][1],Dj[i][2],s=max(217*math.exp(-(lim2+lim*i)/2),1),c='#F5CBA7')
 ax.scatter(Dsa[i][0],Dsa[i][1],Dsa[i][2],s=max(155*math.exp(-(lim2+lim*i)/2),1))
 ax.scatter(Du[i][0],Du[i][1],Du[i][2],s=max(55*math.exp(-(lim2+lim*i)/2),1))
 ax.scatter(Dn[i][0],Dn[i][1],Dn[i][2],s=max(48*math.exp(-(lim2+lim*i)/2),1))





ani=animation.FuncAnimation(fig,actualizar,range(N),interval=500,repeat=True)
#lim=lim+0.5
#ani = FuncAnimation(fig, animate, repeat=False, interval=1, frames=len(x)//20)
#ani.save('orbita.gif', writer='imagemagick', fps=30)




#fig = plt.gcf()
plt.show()
#fig.savefig('a.png')
