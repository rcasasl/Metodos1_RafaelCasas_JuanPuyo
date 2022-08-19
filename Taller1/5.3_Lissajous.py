# -*- coding: utf-8 -*-
"""
5.3 Gráficar figuras de lissajous para los 
angulos de desfase correspondientes.

x= Asin(wxt)
y= Asin(wyt + delta)
"""
import matplotlib.pyplot as plt
import math as mt



n_s=5
val_des=[0,(mt.pi)/4,(mt.pi)/2]
def figuras_lissa(delta:float)->None:
    nx=1
    ny=1
    k=1
    for i in range(1,6):
        ny = i
        for o in range(1,ny+1):
            val_x=[]
            val_y=[]
            theta=0
            nx = o
            while theta <= 2*(mt.pi):
                x= mt.sin(nx*theta)
                y= mt.sin(ny*theta+delta)
                val_x.append(x)
                val_y.append(y)
                theta += 0.001
            
            plt.subplot(n_s,n_s,k)
            plt.plot(val_x,val_y)
            plt.axis("off")
            k += 1
    plt.show()
figuras_lissa(val_des[0])
figuras_lissa(val_des[1])
figuras_lissa(val_des[2])
