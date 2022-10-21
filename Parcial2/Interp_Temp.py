# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 17:18:10 2022

@author: Adriana
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:34:38 2022

@author: Adriana
"""

import numpy as np
import sympy as sym
from tqdm import tqdm
import matplotlib.pyplot as plt

X=np.array([1,-1,1,-1])
Y=np.array([1,1,-1,-1])
Z=np.array([[1,2] , [0.3,0.5]]) 


def T(x,y,p):
    return p[0]+p[1]*x+p[2]*y+p[3]*x*y
p0=np.zeros((4,2))
p0[:,0]=X
p0[:,1]=Y


b=np.array([1,2,0.3,0.5])

def GetFit(p,b):
    M=np.ones((4,4))
    M[:,1]=p[:,0]
    M[:,2]=p[:,1]
    M[:,3]=p[:,0]*p[:,1]

    par=np.linalg.solve(M,b)
    return par
par= GetFit(p0,b)
r=T(0,0.5,par)

x=sym.Symbol("x",real="True")
y=sym.Symbol("y",real="True")

g=T(x,y,par)


print("\nModelo: ",g.simplify(),"\nEstimación temperatura: ",r)



f=lambda x,y: T(x,y,par)

x=np.linspace(-1,1,100)
y=np.copy(x)
xx1,yy1=np.meshgrid(x,y)

plt.scatter(xx1,yy1, c = f(xx1,yy1), cmap= "RdBu_r")
plt.show()

fig = plt.figure(figsize=(6,6))
#ax = fig.add_subplot(2,1,1)
ax1 = fig.add_subplot(111, projection = '3d')


ax1.set_xlim3d(-1, 1)
ax1.set_ylim3d(-1, 1)
ax1.set_zlim3d(0, 2)

ax1.set_zlabel("T(x,y)")


#ax.view_init(10,60)
ax1.view_init(30, 300)


ax1.scatter(xx1,yy1,f(xx1,yy1), c = f(xx1,yy1), cmap= "RdBu_r",alpha=0.5)

ax1.scatter(1,1,f(1,1),color="k",s=100)
ax1.scatter(1,-1,f(1,-1),color="k",s=100)
ax1.scatter(-1,-1,f(-1,-1),color="k",s=100)
ax1.scatter(-1,1,f(-1,1),color="k",s=100)
ax1.grid()
#plt.plot_color_gradients('Sequential (2)',['hot'])

plt.show()



"""

Minimización

"""
s="-"
print(s*40,"\n Parte Minimización \n",s*40)
def Rotate(p,theta=np.pi/180):
        
    M=np.array([[np.cos(theta),-1*np.sin(theta)],[np.sin(theta),np.cos(theta)]])
    
    n_p=np.dot(p,M)
    
    return n_p
"""
def Grad_T(x,y,p):
    return np.array([ p[2]+p[3]*y , p[1]+p[3]*x ])
"""
#p1=Rotate(p0,0)
#p1=Rotate(X,Y,np.pi/3)
#print(p1)
N=200

theta=np.linspace(0,2*np.pi,int(N))





#p2=p0
#lr=0.001

val_T=np.array([])
val_theta=np.copy(val_T)
for i in theta:
    p1=Rotate(p0,i)
    
    para= GetFit(p1,b)
    
    r=T(0,0.5,para)
    val_T=np.append(val_T,r)
    val_theta=np.append(val_theta,i)
    
    

#print(p1)
#print(val_T)
#r=T(0,0.5,par)

T_min=np.min(val_T)
print("Temperatura mínima: ",T_min)
#i=np.where(val_T - T_min <= 1e-6)
i=np.where(val_T == T_min)

theta_min=val_theta[i]
print("Ángulo mínimo",theta_min)
plt.plot(theta,val_T)
plt.scatter(theta_min,T_min,color="r")
#plt.scatter(theta_min,val_T[i],color="r")
plt.xlabel("ángulo theta(rad)")
plt.ylabel("Temperatura (°K)")
plt.axhline(y=T_min,color="r",linestyle= "dashed")
plt.axvline(x=theta_min,color="r",linestyle= "dashed")
plt.grid()
plt.show()

#x=sym.Symbol("x",real="True")
#y=sym.Symbol("y",real="True")

#g=T(x,y,par)

#print(g.simplify(),"\n",r)

"""
plt.scatter(p0[:,0],p0[:,1],color="k")
plt.scatter(p1[:,0],p1[:,1],color="r")
plt.show()
"""

#print(r)

