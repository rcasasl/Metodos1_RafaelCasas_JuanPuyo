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



"""
Verifique que la suma de todos los estados observables es 1.
"""
print("Probabilidad de todos los estados observables (prior igual a [0.2,0.8]): \n",np.sum(PObs))

"""
¿Depende el resultado de la probabilidad a-priori?
"""
fig = plt.figure(figsize=(15,6))
ax1 = fig.add_subplot(1,2,1)

ax1.plot(PObs,color="r")
ax1.title.set_text("Probabilidad de observaciones con \n prior igual a: [0.2,0.8]")

Prior =  np.array([0.6,0.4])#Cambiando la probabilidad apriori

for j in range(NObs):
    
    dim = HiddenStates.shape[0]
    P = np.zeros(dim)
    
    for i in range(dim):
        P[i] = GetProb(T,E,ObsStates[j],HiddenStates[i],Prior)
        
        
    PObs[j] = np.sum(P)

print("Probabilidad de todos los estados observables (prior igual a [0.6,0.4]): \n",np.sum(PObs))

ax2= fig.add_subplot(1,2,2)
ax2.plot(PObs,color="k")
ax2.title.set_text("Probabilidad de observaciones con \n prior igual a: [0.6,0.4]")
                   

print("Como se puede apreciar en los gráficos,la probabilidad a priori altera las probabilidades de las observaciones, como era de esperarse.")

