import matplotlib.pyplot as plt
import numpy as np
print "Medicion de tiempos de ejecucion para algoritmo de AEDII"
toread=open("input.txt")
array=toread.readlines()
print array
fstline=array[0].split()
tramos=int(fstline[0])
variaciones=int(fstline[1])
numElem=[] #Num de elementos (Eje x)
tiempos=[] #Medicion de tiempos (Eje y)
titletrab=[] #Numero de trabajadores (Titulo)
numtrab=0
numw=0
#Proximamente el while
