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

t,x=generateSinusoidal(1.0,44100,400,0.5,(math.pi)/2)#0.5seconds can be output
plt.plot(t,x,label='Generate_Sinusoidal')
plt.legend()
plt.xlabel('time/s')
plt.ylabel('amplitude')
plt.show()
