# -*- coding: utf-8 -*-
"""
Usando los m´etodos de Newton-Raphson y descenso del gradiente, encuentre la soluci´on
de los siguientes sistemas de ecuaciones no lineales
"""
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from IPython.display import clear_output
import time


def f1(v):
    return np.log(v[0]**2+v[1]**2) - np.sin(v[0]*v[1]) - np.log(2*np.pi)
def f2(v):
    return np.exp(v[0]-v[1]) + np.cos(v[0]*v[1])
S1=(f1, f2)

def g1(v):
    return 6*v[0] -2*np.cos(v[1]*v[2]) - 1
def g2(v):
    return 9*v[1]+np.sqrt(v[0]**2+np.sin(v[2])+1.06) +0.9
def g3(v):
    return 60*v[2]+3*np.exp(-v[0]*v[1]) + 10*np.pi-3
S2=(g1,g2,g3)

"""
NEWTON-RAPHSON
"""
a="-"
print(40*a)
print("\nNewton-Raphson\n")

def GetVectorF(G,r):
    
    dim = len(G)
    
    v = np.zeros(dim)
    
    for i in range(dim):
        v[i] = G[i](r)
        
    return v
def GetJacobian(G,r,h=1e-6):
    
    dim = len(G)
    
    J = np.zeros((dim,dim))
    
    for i in range(dim):
        for j in range(dim):
            h_=np.zeros(dim)
            
            h_[j]=h
           
            J[i,j] = (  G[i](r+h_) - G[i](r-h_) )/(2*h)
            
            #J[i,j] = (  G[i](r[0],r[1]+h,r[2]) - G[i](r[0],r[1]-h,r[2]) )/(2*h)
            #J[i,j] = (  G[i](r[0],r[1],r[2]+h) - G[i](r[0],r[1],r[2]-h) )/(2*h)
        
    return J.T

def NewtonRaphson(G,r,error=1e-10):
    
    it = 0
    d = 1
    Vector_d = np.array([])
    
    while d > error:
        
        it += 1
        
        rc = r
        
        F = GetVectorF(G,r)
        J = GetJacobian(G,r)
        InvJ = np.linalg.inv(J)
        
        r = rc - np.dot( InvJ, F )
        
        diff = r - rc
        #print(diff)
        
        d = np.linalg.norm(diff)
        
        Vector_d = np.append( Vector_d , d )
        
    return r,it,Vector_d
"""
El vector de partida [2,2] se debe construir usando np.array, ya que de lo
contrario al realizar las sumas en la funcion del Jacobiano, se van a 
concatenar las listas, no se van a sumar sus componentes
"""
rs1,it,distancias = NewtonRaphson(S1,np.array([2,2]))

print("Solución sistema 1: ",rs1,"\nNúmero de iteraciones",it)

print("\nComprobación:",S1[0](rs1),S1[1](rs1),"\n")


rs2,it,distancias = NewtonRaphson(S2,np.array([0,0,0]))

print("Solución sistema 2: ",rs2,"\nNúmero de iteraciones",it)

print("\nComprobación:",S2[0](rs2),S2[1](rs2),S2[2](rs2),"\n")


"""
DESCENSO GRADIENTE
"""
print(40*a)
print("\nDescenso Gradiente\n")

def GetMetric(G,r):
    v = GetVectorF(G,r)
    return 0.5*np.linalg.norm(v)**2
def GetFig(F,R,it):
    
    fig = plt.figure(figsize=(8,4))
    
    labels = ['X','Y','Z']
    
    ax = fig.add_subplot(1,2,1)
    ax1 = fig.add_subplot(1,2,2)

    ax.set_title('Metric: %.20f' %(F[it]))

    ax.plot(F[:it])
    ax.set_xlabel('%.0f' %(it))
    ax.set_yscale('log')
    ax1.plot(R[:it],label=labels)
    ax1.set_xlabel('%.0f' %(it))
    ax1.legend(loc=0)
    
    plt.show()
def GetSolve(G,r,lr=1e-3,epochs=int(1e5),error=1e-7):
    
    d = 1
    it = 0
    Vector_F = np.array([])
    
    R_vector = np.array(r)
    print("Entrenamiento en curso...")
    while d > error and it < epochs:
        
        CurrentF = GetMetric(G,r)
        
        J = GetJacobian(G,r)
        
        GVector = GetVectorF(G,r)
        #print(J,"\n\n",GVector)
        
        #Machine Learning
        r = r - lr*np.dot(J,GVector) 
        
        R_vector = np.vstack((R_vector,r))
        
        NewF = GetMetric(G,r)
        
        
        Vector_F = np.append(Vector_F,NewF)
        
        d = np.abs( CurrentF - NewF )/NewF
        

        """
        if it%500 == 0:
            #print(it,d)
            clear_output(wait=True)
            GetFig(Vector_F,R_vector,it)
            time.sleep(0.01)
        """    
        it += 1
        
    if d < error:
        print(' Entrenamiento completo ', d, 'iteraciones', it)
        
    if it == epochs:
        print(' Entrenamiento no completado ')
        
    return r,it,Vector_F,R_vector

rds1,it,F,R = GetSolve(S1,np.array([2,2]),lr=1e-2)
print("\nSolución sistema 1: ",rds1,"\nNúmero de iteraciones",it,"\n")
print("\nComprobación:",S1[0](rds1),S1[1](rds1),"\n")

rds2,it,F,R = GetSolve(S2,np.array([0,0,0]),lr=1e-4)
print("\nSolución sistema 2: ",rds2,"\nNúmero de iteraciones",it,"\n")
print("\nComprobación:",S2[0](rds2),S2[1](rs2),S2[2](rds2),"\n")