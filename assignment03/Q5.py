from scipy.signal import chirp, spectrogram
import matplotlib.pyplot as plt
import numpy as np

fs = 7200
T = 4
t = np.arange(0, int(T*fs)) / fs

def plot_spectrogram(title, w, fs):
    ff, tt, Sxx = spectrogram(w, fs=fs, nperseg=256, nfft=576)
    plt.pcolormesh(tt, ff[:145], Sxx[:145], cmap='gray_r', shading='gouraud')
    plt.title(title)
    plt.xlabel('t (sec)')
    plt.ylabel('Frequency (Hz)')
    plt.grid()

w = chirp(t, f0=1500, f1=250, t1=T, method='quadratic')
plot_spectrogram(f'Sine Sweep, f(0)=1500, f({T})=250', w, fs)
plt.show()
