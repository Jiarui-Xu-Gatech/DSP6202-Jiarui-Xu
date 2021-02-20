import numpy as np
import math
import matplotlib.pyplot as plt

def generateSinusoidal(amplitude, sampling_rate_Hz, frequency_Hz, length_secs, phase_radians):
    t=np.linspace(0., length_secs, num=int(sampling_rate_Hz*length_secs))
    x1=[]
    for t1 in t:
        x1.append(amplitude*math.sin(2*math.pi*frequency_Hz*t1+phase_radians))
    x=np.array(x1)
    return t,x

def generateSquare(amplitude, sampling_rate_Hz, frequency_Hz, length_secs, phase_radians):
    t=np.linspace(0., length_secs, num=int(sampling_rate_Hz*length_secs))
    x=np.zeros(len(t))
    for k in range(1,11):
        t2,x2=generateSinusoidal(amplitude, sampling_rate_Hz, (2*k-1)*frequency_Hz, length_secs, phase_radians)
        x=x+((4/math.pi)*x2/(2*k-1))
    return t,x

t,x=generateSquare(1.0,44100,400,0.5,0)#0.5seconds can be output
plt.plot(t,x,label='Generate_Square')
plt.legend()
plt.xlabel('time/s')
plt.ylabel('amplitude')
plt.show()
