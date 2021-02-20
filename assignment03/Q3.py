import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, show

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

def computeSpectrum(x,sample_rate_Hz):
    transformed = np.fft.fft(x)
    XAbs1=[]
    XPhase1=[]
    XRe1=[]
    XIm1=[]
    f1=[]
    for item in transformed:
        XAbs1.append((item.real*item.real+item.imag*item.imag)**0.5)
        XPhase1.append(np.angle(item))
        XRe1.append(item.real)
        XIm1.append(item.imag)
    XAbs=np.array(XAbs1[:int(len(XAbs1)/2)])
    XPhase=np.array(XPhase1[:int(len(XPhase1)/2)])
    XRe=np.array(XRe1[:int(len(XRe1)/2)])
    XIm=np.array(XIm1[:int(len(XIm1)/2)])
    f=np.linspace(0., 44100,len(XAbs))
    return f,XAbs,XPhase,XRe,XIm
        

'''t,x=generateSquare(1.0,44100,400,0.05,0)
f,XAbs,XPhase,XRe,XIm=computeSpectrum(x,44100)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
ax1.plot(f,XAbs,'b.-')
ax1.set_title('FFT of Square Wave')
ax1.set_ylabel('Magnitude')
ax2.plot(f,XPhase, 'g')
ax2.set_xlabel('frequncy/Hz')
ax2.set_ylabel('Phase(radians)')
plt.legend(loc='best')
show()'''


t,x=generateSinusoidal(1.0,44100,400,0.05,0)
f,XAbs,XPhase,XRe,XIm=computeSpectrum(x,44100)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
ax1.plot(f,XAbs,'b.-')
ax1.set_title('FFT of Sine Wave')
ax1.set_ylabel('Magnitude')
ax2.plot(f,XPhase, 'g')
ax2.set_xlabel('frequncy/Hz')
ax2.set_ylabel('Phase(radians)')
plt.legend(loc='best')
show()
