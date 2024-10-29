import numpy as np
import matplotlib.pyplot as plt
signal=np.sin(2*np.pi*1*np.arange(0,0.01,0.001))
bits=4
max_val=np.max(signal)
min_val=np.min(signal)
step_size=(max_val-min_val)/(2**bits-1)
quantized_signal=np.round((signal-min_val)/step_size)
digital_bit_stream=[]
for val in quantized_signal:
	digital_bit_stream.extend([int(b) for b in format(int(val),'04b')])
dequantized_signal=np.zeros(len(quantized_signal))
for i,val in enumerate(quantized_signal):
	dequantized_signal[i]=val*step_size+min_val
plt.plot(signal,label='Origianal signal')
plt.plot(dequantized_signal,label='Dequantized Signal(4-bit)')
plt.legend()
plt.show()
