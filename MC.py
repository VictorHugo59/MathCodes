
import matplotlib.pyplot as plt
import numpy as np
import math
#PRIMERO PRUEBA CON FUNCION SIMPLE
#function to integrate
funcion="(1/(1+(x**2)))*(1/(1+(x**2)))"
limitxA=-7.5
limitxB=7.5
limityA=0
limityB=1.5
N=50000
#limitxA=float(input("escribe el x minimo: "))
#limitxB=float(input("escribe el x max: "))
#limityA=float(input("escribe el y minimo: "))
#limityB=float(input("escribe el y max: "))
#N=int(input("escribe el numero de puntos: "))





#Tienes que obtener ymin y ymax en base a la funcion,
#por lo que mas adelante no se los pides al usuario
def integracion_MC(f,xmin,xmax,ymin,ymax,N):
    #Generar puntos random
    puntosx=np.random.uniform(low=xmin,high=xmax,size=N)
    puntosy=np.random.uniform(low=ymin,high=ymax,size=N)

    #crear listas vacías para añadir los puntos que sen, y no sean
    puntosDentroX = []
    puntosDentroY = []
    puntosFueraX = []
    puntosFueraY = []

    #evaluar si el punto está dentro de la funcion o no, ojo porque si la
    #funcion tiene area negativa, tienes que considerarla

    for i in range(len(puntosx)):
        x=puntosx[i]
        if puntosy[i]>0:
            if (eval(f) >= puntosy[i]):
                puntosDentroX.append(puntosx[i])
                puntosDentroY.append(puntosy[i])
            else:
                puntosFueraX.append(puntosx[i])
                puntosFueraY.append(puntosy[i])
        else:
            if (eval(f) < puntosy[i]):
                puntosDentroX.append(puntosx[i])
                puntosDentroY.append(puntosy[i])
            else:
                puntosFueraX.append(puntosx[i])
                puntosFueraY.append(puntosy[i])
    #start, stop, step
    #x=np.arange(xmin,xmax,0.1)
    #y=eval(f)

    plt.plot(puntosDentroX, puntosDentroY, ".", color='blue')
    plt.plot(puntosFueraX, puntosFueraY, ".", color='red')
    #plt.plot(x, y)
    plt.show()
    return (((xmax - xmin)*(ymax - ymin)*(len(puntosDentroX))) / N)

print("The area under the curve si approximately: ",integracion_MC(funcion, limitxA, limitxB, limityA, limityB, N))
