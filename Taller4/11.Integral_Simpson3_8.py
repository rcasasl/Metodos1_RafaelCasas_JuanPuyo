# -*- coding: utf-8 -*-
"""
Calcular usando método Simpson 3/8
"""
import numpy as np
import matplotlib.pyplot as plt

f= lambda x: np.sqrt(1+ np.exp(-x**2))
x= np.linspace(-2,2,50)
y=f(x)
plt.plot(x,y)

a,b=-1,1
h=(b-a)/3

Int= (3/8)*h*(f(a)+f(b)+3*f((b+2*a)/3)+3*f((2*b+a)/3))
print(Int)
