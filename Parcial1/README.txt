creando carpeta para el parcial ;)


df= lambda x: (np.cos(x))**-2/(2*np.sqrt(np.tan(x)))

x= np.linspace(0.1,1.1,100)
y=df(x)
plt.plot(x,y)
