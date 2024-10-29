import numpy as np
import matplotlib.pyplot as plt
duration=0.5
sample_rate=8000
frequency=200
num_samples=int(duration*sample_rate)
t=np.arange(num_samples)/sample_rate
sin_wave=np.sin(2*np.pi*frequency*t)
plt.plot(t,sin_wave,color='blue')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

duration=0.5
sample_rate=1000
frequency=200
num_sample=int(duration*sample_rate)
t=np.arange(num_samples)/sample_rate
sin_wave=np.sin(2*np.pi*frequency*t)
plt.plot(t,sin_wav)
plt.xlabel('time(s)')
plt.ylabel('amplitude')
plt.grid(False)
plt.show()

