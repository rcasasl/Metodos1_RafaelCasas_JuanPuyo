# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 20:59:16 2022

@author: Juan
"""

import numpy as np
from tqdm import tqdm

def GenerarPuntos():
    x_1=np.random.rand()
    x_2=np.random.rand()
    x_3=np.random.rand()
    x_4=np.random.rand()
    x_5=np.random.rand()
    x_6=np.random.rand()
    x_7=np.random.rand()
    x_8=np.random.rand()
    
    return np.array([x_1,x_2,x_3,x_4,x_5,x_6,x_7,x_8])



def f(v):
    return ((np.sum(v)**2))
#v=GenerarPuntos()
#print(f(v),np.sum(v)**2)

N=1e5

muestra=np.zeros(int(N))
for i in tqdm(range(int(N))):
    sum_ = f(GenerarPuntos())
    muestra[i]=sum_

print(len(muestra))
integral=(2**(-7))*np.average(muestra)
    
print("estimación Montecarlo: ",integral,"\nIntegral exacta: ",25/192)     

