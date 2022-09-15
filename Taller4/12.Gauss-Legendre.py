# -*- coding: utf-8 -*-
"""
Calcular integral por la cuadratura de gaus legendre
"""
import numpy as np
a = 1
b = 2

f = lambda x : 1/(x**2)
n=2

rts,wghts=np.polynomial.legendre.leggauss(n)
x = 0.5*((b-a)*rts + a + b)
Int= 0.5*(b-a)*np.sum(wghts*f(x))
print(n,":",Int)
n=3

rts,wghts=np.polynomial.legendre.leggauss(n)
x = 0.5*((b-a)*rts + a + b)
Int2= 0.5*(b-a)*np.sum(wghts*f(x))
print(n,":",Int2)