# -*- coding: utf-8 -*-
"""
5.2 Espiral de Arquimedes
"""
"""
calcule las posiciones r entre θ ∈ [0., 2π], si a=0 y b=1

r= a + bθ

x=rcos(θ)
y=rsin(θ)
"""
import math as mt
import matplotlib.pyplot as plt
pos_r=[]
r=0
while r <= 2*(mt.pi):
    pos_r.append(r)
    r += 0.0001
#print(pos_r)
coor_x=[]
coor_y=[]
for i in range(0,len(pos_r)):
    coor_x.append(pos_r[i]*mt.cos(pos_r[i]))
    coor_y.append(pos_r[i]*mt.sin(pos_r[i]))
plt.plot(coor_x,coor_y)
plt.show()


