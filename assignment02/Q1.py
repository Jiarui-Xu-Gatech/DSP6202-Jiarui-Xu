#If the length of 'x' is 200 and the length of 'h' is 100, what is the length of 'y' ?
#Answer:y's length will be 299

import numpy
import numpy as np
import matplotlib.pyplot as plt


def myTimeConv(x,h):
    y=[]
    for i in range(len(x)+len(h)):
        z=0
        if i<max(len(x),len(h)):
            for j in range(min(i+1,min(len(x),len(h)))):
                	z=z+h[j]*x[i-j]
        elif i>max(len(x),len(h)):
            for j in range(i-max(len(x),len(h)),min(len(x),len(h))):
                	z=z+h[j]*x[len(x)-1-(j-(i-max(len(x),len(h))))]
        if i!=max(len(x),len(h)):
            y.append(z)
    return np.array(y)

listx=[]
listh=[]
inh=0
for i in range(100):
    listx.append(1)
for i in range(25):
    inh=inh+i/25
    listh.append(inh)
listh.append(1)
for i in range(25):
    inh=inh-i/25
    listh.append(inh)
x=np.array(listx)
h=np.array(listh)
y=myTimeConv(x,h)

print(y)

t=np.linspace(0.,len(y),len(y))
plt.plot(t,y,label='convolution made by myself')
plt.legend()
plt.xlabel('index')
plt.ylabel('convolution for x and h')
plt.show()
