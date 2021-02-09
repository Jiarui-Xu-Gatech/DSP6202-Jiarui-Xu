#If the length of 'x' is 200 and the length of 'h' is 100, what is the length of 'y' ?
#Answer:y's length will be 299

import numpy
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import time,datetime
import scipy
import wave
import io
from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io
from scipy import signal


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

def CompareConv(x, h):
    import time,datetime
    starty=time.time()
    y=myTimeConv(x,h)
    endy=time.time()
    durationy=endy-starty

    starty2=time.time()
    y2 = signal.convolve(x,h)
    endy2=time.time()
    durationy2=endy2-starty2
    
    m=(np.sum(y-y2))/len(y)
    mabs=(np.sum(abs(y-y2)))/len(y)
    stdev=(np.sum((y-y2)*(y-y2)))/len(y)
    time=np.array([durationy,durationy2])
    return m,mabs,stdev,time

def loadSoundFile(filename):
    num,dataSound=wavfile.read(filename)
    dataSound = dataSound.astype(np.float32)#to be float
    return dataSound
    
x=loadSoundFile('DSP6202-Jiarui-Xu/assignment02/audio/piano.wav')
h=loadSoundFile('DSP6202-Jiarui-Xu/assignment02/audio/impulse-response.wav')

m,mabs,stdev,time=CompareConv(x, h)
print('m=')
print(m)
print('mabs=')
print(mabs)
print('stdev=')
print(stdev)
print('time=')
print(time)

