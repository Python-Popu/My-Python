



#import math as math
import matplotlib.pyplot as plt


#initiator
x =[0.0 for k in range(100)]
y =[0.0 for k in range(100)]

# data creation
x = [0.1*k for k in range(100)]
for k in range(100):
    y[k] = x[k]*x[k]
    

plt.figure(1)
plt.scatter(x,y)
plt.show()
