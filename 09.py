import matplotlib.pyplot as plt
import math
import random

C = 0.0001
V = 10
L = 0.01013
step = 0.0001

R = 1

i = 0
q = 0
t = 0
result = []
while t <= 0.05:
    t += step
    q = q + step * i
    i = i + step * (V - R*i - q/C)/L
    result.append([t, i])


plt.plot([x[0] for x in result], [x[1] for x in result])
plt.title('RL Circuit')
plt.xlabel('time (s)')
plt.ylabel("i [A]")


plt.grid()
plt.show()
