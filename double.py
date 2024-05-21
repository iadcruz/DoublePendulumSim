import numpy as np
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

