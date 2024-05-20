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
omega1 = 0.0
omega2 = 0.0

state = np.array([theta1, omega1, theta2, omega2])

#Time variables
dt = 0.01
t_max = 20.0
t = np.arange(0, t_max, dt)

def differentials(state):
    theta1, omega1, theta2, omega2 = state
    
    domega1 = 9*g*m2*np.sin(theta2)*np.cos(theta1-theta2)+9*l1*m2*np.sin(theta1-theta2)*np.cos(theta1-theta2)*np.square(omega1)+6*l2*m2*np.sin(theta1-theta2)*np.square(omega2)-6*g*m1*np.sin(theta1)-12*g*m2*np.sin(theta1)
    domega2 = -9*g*m1*np.sin(theta1)+9*g*m1*np.sin(theta1)*np.cos(theta1-theta2)-6*g*m1*np.sin(theta2)-18*g*m2*np.sin(theta1-theta2)*np.sin(theta1)+18*g*m2*np.sin(theta1)*np.cos(theta1-theta2)-18*g*m2*np.sin(theta2)-6*l1*m1*np.sin(theta1-theta2)*np.square(omega1)-18*l1*m2*np.sin(theta1-theta2)*np.square(omega1)+9*l2*m2*np.square(np.sin(theta1-theta2))*np.square(theta2)-9*l2*m2*np.sin(theta1-theta2)*np.cos(theta1-theta2)*np.square(theta2)
    
    denom1 = 4*l1*m1+9*l1*m2*np.sin(theta1-theta2)*np.cos(theta1-theta2)-9*l1*m2*np.square(np.cos(theta1-theta2))+12*l1*m2
    denom2 = 4*l2*m1+9*l2*m2*np.sin(theta1-theta2)*np.cos(theta1-theta2)-9*l2*m2*np.square(np.cos(theta1-theta2))+12*l2*m2
    
    domega1 /= denom1
    domega2 /= denom2

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

def init():
    line.set_data([], [])
    return line,

def update(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    
    line.set_data(thisx, thisy)
    return line,

ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=dt*1000)
plt.show()