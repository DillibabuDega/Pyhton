import numpy as np
from matplotlib import pyplot as plt

signal=[1,2,3,4,5]
l=2
dsignal=signal[::l]
print(signal)
print(dsignal)
plt.plot(signal,label='Original Signal')
plt.plot(dsignal,label='Downsampled signal')
plt.legend()
plt.show()
