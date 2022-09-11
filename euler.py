import math

y=4
x=2
dydx="(2/5)*(x**2)+(1/10)*math.sqrt(y)"


def euler(f,y,x,n):
    h=(2.5-2)/n
    i=0
    while i < n:
        y=y+h*(eval(f))
        x=x+h
        i+=1
    print(y)
    return y

x=euler(dydx,y,x,10)
y=euler(dydx,y,x,15)

print("con 10 particiones es: ", x, "y con 15 es: ", y)

#para obtener el error porcentual, divides la aproximacion con 15 entre el de la aproximacion con 10
#y lo multiplicas por 100, si es menor a 1, se esta acercando al valor real, de lo contrario, se aleja.
