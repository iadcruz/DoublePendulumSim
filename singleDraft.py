import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from plots import t_max
from plots import dt
from plots import t

#Initial Conditions
theta = 0.0
l = 1.0
gSingle = 9.8

#Constants
omega = np.sqrt(l / gSingle)

stateSingle = np.array([theta])
xSingle = []
ySingle = []

for _ in t:
    xSingle.append(l*np.cos(omega * _))
    ySingle.append(l*np.sin(omega * _))