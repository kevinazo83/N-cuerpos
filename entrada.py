import numpy as np

lista=np.ones((10,14))    #lista de los datos iniciales, los tenemos por defecto
p=9                #numero de planetas a graficar
av=0.05         #celovidad a la que se agranda la grafica
t=1                #tamaño de la grafica inicial o por defecto

#sol
M = 332959;
V = 0;
X = 0;
dt= 0.01
lista[0]=(M,X,0,0,0,V,0,0,0,0,0,0,0,dt);

#	//Mercurio
M = 0.0553;
V = 1.036156924;
X = 0.3074916;
dt=0.01
lista[1]=(M,X,0,0,0,V,0,0,0,0,0,0,0,dt);

#	//Venus
M = 0.815;
V = -0.6152291537;
X = -0.6194454586;
dt=0.01
lista[2]=(M,X,0,0,0,V,0,0,0,0,0,0,0,dt);

#	//Tierra
M = 1;
V = 0.5321328117;
X = 0.983271237;
dt=0.01
lista[3]=(M,X,0,0,0,V,0,0,0,0,0,0,0,dt);

#	//Marte
M = 0.1074;
V = -0.4655503305;
X = -1.38137259;
dt=0.01
lista[4]=(M,X,0,0,0,V,0,0,0,0,0,0,0,dt);

#	//Jupiter
M = 317.833;
V = 0.2410320956;
X = 4.950581337;
dt=0.1
lista[5]=(M,X,0,0,0,V,0,0,0,0,0,0,0,dt);

#	//Saturno
M = 95.152;
V = -0.1788415987;
X = -9.074705468;
dt=0.1
lista[6]=(M,X,0,0,0,V,0,0,0,0,0,0,0,dt);

#	//Urano
M = 14.536;
V = 0.1249080321;
X = 18.26697968;
dt=0.1
lista[7]=(M,X,0,0,0,V,0,0,0,0,0,0,0,dt);

#	//Neptuno
M = 17.147;
V = -0.0966236535;
X = -29.88718083;
dt=0.2
lista[8]=(M,X,0,0,0,V,0,0,0,0,0,0,0,dt);
#fila que contiene el numero de cuerpos, tamaño grafica, vel de alejamiento grafica, y dt de cada PLANETA
lista[9]=(p,p,p,p,p,p,p,p,p,p,p,t,av,p);

#abre archivo en modo escritura
f = open('entrada.txt','w')
#escribe los datos de los planetas sobre el archivo
for i in range(p):
    for k in range(14):
      f.write(str(lista[i][k])+"\t\t")
    f.write("\n")
#escribe el numero de planetas, dts, tamaño de la grafica en el archivo
for k in range (14):
     f.write(str(lista[9][k])+"\t\t")
f.write("\n")
f.close()
