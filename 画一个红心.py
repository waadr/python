import math
import numpy as np
import matplotlib.pyplot as plt

p = math.pi
i = np.arange(0,4*p,p/180)
x = [ (16*math.sin(j))**3 for j in i ]
y = [ 13*math.cos(j) - 5*math.cos(2*j) - 2*math.cos(3*j) - math.cos(4*j) for j in i ]

plt.figure(figsize=(10, 10))
plt.plot(x,y,'r-')
plt.show()