import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from double import rungeKutta
from double import l1, l2
from double import state
from single import xSingle, ySingle

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

fig, ax = plt.subplots(2, 2, layout="constrained")
ax[0][0].set_xlim(-2, 2)
ax[0][0].set_ylim(-2, 2)
ax[0][1].set_xlim(-2, 2)
ax[0][1].set_ylim(-2, 2)

ax[1][0].set_xlim(0, 20)
ax[1][0].set_ylim(-2, 2)
ax[1][1].set_xlim(0, 20)
ax[1][1].set_ylim(-2, 2)

line, = ax[0][1].plot([], [], 'o-', lw=2)
trace, = ax[0][1].plot([], [], 'b-', lw=1)
ax[0][1].set_title('Double Pendulum')

line2, = ax[0][0].plot([], [], 'o-', lw=2)
trace2, = ax[0][0].plot([], [], 'b-', lw=1)
ax[0][0].set_title('Single Pendulum')

trace3, = ax[1][0].plot([], [], 'b-', lw=1)
ax[1][0].set_title('X Position vs. Time')

trace4, = ax[1][1].plot([], [], 'b-', lw=1)
ax[1][1].set_title('Y Position vs. Time')

def init():
    line.set_data([], [])
    trace.set_data([], [])

    line2.set_data([], [])
    trace2.set_data([], [])

    trace3.set_data([], [])
    trace4.set_data([], [])
    return line, trace, line2, trace2, trace3, trace4

def update(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    line.set_data(thisx, thisy)
    trace.set_data(x2[:i], y2[:i])

    thisx2 = [0, xSingle[i]]
    thisy2 = [0, ySingle[i]]
    line2.set_data(thisx2, thisy2)
    trace2.set_data(xSingle[:i], ySingle[:i])

    trace3.set_data(t[:i], xSingle[:i])
    trace4.set_data(t[:i], ySingle[:i])
    return line, trace, line2, trace2, trace3, trace4

ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=dt*1000)

plt.show()
