import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from  matplotlib import cm
from scipy.spatial import distance

import math
import random


def f(x,y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

def random_walk(known_points : list[list]):
    while True:
        while True:
            x = random.uniform(-5,5)
            y = random.uniform(-5,5)
            near_point = False
            print("ランダム値:{0},{1}".format(x, y))
            for known_point in known_points:
                if not (distance.euclidean([known_point[0],known_point[1]],[x,y])) < 10:
                    near_point = True
                    print("近似値発見")
            if not near_point:
                print("近似値未発見")
                break

        result = [[x,y,f(x,y)]]
        while True:
            step = random.uniform(-0.05,0.05)
            if f(x+step,y+step) <  result[-1][2]:
                result.append([x,y,f(x+step,y+step)])

            if len(result) > 2 and abs(result[-1][2] - result[-2][2]) < 0.00001:
                break
        if len(known_points) == 0:
            print("1st")
            return result[-1]
        for known_point in known_points:
            print("距離:{0}".format(distance.euclidean(result[-1], known_point)))
            if not (distance.euclidean(result[-1], known_point) < 10):
                print("新規値{0}".format(result[-1]))
                return result[-1]
        print("すでに探索済み:{0}".format(result[-1]))

result = []
while len(result) < 5:
    print(len(result))
    result.append(random_walk(result))

print(result)


X,Y = np.meshgrid(np.linspace(-5,5,100),np.linspace(-5,5,100))
Z = f(X,Y)

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,Z,cmap=cm.coolwarm,alpha=0.5)
ax.contour(X,Y,Z,zdir='z',offset=-50,levels=20)
for i in result:
    ax.scatter(i[0],i[1],i[2],color="red")

plt.show()

