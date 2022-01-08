# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 22:37:08 2020

@author: Iozzi
"""

import random
import math

random.seed()

import matplotlib.pyplot as plt
n = 1000
internal = 0
fig, ax = plt.subplots()
plt.show(block=False)

for i in range(n):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    d = x*x+y*y
    if d < 1:
        ax.plot([x],[y],'ro')
        internal = internal + 1
    else:
        ax.plot([x],[y],'bo')
    plt.pause(0.01)
    
pi_est = 4 * internal / n
print(pi_est)
print(abs(pi_est-math.pi))