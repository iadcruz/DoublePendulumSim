import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from double import rungeKutta
from double import l1, l2
from double import state

dt = 0.01
t_max = 20.0
t = np.arange(0, t_max, dt)
t1 = []
t2 = []

for _ in t:
    state = rungeKutta(state, dt)
    t1.append(state[0])
    t2.append(state[2])

x1 = l1 * np.sin(t1)
y1 = -l1 * np.cos(t1)
x2 = x1 + l2 * np.sin(t2)
y2 = y1 - l2 * np.cos(t2)


fig, ax = plt.subplots(1, 2, layout="constrained")
ax[0].set_xlim(-2, 2)
ax[0].set_ylim(-2, 2)

line, = ax[0].plot([], [], 'o-', lw=2)
trace, = ax[0].plot([], [], 'b-', lw=1)
ax[0].set_title('Double Pendulum')

def init():
    line.set_data([], [])
    trace.set_data([], [])
    return line, trace

def update(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    line.set_data(thisx, thisy)
    trace.set_data(x2[:i], y2[:i])
    return line, trace

ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=dt*1000)

plt.show()