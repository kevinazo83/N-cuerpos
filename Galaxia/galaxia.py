import numpy as np
cantidad = int(input("Escriba el número de planetas que desea graficar(de 10 a 100): "))


lista=np.ones((10,14))    #lista de los datos iniciales, los tenemos por defecto
c=cantidad+1            #numero de planetas a graficar



lista=np.zeros((c+1,14))
lista[c][-1]=c
for i in range(c):
    lista[i][0]=np.random.uniform(10, 200)
    lista[i][1]=np.random.uniform(-100,100)
    lista[i][2]=np.random.uniform(-100,100)
    lista[i][3]=np.random.uniform(-100,100)
    lista[i][4]=np.random.uniform(-5,5)
    lista[i][5]=np.random.uniform(-5,5)
    lista[i][6]=np.random.uniform(-5,5)
    lista[i][-1]=0.5


f = open('entrada.txt','w')
#escribe los datos de los planetas sobre el archivo
for i in range(c+1):
    for k in range(14):
      f.write(str(lista[i][k])+"\t\t")
    f.write("\n")
#escribe el numero de planetas, dts, tamaño de la grafica en el archivo
f.close()
