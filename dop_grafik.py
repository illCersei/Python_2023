import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10)
plt.ylim(-5,20)
plt.xlim(-10,10)
plt.plot(x,x**2)
plt.plot(2*x+10)
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.text(0, 0, "Тут 0;0", fontsize=8)
plt.text(2.5,-5, "2x+10", fontsize=15)
plt.show()