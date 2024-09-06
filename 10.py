import matplotlib.pyplot as plt

C = 0.005
R = 0.5
V = 1.0
L = 0.005
step = 0.001

t = 0
ic = 0

x1 = 0
x2 = 0

result = []

while t <= 0.05:
    t += step
    x1 += step * x2
    # il = x1
    x2 += step * (V - R * x1 - L * x2) / (R * L * C)
    ic = (V - L * x2 - R * x1 )/R
    result.append([t,x1+ic,x1,ic])


plt.plot([x[0] for x in result],[x[1] for x in result], label="i")
plt.plot([x[0] for x in result],[x[2] for x in result], label="i_L")
plt.plot([x[0] for x in result],[x[3] for x in result], label="i_C")

plt.legend()
plt.grid()
plt.show()
