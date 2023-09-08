import numpy as np
import matplotlib.pyplot as plt

x0=0
t0=0
vel0=0
a=1

pinput= input( "\n \n bienvenido a la graficadora de movimiento uniformemente acelerado \n ¿desea introducir sus valores? (s/n) \n En caso negativo se utilizaran condiciones inciales iguales a 0 (y aceleracion igual a 1)")

if pinput=="s":
    px0=input ("introduzca x0: ")
    xo=float(px0)
    pt0=input ("introduzca t0: ")
    t0=float(pt0)
    pvel0=input ("introduzca vel0: ")
    vel0=float(pvel0)
    pa=input("introduca a: ")
    a=float(pa)
    

x=[]
t=[]
vel=[]

for ti in range(1,21):
    t.append(ti)
    xi=x0+vel0*ti + 0.5*a*ti**2
    x.append(xi)
    
    
print("x:", x)
print("t:", t)
plt.scatter(t,x)
plt.plot(t,x)
plt.yticks(range(0,int(xi),10),fontsize=8) #cuantos marcas en el eje queremos desde 0 a xn con uan cada 5 unidades
plt.xticks(range(0,21,1),fontsize=8) 
plt.ylabel("distancia (m)", fontsize=8)
plt.xlabel("tiempo (s)", fontsize=8)
plt.grid()
plt.show()
