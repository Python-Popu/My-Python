



import numpy as np
import matplotlib.pyplot as plt


r = np.arange(0, 6.0, 0.01)



################################################

def function(r):
     theta = 4 * np.pi * r
     return theta
     
     
     
###################################################
     
     
     
     
ax = plt.subplot(111, polar=True)
ax.plot(function(r), r, color='r', linewidth=2)
ax.set_rmax(2.0)
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()






