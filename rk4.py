#codigo runge kutta
import matplotlib.pyplot as plt
import numpy as np
import math
#tasa de cambio de la sal en el agua (sal = entra - sale)
#ecuacion diferencial a reolver
f="6-(x/25)"
#cantidad de sal inical
#condicion inicial cuando la variable independiente es 0
x=75
#intervalos de 5 min
h=5
#el tiempo al que queremos saber el valor de la sal en el agua
b=60
i=0
while i<b:
    xk1=x
    k1=eval(f, {"x": xk1})
    xk2=x+((1/2)*k1*h)
    k2=eval(f, {"x": xk2})
    xk3=x+(1/2)*k2*h
    k3=eval(f, {"x": xk3})
    xk4=x+(1/2)*k3*h
    k4=eval(f, {"x": xk4})
    x=x+(1/6)*h*(k1+2*k2+2*k3+k4)
    i+=h
print(x)
