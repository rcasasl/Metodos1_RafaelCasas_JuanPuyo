# -*- coding: utf-8 -*-
"""
PUNTO 4: Diseñe un algoritmo para encontrar
todos los máximos locales en esta serie de datos
"""
print("PUNTO 4:\n")
file = open("EstrellaEspectro.txt","r")
array= file.readlines()
y_values=[]
maximos= []

"""
este for loop se encarga de separar los valores de y 
de los de x, y los agrupa en la lista de nombre array
"""
for i in array:
        a= i.replace("\n","")
        div= a.split("  ")
        y_values.append(div[1])
#print(y_values)
maxim= y_values[0]
t=1
#Si los datos comienzan ascendentes
if maxim < y_values[t]:
    while t < (len(y_values)-1):    
        if maxim < y_values[t]:
            maxim = y_values[t]
            t +=1
        elif maxim > y_values[t]:
            maximos.append(maxim)
            count=0
            while maxim > y_values[t+count]:
                maxim = y_values[t+count]
                count +=1
            t += count
#Si los datos comienzan descendentes
elif maxim > y_values[t]:
    while t < (len(y_values)-1):
        if maxim > y_values[t]:
            maximos.append(maxim)
            count=0
            while maxim > y_values[t+count]:
                maxim = y_values[t+count]
                count +=1
            t += count
        elif maxim < y_values[t]:
            maxim = y_values[t]
            t +=1
print("La lista de los máximos locales es: \n",maximos,"\nPara un total de",len(maximos),"máximos.")
