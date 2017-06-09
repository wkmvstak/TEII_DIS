import matplotlib.pyplot as plt
import numpy as np
def execGraph(numentradas, listavalores, valorpar,titulo):
    plt.figure("Ejecucion")
    
    it=0
    while it<numentradas:
        plt.subplot(2,2, it+1)
        plt.plot(valorpar[it],listavalores[it])
        it=it+1
    plt.show()
print "Medicion de tiempos de ejecucion para algoritmo de AEDII"
toread=open("input.txt")
array=toread.readlines()
fstline=array[0].split()
tramos=int(fstline[0])
variaciones=int(fstline[1])
numElem=[] #Num de elementos (Eje x)
tiempos=[] #Medicion de tiempos (Eje y)
titletrab=[] #Numero de trabajadores (Titulo)
numtrab=0
numw=0
while i<len(array):
    tempElem = []
    tempTiempo = []
    j=0
    while j<variaciones:
        nums = array[i].split()
        numtrab=int(nums[0])
        numw=int(nums[1])
        i=i+1
        time=int(array[i])
        i=i+1
        tempElem.append(numw)
        tempTiempo.append(time)
        if j==0:
            titletrab.append(numtrab)
        j=j+1
    numElem.append(tempElem)
    tiempos.append(tempTiempo)
execGraph(tramos,tiempos, numElem, titletrab)
print "Cambio sin sentido para hacer rollback"