# -*- coding: utf-8 -*-
"""
Usando la generaci´on de puntos sobre una esfera 
estime la integral
"""
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

"""
def f(P,phi):
    return np.exp(P)*(P**2)*np.sin(phi)
"""
def g(x,y,z):
    return np.exp(np.sqrt(x**2+y**2+z**2))
def Generar_Punto(N,p=1):
    
    u=np.random.rand()
    
    
    P=p*(u**(1/3))
    
    
    theta=np.random.uniform(0,np.pi*2)
    
    phi=np.random.uniform(0,np.pi)
    
    
    
    

    x= P*np.sin(phi)*np.cos(theta)
    y= P*np.sin(phi)*np.sin(theta)
    z= P*np.cos(phi)
    
    return x,y,z

    

N=int(1e5)
Muestra= np.zeros(N)

for i in tqdm(range(N)):
    x,y,z= Generar_Punto(N)
    Muestra[i]= g(x,y,z)    


integral= ((4/3)*np.pi)*np.average(Muestra)
print("\nEstimación: ",integral,"\nExacta: ",4*np.pi*(np.e-2))

