"""
ESTE NO ES EL EJERCICIO FINAL, ES UN BORRADOR. NO EVALUAR

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

class Sistemas_Lineales:
    
    def __init__(self, matriz,vector):
        
        self.matriz = matriz
        self.vector = vector
    
    def MetodoJacobi(self):

        M,N = self.matriz.shape
    
        x = np.zeros(N)
    
        sumk = np.zeros_like(x)
    
        it = 0
        
        itmax = 1000
        
        error = 1e-10
    
        residuo = np.linalg.norm(self.vector - np.dot(self.matriz,x))
        
        while ( residuo > error and it < itmax):
        
            it += 1
        
            for i in range(M):
                sum_ = 0
            
                for j in range(N):
                    if i != j:
                        sum_ += self.matriz[i][j]*x[j]
                sumk[i] = sum_
        
            for i in range(M):
                if self.matriz[i,i] != 0:
                    x[i] = (self.vector[i] - sumk[i])/self.matriz[i,i]
                else:
                    print('No invertible por Jacobi')
            
                residuo = np.linalg.norm(self.vector - np.dot(self.matriz,x))

        print(x,it)
        return x,it
    def GaussSeidel(self,itmax=100,error = 1e-10):
    
        M,N = self.matriz.shape
    
        x = np.zeros(N)
        
        
        
        it = 0
        
        residuo = np.linalg.norm( self.vector - np.dot(self.matriz,x) )
        
        while ( residuo > error and it < itmax ):
            
            it += 1
            
            x1=(1+x[1]+x[2])/3
            y=(3+x1-x[2])/3
            z=(7-2*(x1)-y)/4
            
            
            x[0],x[1],x[2]= x1,y,z
            residuo = np.linalg.norm( self.vector - np.dot(self.matriz,x) )
        print(x,it)
        return x,it
M = np.array([[3,-1,-1],[-1.,3.,1.],[2,1,4]])
b = np.array([1.,3.,7.])

sistema=Sistemas_Lineales(M,b)
sistema.MetodoJacobi()
sistema.GaussSeidel()
