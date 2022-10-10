# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
"""
a) Modifique el c´odigo de la clase para que S
3
sea el ´unico elemento del vector de
funciones.
"""
def f(r):
    return r[0]**2+r[1]**2+r[2]**2+r[3]**2-1
G=(f,)
def GetVectorF(G,r):  
    #print(r)
    v = G[0](r)
    return np.array([v])
#print(GetVectorF(G,np.array([3,0,0,1])))

"""
b) Calcule la m´etrica de minimizaci´on 
 como la magnitud del vector de funciones.
"""
def GetMetric(G,r):
    v = GetVectorF(G,r)
    return np.linalg.norm(v)
"""
c) Modifique el Jacobiano 
    a una dimensi´on (1 × 4).
"""
def GetJacobian(G,r,h=1e-6):
    
    dim = len(G)
    
    J = np.zeros((dim,4))
    
    for i in range(dim):
        for j in range(4):
            h_=np.zeros(4)
            
            h_[j]=h
           
            J[i,j] = (  G[i](r+h_) - G[i](r-h_) )/(2*h)
            
            #J[i,j] = (  G[i](r[0],r[1]+h,r[2]) - G[i](r[0],r[1]-h,r[2]) )/(2*h)
            #J[i,j] = (  G[i](r[0],r[1],r[2]+h) - G[i](r[0],r[1],r[2]-h) )/(2*h)
        
    return J.T
#print(GetJacobian(G,np.array([3,0,0,1])))
"""
d) Genere un punto aleatorio uniformemente distribuido en R
4
(es decir, un vector
aleatorio de 4 componentes) en el intervalo [-1,1].
"""
def GetPoint(min_=-1,max_=1):
    p=np.array([np.random.uniform(min_,max_),np.random.uniform(min_,max_)\
                ,np.random.uniform(min_,max_),np.random.uniform(min_,max_)])
    return p
#print(GetPoint())
"""
e) Corra el algoritmo de aprendizaje 
   para que el vector aleatorio se ubique 
   en alg´un punto de S3
"""
def GetSolve(G,r,lr=1e-3,epochs=int(1e5),error=1e-7):
    
    d = 1
    it = 0
    Vector_F = np.array([])
    
    R_vector = np.array(r)
    #print("Entrenamiento en curso...")
    while d > error and it < epochs:
        CurrentF = GetMetric(G,r)
        #print("Metr")
        
        J = GetJacobian(G,r)
        
        
        GVector = GetVectorF(G,r)
        #print("GVect")
        #print("Jacob",J,"\n\n","GVect",GVector)
        
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
        
    """    
    if d < error:
        print(' Entrenamiento completo ', d, 'iteraciones', it)
    """    
    if it == epochs:
        print(' Entrenamiento no completado ')
        
    return r,it,Vector_F,R_vector
#sol,it,vect,rvect=GetSolve(G,GetPoint())
#print(sol)
N=1e3
puntos=np.zeros((int(N),4))


    
for i in tqdm(range(int(N))):
    sol,it,vect,rvect=GetSolve(G,GetPoint())
    if f(sol) > 1e-8:
        print("Error")
    puntos[i,0]= sol[0]
    puntos[i,1]= sol[1]
    puntos[i,2]= sol[2]
    puntos[i,3]= sol[3]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1, projection = '3d')

#configurar límites de los ejes
ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)

ax.view_init(10, 60)
X=puntos[:,0]
Y=puntos[:,1]
Z=puntos[:,2]
ax.scatter(X,Y,Z,color='b')
plt.show()
#print("\nComprobación:",f(sol))