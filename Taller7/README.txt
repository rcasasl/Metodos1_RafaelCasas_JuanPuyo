#CODIGO BORRADOR, NO EVALUAR!

import numpy as np
import matplotlib.pyplot as plt

A=np.array([[2,-1],[1,2],[1,1]])
b=np.array([2,1,4])

f1= lambda x: 4-x
f2= lambda x: 2*x-2
f3= lambda x: (1/2) -(1/2)*x

N=334

x=np.linspace(-5,5,N)
y=np.copy(x)

Puntos=np.zeros((N,N))
xx,yy=np.meshgrid(x,y)

for j in range(len(y)):
    for i in range(len(x)):   
        p=np.array([x[i],y[j]])
        Puntos[i,j]=np.linalg.norm(np.dot(A,p)-b)
        

minimo=np.min(Puntos)

j,i=np.where(Puntos==minimo)

P_minimo=np.array([float(x[i]),float(y[j])])



fig = plt.figure(figsize=(6,6))

ax1 = fig.add_subplot(111, projection = '3d')


ax1.set_xlim3d(-5, 5)
ax1.set_ylim3d(-5, 5)
ax1.set_zlim3d(0, 20)

ax1.set_zlabel("d(x,y)")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.view_init(30, 50)

ax1.scatter(xx,yy,Puntos, c = Puntos, cmap= "RdBu_r",alpha=0.5)
ax1.scatter(P_minimo[0],P_minimo[1],color="r",s=100)

ax1.grid()
ax1.plot(x,f1(x),color="k")
ax1.plot(x,f2(x),color="k")
ax1.plot(x,f3(x),color="k")

