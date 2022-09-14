creando carpeta para el parcial ;)

"""
la derivada analítica de la función f(x)=sqrt(tanx) es:
    
    f'(x)= sec^2(x)/(2*sqrt(tan(x)))


"""


df= lambda x: (np.cos(x))**-2/(2*np.sqrt(np.tan(x)))

x= np.linspace(0.1,1.1,100)
y=df(x)
plt.plot(x,y)
