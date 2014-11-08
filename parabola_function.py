



#import math as math
import matplotlib.pyplot as plt


#initiator
x =[0.0 for k in range(100)]
y =[0.0 for k in range(100)]

def function(x):
    
    for k in range(100):
       y[k] = x[k]*x[k]
    return y
    
# data creation
x = [0.1*k for k in range(100)]    
y = function(x)


##############################
plt.figure(1)
plt.scatter(x,y)
plt.show()




