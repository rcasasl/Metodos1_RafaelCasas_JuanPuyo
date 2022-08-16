# -*- coding: utf-8 -*-
"""
PUNTO 5: Suceción de Fibonnaci
"""
"""
1. Encontrar los primeros 20 términos
"""
print("\nPUNTO 5:\n")
def fibonnaci(n:int)->int:
    if n > 1:
        return fibonnaci(n-1)+fibonnaci(n-2)
    elif n == 0:
        return 0
    elif n == 1:
        return 1 
def terminos_fibo(n:int)->list:
    terminos=[]
    for i in range(0,n):
        terminos.append(fibonnaci(i))
    return terminos
print("Los 21 primeros terminos de la sucesion de Fibonnaci son: \n",terminos_fibo(21))    
"""
2. Graficar la sucesion de Fibonacci
"""    
import matplotlib.pyplot as plt
x_values=[]
for i in range(0,21):
    x_values.append(i)

plt.plot(x_values,terminos_fibo(21))
plt.xticks(x_values)
plt.show()
"""
3. Encontrar el valor aureo
"""
import math as mt
def Aureo(n:int)->float:
    if n != 0:
        phi = (fibonnaci(n+1))/(fibonnaci(n))
    else:
        phi=0        
    return phi
i=0
valor_n=[]
valor_cociente=[]
while i <=20:
    valor_n.append(i)
    cociente=Aureo(i)
    valor_cociente.append(cociente)
    i +=1
print("\nEl valor de la proporción Aurea (phi) para 20 términos es igual a: ",valor_cociente[-1])
plt.plot(valor_n,valor_cociente)
plt.axhline(y=((1+mt.sqrt(5))/2),color="red")
plt.show()