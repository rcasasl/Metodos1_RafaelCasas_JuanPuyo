# -*- coding: utf-8 -*-
"""
Implemente este algoritmo para 
calcular la derivada de la funci´on del punto 2)
"""
import numpy as np
import matplotlib.pyplot as plt
xi,xf,h=-9.9,9.9,0.05
N=int((xf-xi)/h)
x= np.linspace(xi,xf,N)
e=np.e
funcion = lambda x: 1/(np.sqrt(1+((e)**(-(x)**2))))
val_der= np.zeros(N)
M=[1,-2,1]
def OperadorD(x,h):
    deriv= (M[0]*funcion(x+2*h)+M[1]*funcion(x)+M[2]*funcion(x-2*h))/(4*(h)**2)
    return deriv
val_der[:]=OperadorD(x,h)
#print(val_der)
plt.plot(x,val_der)
plt.show()

