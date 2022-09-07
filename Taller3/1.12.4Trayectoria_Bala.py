# -*- coding: utf-8 -*-
"""
En el lanzamiento de una bala, una c´amara fotogr´afica registra las siguientes
posiciones en metros respecto al arma homicida (tome ~g = −9,8 m/s2 ˆj):
https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReParabolico.csv
Estime el vector velocidad inicial, que estar´ıa definido por la magnitud y direcci´on.
Rpta: V0 = 10 m/s y θ = 20◦
. Hint: Encuentre el termino lineal y cuadr´atico de la
interpolaci´on y compare con la ecuaci´on de trayectoria de la bala.

"""
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import rc
import pandas as pd
#import sympy as sympy
import os.path as path
import urllib.request as urll

url = 'https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/InterpolacionNewton.csv'
filename = 'InterpolacionNewton.csv'
urll.urlretrieve(url, filename)
if not path.exists(filename):
    Path_ = urll.urlretreive(url,filename)
else:
    print("encontrado")
    Path_=filename
Data= pd.read_csv(Path_,sep=",")

X=np.float64(Data["X"])
Y=np.float64(Data["Y"])

g= -9.8

def Lagrange(x,xi,i):
    prod= 1.0
    n=len(xi)
    
    for j in range(n):
        if j != i:
            prod *= (x-xi[j])/(xi[i]-xi[j])
            
    return prod
def Poly(x,xi,yi):
    Sum=0
    n=len(xi)
    
    for i in range(n):
        Sum += yi[i]*Lagrange(x,xi,i)
    return Sum

xg=np.linspace(-4,10,100)
yg=Poly(xg,X,Y)

plt.scatter(X,Y,color="r")
plt.plot(xg,yg,color="k")

M=np.vander(X)

coeff= np.linalg.solve(M,Y)
"""
El término lineal es igual a: tan(theta)
El término cuadratico es igual a: g/(2*cos^2(theta)*(V0)^2) 
"""
coef_lin=coeff[-2]
coef_cuad=coeff[-3]

theta=np.arctan(coef_lin)#+2*np.pi

V0=(g/((coef_cuad)*(2*(np.cos(theta))**2)))**(1/2)
print(theta,V0)