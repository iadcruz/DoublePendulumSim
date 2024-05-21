import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Constants
g = 9.8
l1 = 1.0
l2 = 1.0
m1 = 1.0
m2 = 1.0

#Initial conditions
theta1 = np.pi / 2
theta2 = np.pi / 2
omega1 = 2.0
omega2 = 6.0

state = np.array([theta1, omega1, theta2, omega2])

#Time variables
dt = 0.01
t_max = 20.0
t = np.arange(0, t_max, dt)

def differentials(state):
    theta1, omega1, theta2, omega2 = state
    delta = theta2 - theta1
    
    denom1 = (m1 + m2) * l1 - m2 * l1 * np.cos(delta) * np.cos(delta)
    denom2 = (l2 / l1) * denom1
    
    domega1 = (m2 * l1 * omega1**2 * np.sin(delta) * np.cos(delta) + m2 * g * np.sin(theta2) * np.cos(delta) + m2 * l2 * omega2**2 * np.sin(delta) - (m1 + m2) * g * np.sin(theta1)) / denom1
    domega2 = (-m2 * l2 * omega2**2 * np.sin(delta) * np.cos(delta) + (m1 + m2) * g * np.sin(theta1) * np.cos(delta) - (m1 + m2) * l1 * omega1**2 * np.sin(delta) - (m1 + m2) * g * np.sin(theta2)) / denom2


    return np.array([omega1, domega1, omega2, domega2])

def rungeKutta(state, dt):
    k1 = dt * differentials(state)
    k2 = dt * differentials(state + 0.5 * k1)
    k3 = dt * differentials(state + 0.5 * k2)
    k4 = dt * differentials(state + k3)

    return state + (k1 + 2 * k2 + 2 * k3 + k4) / 6

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

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

line, = ax.plot([], [], 'o-', lw=2)
trace, = ax.plot([], [], 'b-', lw=1)

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