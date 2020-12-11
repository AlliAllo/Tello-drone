import sounddevice as sd
import scipy
import numpy as np
from scipy.io import wavfile as wav
from scipy.io.wavfile import write, read
from scipy import fftpack as scfft
from matplotlib import pyplot as plt

minimumVolume = 0.5
fs = 44100
seconds = 1
#sd.default.device = 1,6

H0 = [1280, 660,650,640]
H1 = [570,580,590,1140]
H2 = [520,510,1020,500]
H3 = [960,480,490,970]
H4 = [860,430,440,850]
H5 = [380,760,390,770]
H6 = [340,680,350,670]
H7 = [320,640,330,650]
H8 = [570,290,580,280]
H9 = [510,260,270,500]
H10 = [480,240,250,720]
H11 = [430,220,210,420]
H12 = [190,380,570,200]
H13 = [180,340,170,510]

while True:
    recording = sd.rec(int(fs*seconds),samplerate=fs,channels=1)

    sd.wait()
    write('output.wav', fs, recording)

    fs_rate, signal = read("output.wav")
    l_audio = len(signal.shape)
    N = signal.shape[0]
    secs = N / float(fs_rate)
    Ts = 1.0 / fs_rate
    t = scipy.arange(0, secs, Ts)
    FFT = abs(scipy.fft(signal))
    FFT_side = FFT[range(N // 2)]
    freqs = scipy.fftpack.fftfreq(signal.size, t[1] - t[0])
    fft_freqs = np.array(freqs)
    freqs_side = freqs[range(N // 2)]
    fft_freqs_side = np.array(freqs_side)

    volume = np.array(abs(FFT_side))
    audible = np.where(volume > minimumVolume)
    if freqs_side[audible].any():
        #highestFrequenzy = max[0])

        HighestAudibleFrequency = int(max(freqs_side[audible]))

        print(HighestAudibleFrequency)


        if HighestAudibleFrequency in H0:
            print("H0")
        if HighestAudibleFrequency in H1:
            print("H1")
        if HighestAudibleFrequency in H2:
            print("H2")
        if HighestAudibleFrequency in H3:
            print("H3")
        if HighestAudibleFrequency in H4:
            print("H4")
        if HighestAudibleFrequency in H5:
            print("H5")
        if HighestAudibleFrequency in H6:
            print("H6")
        if HighestAudibleFrequency in H7:
            print("H7")
        if HighestAudibleFrequency in H8:
            print("H8")
        if HighestAudibleFrequency in H9:
            print("H9")
        if HighestAudibleFrequency in H10:
            print("H10")
        if HighestAudibleFrequency in H11:
            print("H11")
        if HighestAudibleFrequency in H12:
            print("H12")
        if HighestAudibleFrequency in H13:
            print("H13")