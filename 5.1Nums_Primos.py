# -*- coding: utf-8 -*-
"""
5.1 Numeros Primos
"""
"""
1. Calcular los primeros 100 numeros primos
"""
def primo(n:int)->bool:
    i=1
    primo= True
    if n == 1:
        primo = False
    while i < n and primo == True:
        modulo= n%i
        if modulo == 0 and i != 1:
            primo = False
        i += 1
    return primo
primos=[]
num=1
while len(primos)<1000:
    if primo(num)== True:
        primos.append(num)
    num += 1
"""
2. imprimir en pantalla los 10 primeros numeros primos.
"""
print ("\nLa lista de los primeros 10 primos es: ",primos[0:10])
"""
3. Graficar los primeros 1000 primos
"""
import matplotlib.pyplot as plt
pos_primos=[]
for i in range(1,1001):
    pos_primos.append(i)
plt.plot(pos_primos,primos)
plt.show()
