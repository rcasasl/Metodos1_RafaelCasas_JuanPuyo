# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 14:59:11 2022

@author: Juan
"""

import numpy as np
import matplotlib.pyplot as plt
import wget  
import os.path as path


file = 'Sigmoid.csv'

url = 'https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/Sigmoid.csv'
if not path.exists(file):
    Path_ = wget.download(url,file)
    print('File loaded')
else:
    Path_ = file

data = np.loadtxt(Path_,dtype=float,delimiter=",",skiprows=1)

x = data[:,0]
y = data[:,1]
N = len(x)
"""
a) Defina el modelo de ajuste
"""

def M(x,p):
    return p[0]/(p[1]+np.exp(-p[2]*x))

"""
b)Defina la m´etrica (funci´on de costo) a minimizar
"""

def X2(p,x,y):
    term= y-M(x,p)
    return np.sum(term**2)
"""
e) Use una taza de aprendizaje γ = 1 × 10^−3 o γ = 5 × 10^−4
,
~θ0 = [1, 1, 1], un error de
parada  = 0.01 y un m´aximo de iteraciones de 1 × 10^4

"""
#"""
def ErrorProm(p,x,y):
    term=np.abs((y-M(x,p)))
    return np.average(term)
#"""
#par0=np.array([np.random.rand(), np.random.rand(), np.random.rand()])
par0=np.array([1,1,1])
print(par0)

def GetGrad(M,p,x,h=1e-6):
    
    dim=len(p)
    J = np.zeros(dim)
    
    for j in range(dim):
        h_=np.zeros(dim)
        
        h_[j]=h
           
        J[j] = (  M(x,p+h_) - M(x,p-h_) )/(2*h)
            
            
        
    return J

def DescGrad(M,p,x,y,lr=1e-3,epochs=int(1e4),error=1e-2):
    
    d = 1
    it = 0
    
    
    
    
    while d > error and it < epochs:
        
        CurrentMe = X2(p,x,y)
        #print(CurrentMe)
        Sum=0
        
        #Machine Learning
        for i in range(len(y)):
            Sum += (y[i]-M(x[i],p))*GetGrad(M,p,x[i])
        #print(Sum)
            
        p = p - lr*(-2)*Sum
        
        
        NewMe = X2(p,x,y)
        #print(NewMe)
        
        
        d = ErrorProm(p,x,y)
        #d= np.abs(CurrentMe-NewMe)/NewMe
        #d=np.sqrt(NewMe/len(y))
        
        #print(CurrentMe,NewMe,d,"\n",p,"\n")
        """
        if it%500==0:
            print(CurrentMe,NewMe)
        #"""    
        it += 1
        
    if d < error:
        print(' Entrenamiento completo ', d, 'iteraciones', it)
        
    if it == epochs:
        print(' Entrenamiento no completado ',d)
        
    return p,it


par,num_it=DescGrad(M,par0,x,y)
print(par)

"""
f) Grafique los datos y the best fit model con sus par´ametros.
"""

X=np.linspace(-10,10,120)
plt.scatter(x,y)
plt.plot(X,M(X,par),color="k")
plt.show()
