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


def generateBlocks(x, sample_rate_Hz, block_size, hop_size):
    xList=x.tolist()
    lastnumber=len(xList)%hop_size#zero-pad the input signal appropriately for the last block
    if lastnumber<block_size:
        for i in range(block_size-lastnumber):
            xList.append(0)
    t1=[]
    t2=[]
    for i in range(int(len(xList)/hop_size)+1):
        if i*hop_size+block_size<=len(xList):
            t1.append(i*hop_size)
            t2.append(i*hop_size/sample_rate_Hz)
    t=np.array(t2)
    X=np.zeros((block_size,len(t)))
    for item in t1:
        for i in range(block_size):
            X[i][t1.index(item)]=xList[item+i-1]
    return t,X

def plotSpecgram(freq_vector, time_vector, magnitude_spectrogram):
  if len(freq_vector) < 2 or len(time_vector) < 2:
    return

  Z = 20. * np.log10(magnitude_spectrogram)
  Z = np.flipud(Z)
  
  pad_xextent = (time_vector[1] - time_vector[0]) / 2
  xmin = np.min(time_vector) - pad_xextent
  xmax = np.max(time_vector) + pad_xextent
  extent = xmin, xmax, freq_vector[0], freq_vector[-1]
  
  im = plt.imshow(Z, None, extent=extent, origin='upper')
  plt.axis('auto')
  plt.xlabel('time/s')
  plt.ylabel('frequncy/Hz')
  plt.title('Specgram')
  plt.show()

def mySpecgram(x,  block_size, hop_size,sample_rate_Hz, window_type):
    t,X=generateBlocks(x,sample_rate_Hz, block_size, hop_size)
    winHamming=np.zeros(block_size)
    winHamming2=np.hanning(block_size)
    winRec=np.zeros(block_size)
    for i in range(0,block_size):
        t2=float(i)/float(block_size)
        t2=t-0.5
        winHamming[i]=(25.0/46.0)+(21.0/46.0)*math.cos(math.pi*2*i)
        winRec[i]=1
    for i in range(0,len(X[i])):
        if window_type=='hann':
            for j in range(0,block_size):
                X[j][i]=X[j][i]*winHamming2[j]
        if window_type=='rect':
            for j in range(0,block_size):
                X[j][i]=X[j][i]*winRec[j]
    magnitude_spectrogram=np.zeros((int(block_size/2),len(t)))
    for i in range(0,len(t)):
        mag=[]
        transformedBefore=np.zeros(int(block_size))
        for j in range(int(block_size)):
            transformedBefore[j]=X[j][i]
        transformed=np.fft.fft(transformedBefore)[:int(block_size/2)]
        for item in transformed:
            mag.append((item.real*item.real+item.imag*item.imag)**0.5)
        for j in range(int(block_size/2)):
            magnitude_spectrogram[j][i]=mag[j]
        magNp=np.array(mag)
    freq_vector=np.linspace(0., 44100,int(block_size/2))
    time_vector=t
    plotSpecgram(freq_vector, time_vector, magnitude_spectrogram)
    return freq_vector, time_vector, magnitude_spectrogram

block_size=2048
t,x=generateSquare(1.0,44100,400,0.5,0)
freq_vectorRec, time_vectorRec, magnitude_spectrogramRec=mySpecgram(x,  2048, 1024, 44100, 'rect')
freq_vectorHann, time_vectorHann, magnitude_spectrogramHann=mySpecgram(x,  2048, 1024, 44100, 'hann')

    
