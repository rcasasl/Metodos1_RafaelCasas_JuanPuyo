# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 13:46:28 2022

@author: rafae
"""

#factorial

def factorial(num:int) -> int:
    nfact = 1
    while (num > 1):
        nfact *= num
        num -= 1
        
    return nfact

#print(factorial(20))

def variaciones(n:int, r:int) -> int:
    d = n 
    nfact = 1
    rfact = 1
    while (n> 1):
        nfact *= n
        n -= 1
        
    num = d-r
    while (num>1):
        rfact *= num
        num -= 1        
        
    variacion = nfact/rfact    

    return variacion
#print(variaciones(6, 3))

def combinacion(n:int, m:int) -> int:
    while (n>m):
        d = n
        f = m
        nfact = 1
        rfact = 1
        mfact = 1
        while (n> 1):
            nfact *= n
            n -= 1
        while (m> 1):
            mfact *= m
            m -= 1  
        num = d-f
        while (num>1):
            rfact *= num
            num -= 1        
            
        combinacion = nfact/(mfact*rfact)    

        return combinacion
#print(combinacion(21, 11))
    
    