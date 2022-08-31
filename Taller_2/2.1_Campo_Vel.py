# -*- coding: utf-8 -*-
"""
1. Calcular el campo de velocidades cerca 
de la superficie de un cilindro de radio R = 2 cm.
"""
import numpy as np
"""
a) Definir una discretización en 
los ejes x e y, donde la región es: A ∈ [−4, 4] 
con 25 puntos en
cada eje
"""
xi,xf,N=-4,4,25
x=np.linspace(xi,xf,N)
y=x.copy()
#print(x[-1])
"""
b) Definir la funci´on potencial del flujo
"""
V= 2
R= 2
def fun_pot_flu(V,x,y,R):
    f= V*x*(1-(R**2)/((x**2)+(y**2)))
    return f
"""
c) Calcule y guarde adecuadamente 
el campo de velocidades usando 
la definición de derivada
parcial central:
    
    vx =∂φ
        ∂x
vy = −∂φ
      ∂y
"""
h=0.001
def calc_der_c_x(x,y,h:float):
    der_c_x=(fun_pot_flu(V,x+h,y,R)-fun_pot_flu(V,x-h,y,R))/(2*h)
    #print(x,h,der_c)
    #print(funcion(x+h),funcion(x-h))
    return der_c_x

def calc_der_c_y(x,y,h:float):
    der_c_y=(fun_pot_flu(V,x,y+h,R)-fun_pot_flu(V,x,y-h,R))/(2*h)
    #print(x,h,der_c)
    #print(funcion(x+h),funcion(x-h))
    return -1*der_c_y

def campo_vel():
    Cfx= np.zeros((N,N))
    Cfy = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            if ((x[j])**2 + (y[i])**2 >= R**2 ):
                Cfx[i,j],Cfy[i,j]=calc_der_c_x(x[j],y[i],h),calc_der_c_y(x[j],y[i],h)
    
    return Cfx,Cfy
"""
d) Dibuje el campo de velocidades 
    usando el método: ax.quiver(x[i],y[j],Vx[i,j],Vy[i,j])
"""
Cfx,Cfy= campo_vel()
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(4,4))
ax= fig.add_subplot(1,1,1)
for i in range(N):
    for j in range(N):
        ax.quiver(x[i],y[j],Cfx[i,j],Cfy[i,j],color="b")

theta=np.linspace(0,2*np.pi,50)
coor_x=np.zeros(50)
coor_y=coor_x.copy()
coor_x[:]=R*np.cos(theta)
coor_y[:]=R*np.sin(theta)

ax.plot(coor_x,coor_y,color="r")

