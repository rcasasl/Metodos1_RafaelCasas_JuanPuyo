# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:34:38 2022

@author: Adriana
"""

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

M = np.array([[3,-1,-1],[-1.,3.,1.],[2,1,4]])
print(M)
b = np.array([1.,3.,7.])
print(b)

def GetGaussSeidelMethod(A,b,itmax=100,error = 1e-10):
    
    M,N = A.shape
    """
    if M != 3 or N != 3 or np.linalg.det(A) == 0.:
        return print("Este método esta diseñado para sistemas 3x3")
    """

    x = np.zeros(N)
    
    sumk = np.zeros_like(x)
    
    it = 0
    
    residuo = np.linalg.norm( b - np.dot(A,x) )
    
    while ( residuo > error and it < itmax ):
        
        it += 1
        
        x1=(1+x[1]+x[2])/3
        y=(3+x1-x[2])/3
        z=(7-2*(x1)-y)/4
        
        
        x[0],x[1],x[2]= x1,y,z
        residuo = np.linalg.norm( b - np.dot(A,x) )
        
    return x,it,residuo

Xsol,it,residuo= GetGaussSeidelMethod(M,b)

print(Xsol,it,residuo)