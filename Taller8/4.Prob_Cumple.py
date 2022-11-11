# -*- coding: utf-8 -*-
"""
a)Calcular la probabilidad que n persona, 
tengan fechas diferentes de cumplea˜nos
"""

import numpy as np
import matplotlib.pyplot as plt

prob= lambda n: (np.math.factorial(365)/np.math.factorial(365-n))/(365**n)
print(prob(23))

"""
Grafique la probabilidad P(n ≤ 80) como
funci´on de n
"""

n= np.linspace(1,80,80)
probab=np.array([])
for i in n:
    probab=np.append(probab,prob(i))

plt.plot(n,probab)
plt.grid()
plt.title("Probabilidad en función \n de n ")
plt.ylabel("P(n)")
plt.xlabel("n")
plt.show()