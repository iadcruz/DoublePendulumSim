import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Initial Conditions
theta = np.pi / 2
l = 1.0
gSingle = 9.8

#Constants
omega = np.sqrt(l / gSingle)

#Time Variables
dt = 0.1
t_max  = 200.0
t = np.arange(0, t_max, dt)

xSingle = []
ySingle = []

for _ in t:
    thetaCurr = theta * np.cos(omega * _)
    xSingle.append(np.sin(thetaCurr) * l)
    ySingle.append(-np.cos(thetaCurr) * l)