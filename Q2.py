import scipy
import wave
import numpy as np
import io
from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io
import matplotlib.pyplot as plt
from scipy import signal


def crossCorr(x,y):
    '''squareX=0
    squareY=0
    squareXY=0
    sumX=0
    sumY=0
    sumMulti=0
    for i in range(len(x)):
        sumX=sumX+(x[i][0])
        sumY=sumY+(y[i][0])
    aveX=sumX/len(x)
    aveY=sumY/len(y)
    sum2X=0
    sum2Y=0
    for i in range(len(x)):
        sum2X=sum2X+(x[i][0]-aveX)*(x[i][0]-aveX)
        sum2Y=sum2Y+(y[i][0]-aveY)*(y[i][0]-aveY)
    squareX=(sum2X/len(x))**0.5
    squareY=(sum2Y/len(y))**0.5
    for i in range(len(x)):
        sumMulti=sumMulti+((x[i][0]-aveX)*(y[i][0]-aveY))#just need the left channel
    squareMulti=sumMulti/len(x)
    return squareMulti/(squareX*squareY)'''#the above do the same but not effient
    return signal.correlate(x, y, mode='full')
    
    
    

def loadSoundFile(filename):
    data_dir = pjoin(dirname(scipy.io.__file__), 'tests', 'data')
    wav_fname = pjoin(data_dir, filename)
    num,dataSound=wavfile.read(wav_fname)
    dataSound = np.delete(dataSound, -1, axis=1)#just need the left channel
    #Reduce sample accuracy to improve efficiency
    result=[]
    for i in range(0,len(dataSound),100):
        result.append(dataSound[i][0])
    dataResult = np.array(result)
    dataResult = dataResult.astype(np.float32)#to be float
    return dataResult


def findSnarePosition(snareFilename, drumloopFilename):
    x=loadSoundFile(snareFilename)
    y2=loadSoundFile(drumloopFilename)
    squareX=0
    squareY=0
    sumX=0
    sumY=0
    for i in range(len(x)):
        sumX=sumX+(x[i])
        sumY=sumY+(y2[i])
    aveX=sumX/len(x)
    aveY=sumY/len(y2)
    sum2X=0
    sum2Y=0
    for i in range(len(x)):
        sum2X=sum2X+(x[i]-aveX)*(x[i]-aveX)
        sum2Y=sum2Y+(y2[i]-aveY)*(y2[i]-aveY)
    squareX=(sum2X/len(x))**0.5
    squareY=(sum2Y/len(y2))**0.5#can use for nomaliozation

    z2=crossCorr(loadSoundFile(snareFilename),loadSoundFile(drumloopFilename))
    t = np.linspace(0.,4,len(z2))
    
    listy=z2.tolist()
    max=0
    for item in listy:
        if item>max:
            max=item
        elif -item>max:
            max=-item
    for i in range(len(listy)):
        item=listy[i]
        listy[i]=item/max
    listResult=[]
    for i in range(len(listy)):
        if listy[i]>=0.95 or -listy[i]>=0.95:
            listResult.append(i*4/len(listy))
    return listResult

print(findSnarePosition('snare.wav','drum_loop.wav'))#The unit of data here is seconds

file = open('02-snareLocation.txt','w')

file.write(str(findSnarePosition('snare.wav','drum_loop.wav')))

file.close()
