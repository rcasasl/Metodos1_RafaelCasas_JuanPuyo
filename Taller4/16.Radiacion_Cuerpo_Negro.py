# -*- coding: utf-8 -*-
"""
a) Compute this integral using the Gauss-Laguerre quadrature method for n=3
evaluation points.

"""
import numpy as np
import matplotlib.pyplot as plt
a = 0
b = 1

f = lambda x : np.exp(x)*(x**3/(np.exp(x)-1))
n=3

rts,wghts=np.polynomial.laguerre.laggauss(n)
#x = 0.5*((b-a)*rts + a + b)
Int= np.sum(wghts*f(rts))



Int= np.sum(wghts*f(rts))



print(n,":",Int)

"""
Graficar error relativo
"""
Err= lambda I: (I)/((np.pi**4)/15)
x= np.arange(2,11)
y=np.array([])
for i in x:
    
    rts,wghts=np.polynomial.laguerre.laggauss(i)
    #t = 0.5*((b-a)*rts + a + b)
    Int2= np.sum(wghts*f(rts))
    
    
   
    
    Integral= Int2
    
    y=np.append(y,Err(Integral))

plt.scatter(x,y)
plt.axhline(1,color="k",linestyle="dashed")
plt.show()