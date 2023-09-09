import numpy as np
from matplotlib import pyplot
def f(x):
    return x**2

y = []
for x in range(21):
    y.append(f(x))

x = [x for x in range(21)]

pyplot.title("Задание 0")
pyplot.xlabel("x")
pyplot.ylabel("y")
pyplot.plot(x,y)
pyplot.show()