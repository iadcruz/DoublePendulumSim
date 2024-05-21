import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Initial Conditions
theta = 0.0
l = 1.0
gSingle = 9.8

#Constants
omega = np.sqrt(l / gSingle)

#Time Variables
dt = 0.01
t_max  = 20
t = np.arange(0, t_max, dt)

stateSingle = np.array([theta])
xSingle = []
ySingle = []

for _ in t:
    xSingle.append(l*np.cos(omega * _))
    ySingle.append(l*np.sin(omega * _))