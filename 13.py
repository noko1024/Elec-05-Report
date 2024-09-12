import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from  matplotlib import cm

import math
import random

from pyparsing import alphas


def f(x,y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2


x = random.uniform(-5,5)
y = random.uniform(-5,5)
result =[[x,y,f(x,y)]]


min_points = []

while True:
    step = random.uniform(-0.05,0.05)
    if f(x+step,y+step) <  result[-1][2]:
        result.append([x,y,f(x+step,y+step)])

    if len(result) > 1 and (result[-1][2] - result[-2][2]) < 0.00001:
        min_points.append([x,y,f(x+step,y+step)])
        print(len(min_points))
        x = random.uniform(-5, 5)
        y = random.uniform(-5, 5)
    if len(min_points) > 10:
        break



X,Y = np.meshgrid(np.linspace(-5,5,100),np.linspace(-5,5,100))
Z = f(X,Y)

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,Z,cmap=cm.coolwarm,alpha=0.5)
ax.contour(X,Y,Z,zdir='z',offset=-50,levels=20)
for i in min_points:
    ax.scatter(i[0],i[1],i[2],color="red")
    print(i)
plt.show()

