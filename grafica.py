#Graficar
from math import pi, sin, cos
import matplotlib.pyplot as plt

x=[]
y=[]
z=[]
cont=-2*pi
while cont <= 2*pi:
	x.append(cont)
	y.append(sin(cont))
	z.append(cos(cont))
	cont+=0.1



plt.plot(x,y, label='Sin(x)')
plt.plot(x,z, label='Cos(x)')
plt.legend()
plt.grid()
plt.title('Grafica Trigonometrica')
plt.xlabel('Dominio')
plt.ylabel('Rango')
plt.show()
