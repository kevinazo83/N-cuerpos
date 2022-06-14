"""
Created on Mon Jun 13 14:50:39 2022

@author: Keven
"""
from tkinter import *
#from tkinter import ttk

# raiz principal
raiz=Tk()
raiz.title("Problema de n-cuerpos")
raiz.iconbitmap("sol.ico")
raiz.geometry("1280x720")
raiz.config(bd=10,relief="ridge",cursor="trek")
#raiz.config(bg="#E4E4E4")

#titulo principal
titulo=Label(raiz,text="Simulador de n-cuerpos")
titulo.pack()
titulo.config(font=("Funsized",32))

#frame principal
mainframe=Frame(raiz,width=1280,height=720)
mainframe.pack(anchor=CENTER)

#configurar la malla "grid"
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
#Entradas
N=Entry(mainframe)
N.grid(row=1,column=2)

cuerpo1=Entry(mainframe)
cuerpo1.grid(row=2,column=2)

cuerpo2=Entry(mainframe)
cuerpo2.grid(row=3,column=2,sticky="w")

cuerpo3=Entry(mainframe)
cuerpo3.grid(row=4,column=2)

#labels de las entradas
label_N=Label(mainframe,text="Número de cuerpos:")
label_N.grid(row=1,column=1)

label_cuerpo1=Label(mainframe,text="cuerpo 1:")
label_cuerpo1.grid(row=2,column=1,sticky="e")

label_cuerpo2=Label(mainframe,text="cuerpo 2:")
label_cuerpo2.grid(row=3,column=1,sticky="e")

label_cuerpo3=Label(mainframe,text="cuerpo 3:")
label_cuerpo3.grid(row=4,column=1,sticky="e")

# loop principal 
raiz.mainloop()
