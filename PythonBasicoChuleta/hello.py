import matplotlib.pyplot as plt
import numpy as np

#Hola Mundo
msg="Hello World"
print(msg)

#Ejemplo de PLOT
x = np.linspace(0,20,100)
plt.plot(x, np.sin(x))
plt.show()


