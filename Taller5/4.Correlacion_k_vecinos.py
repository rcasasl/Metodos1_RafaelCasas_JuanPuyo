# -*- coding: utf-8 -*-
"""

"""
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

N=1e4

x=np.random.rand(int(N))

def C(k,x):
    prod=np.array([])
    for i in range(len(x)-30):
        prod=np.append(prod,x[i]*x[i+k])
    
    return np.average(prod)
cor=C(30,x)
print("\n\nCorrelación con k=30:",cor,"\n\n")
k=np.arange(1,31)
y= np.array([])
for i in tqdm(k):
    y=np.append(y,C(i,x))
#print(y)
plt.plot(k,y)
plt.title("Generador Numpy")
plt.ylabel("C(k)")
plt.xlabel("k-esimo vecino")
plt.grid()
plt.ylim(ymin=0.20,ymax=0.30)
plt.show()


