import numpy as np

import scipy.io.wavfile as wavfile 

import scipy.signal as signal

import pyaudio

import wave

import matplotlib.pyplot as graph

def cor(aList,bList):

    mean1=np.mean(aList)

    mean2=np.mean(bList)

    st_dev_1=np.std(aList)

    st_dev_2=np.std(bList)

    ##print('mean1=',mean1,'mean2=',mean2)

    ##print(st_dev_1,st_dev_2)

    sg1=(aList-mean1)/(st_dev_1)

    sg2=(bList-mean2)/(st_dev_2)

    ##print('sg1=',sg1,'sg2=',sg2)

    ##print("sg1 max=",max(sg1),'sg2 max=',max(sg2))

    x=((signal.correlate(sg1,sg2)))/16000
    
    print(x)
    y=max(x)

    return y



s0=wavfile.read("C:\Users\Lenovo\Documents\Audacity\\rec0.WAV")
print(s0[1])
s1=wavfile.read("C:\Users\Lenovo\Documents\Audacity\\rec1.WAV")

s2=wavfile.read("C:\Users\Lenovo\Documents\Audacity\\rec2.WAV")

s3=wavfile.read("C:\Users\Lenovo\Documents\Audacity\\rec3.WAV")

s4=wavfile.read("C:\Users\Lenovo\Documents\Audacity\\rec4.WAV")

s5=wavfile.read("C:\Users\Lenovo\Documents\Audacity\\rec5.WAV")

s6=wavfile.read("C:\Users\Lenovo\Documents\Audacity\\rec6.WAV")

s7=wavfile.read("C:\Users\Lenovo\Documents\Audacity\\rec7.WAV")



FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 2
WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,

                rate=RATE, input=True,

                frames_per_buffer=CHUNK)

print "recording..."
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):

    data = stream.read(CHUNK)

    frames.append(data)

print "finished recording"

# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

# reading file
recording=wavfile.read("file.wav")
myrecording=recording[1]
print(myrecording)
graph.plot(myrecording)


x0=cor(myrecording,s0[1])

x1=cor(myrecording,s1[1])

x2=cor(myrecording,s2[1])

x3=cor(myrecording,s3[1])

x4=cor(myrecording,s4[1])

x5=cor(myrecording,s5[1])

x6=cor(myrecording,s6[1])

x7=cor(myrecording,s7[1])



x=[x0,x1,x2,x3,x4,x5,x6,x7]

print(x)

z=max(x)

print(z)



if z>.88:

    ##integration with arduino program

    print("Matched")

else :    

    print("Different signals")