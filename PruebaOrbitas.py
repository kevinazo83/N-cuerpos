
import numpy as np
import matplotlib.pyplot as plt
import imageio

D = np.genfromtxt("datos.txt")
N = 20000 #Numero de datos para cada cuerpo
C = 9 #Numero de cuerpos
tt = 20000 #dts que se grafican
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
		Du[3*i+j] = D[i*C+8,j]

Ds = np.reshape(Ds,(N,3))
Dm = np.reshape(Dm,(N,3))
Dv = np.reshape(Dv,(N,3))
Dt = np.reshape(Dt,(N,3))
Dma = np.reshape(Dma,(N,3))
Dj = np.reshape(Dj,(N,3))
Dsa = np.reshape(Dsa,(N,3))
Du = np.reshape(Du,(N,3))
Dn = np.reshape(Dn,(N,3))
#print(Ds)

fig, ax = plt.subplots(figsize=(20,20))
ax.scatter(Ds[:tt,0],Ds[:tt,1])
ax.plot(Dm[:tt,0],Dm[:tt,1])
ax.plot(Dv[:tt,0],Dv[:tt,1])
ax.plot(Dt[:tt,0],Dt[:tt,1])
ax.plot(Dma[:tt,0],Dma[:tt,1])
ax.plot(Dj[:tt,0],Dj[:tt,1])
ax.plot(Dsa[:tt,0],Dsa[:tt,1])
ax.plot(Du[:tt,0],Du[:tt,1])
ax.plot(Dn[:tt,0],Dn[:tt,1])

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

plt.savefig("PruebaOrbitas.png")
