# -*- coding: utf-8 -*-
"""
Calcular todas las ra´ıces reales de 
los primeros 20 polinomios de Laguerre.


"""
import numpy as np
import sympy as sym

def Laguerre(n):
    x= sym.Symbol("x",Real=True)
    y= sym.Symbol("y",Real=True)
    e=np.e
    y= (e**(-x))*(x**n)
    
    p= ((e**x)/np.math.factorial(n))*sym.diff(y,x,n)
    poly=sym.lambdify([x],p,'numpy')
    return poly
def Derivative(f,x,h=1e-8):
    return (f(x+h)-f(x-h))/(2*h)
def Metod_Newt(f,der_f,xn,h=1e-8,iter_max=1000,preci=1e-8):
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
def GetAllRoots(x,Funcion,tolerancia=6):
    
    Roots = np.array([])
    
    if np.abs(Funcion(0)) < 1e-10:
        Roots=np.append(Roots,0)
    
    for i in x:
        root = Metod_Newt(Funcion,Derivative,i)
        
        if root != False:
            
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots,croot)
                
    Roots.sort()
    
    return Roots
def Calc_Raiz_20_pol():
    Raices=np.array([])
    n=np.arange(21)
    
    for i in n:
        if i !=0:
        
            x=np.linspace(0,100,50)
            r=GetAllRoots(x,Laguerre(i))
            
            Raices=np.append(Raices,"Laguerre grad "+str(i)+":")
            Raices=np.append(Raices, r)
        
    return Raices
r=Calc_Raiz_20_pol()
print(r)
#print(GetAllRoots(x,Laguerre(2)))
