# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:34:38 2022

@author: Adriana
"""

import numpy as np
M = np.array([[3,-1,-1],[-1.,3.,1.],[2,1,4]])
print(M)
b = np.array([1.,3.,7.])
print(b)


def Gauss_Seidel(matriz,vector,itmax=100,error = 1e-10):
        M,N = matriz.shape
    
        x = np.zeros(N)
    
        sumk = np.zeros_like(x)
    
        it = 0
        
        
    
        residuo = np.linalg.norm(vector - np.dot(matriz,x))
        
        while ( residuo > error and it < itmax):
        
            it += 1
        
            for i in range(M):
                sum_ = 0
            
                for j in range(N):
                    if i != j:
                        sum_ += matriz[i][j]*x[j]
                x[i] = (vector[i]-sum_)/(matriz[i][i])
                
            residuo = np.linalg.norm(vector-np.dot(matriz,x))
        
        return x,it

Xsol,it= Gauss_Seidel(M,b)

print(Xsol,it)
