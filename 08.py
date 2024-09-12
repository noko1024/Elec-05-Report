import matplotlib.pyplot as plt

V = 1000
R = 100
L = 0.3

step = 0.0001

i = 0
t = 0
result = []
while i <= 9.99:
    t += step
    i += step * (V-i*R) / L
    result.append([t, i])


plt.plot([x[0] for x in result], [x[1] for x in result])
plt.title('RL Circuit')
plt.xlabel('time (s)')
plt.ylabel("c")


plt.grid()
plt.show()
