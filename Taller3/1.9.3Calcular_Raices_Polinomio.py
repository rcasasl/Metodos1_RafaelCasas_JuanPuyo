# -*- coding: utf-8 -*-
"""
3. Calcular todas las ra´ıces reales de:
f(x) = 3x^5 + 5x^4 − x^3

"""
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-2,1,100)
def Funcion(x):
    return 3*(x**5) + 5*(x**4) -(x**3) 
y=Funcion(x)
plt.plot(x,y)
plt.axhline(y=0,color="k")
def Derivative(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)
def Metod_Newt(f,der_f,xn,h=1e-6,iter_max=1000,preci=1e-6):
    err=1
    itera=0
    while err > preci and itera < iter_max:
        
        try:
            
            xn1 = xn - f(xn)/der_f(f,xn)
            #err = np.abs(f(xn)/der_f(f,xn,c))
            err=np.abs((xn1-xn)/xn)
            
        except ZeroDivisionError:
            print('Division por cero, pruebe otro valor')
            
        xn = xn1
        itera += 1
        #print('raiz:', xn,itera,err)
    
    if itera == iter_max:
        return False
    else:
        return xn
def GetAllRoots(x,Funcion,tolerancia=8):
    
    Roots = np.array([])
    
    if Funcion(0) < 1e-10:
        Roots=np.append(Roots,0)
    
    for i in x:
        root = Metod_Newt(Funcion,Derivative,i)
        
        if root != False:
            
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots,croot)
                
    Roots.sort()
    
    return Roots
print(GetAllRoots(x,Funcion))
