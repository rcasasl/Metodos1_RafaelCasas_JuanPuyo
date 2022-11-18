# -*- coding: utf-8 -*-
"""
 Calcule las probabilidades de cada estado observable (o) como 
 la suma de las probabilidades de todos los estados ocultos.
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

#DictH = {0:'Justa',1:'Sesgada'}




def GetHiddenStates(States, N):
    
    CStates = list( combinations_with_replacement(States,N) )
    
    Permu = []
    
    for it in CStates:
        p = list(permutations(it,N))
        
        for i in p:
            if i not in Permu:
                Permu.append(i)
    
    
    return np.array(Permu)

HiddenStates=GetHiddenStates(States,8)

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



ObsStates = GetHiddenStates([0,1],8)


NObs = ObsStates.shape[0]

PObs = np.zeros(NObs)

for j in range(NObs):
    
    dim = HiddenStates.shape[0]
    P = np.zeros(dim)
    
    for i in range(dim):
        P[i] = GetProb(T,E,ObsStates[j],HiddenStates[i],Prior)
        
        
    PObs[j] = np.sum(P)

plt.plot(PObs)


"""
Verifique que la suma de todos los estados observables es 1.
"""
print("Probabilidad de todos los estados observables",\
      np.sum(PObs))

