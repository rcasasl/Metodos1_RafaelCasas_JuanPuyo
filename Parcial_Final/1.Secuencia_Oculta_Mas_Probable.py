# -*- coding: utf-8 -*-
"""
Encuentre la secuencia oculta m´as probable del tipo de moneda que se eligi´o en cada
lanzamiento y su respectiva probabilidad Pi
.

"""

import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

States = np.array([0,1]) # 0 Justa, 1 Sesgada
Prior =  np.array([0.2,0.8])

T = np.array([[0.8,0.2],[0.2,0.8]])

E = np.array([[0.5,0.9],[0.5,0.1]])

DictH = {0:'Justa',1:'Sesgada'}

Obs= np.array([1,0,0,0,1,0,1,0])# 0 Cara, 1 Sello

def GetHiddenStates(States, N):
    
    CStates = list( combinations_with_replacement(States,N) )
    
    Permu = []
    
    for it in CStates:
        p = list(permutations(it,N))
        
        for i in p:
            if i not in Permu:
                Permu.append(i)
    
    
    return np.array(Permu)

HiddenStates=GetHiddenStates(States,len(Obs))

def GetProb(T,E,Obs,State,Prior):
    n= len(Obs)
    p=1
    p*= Prior[State[0]]

    for i in range(n-1):
        p *= T[ State[i+1],State[i]]
    #print(p,State)
    
    for i in range(n):
        p *= E[ Obs[i], State[i] ]
    
    return p

dim= len(HiddenStates)
P= np.zeros(dim)



for i in range(dim):
    P[i]= GetProb(T,E,Obs,HiddenStates[i],Prior)

maxP = np.max(P)
ii = np.where( P == np.amax(P))
secuencia=HiddenStates[ii]
#print(secuencia,maxP)
secuencia_oculta=[]
for i in range(len(secuencia[0])):
    secuencia_oculta.append(DictH[secuencia[0,i]])

print("Las secuencia oculta más probable es: \n",\
      secuencia_oculta, "\n y su probabilidad es:",maxP)


plt.plot(P,color='k')
plt.grid()
plt.axhline(y=maxP,color="r")
