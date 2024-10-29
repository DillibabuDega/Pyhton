"""x='01100001'
print(x)
x='01100001'
text=chr(int(x,2))
print(text)
with open('binary_file.txt','r') as f:
	data=f.read()
	print(data)
with open('binary_file.txt','r') as f:
	data=f.read(8)
	while data!=' ':
		text=chr(int(dta,2))
		print(text,end='')
		data=f.read(8)"""
import numpy as np
signal=np.sin(2*np.pi*1*np.arange(0,0.01,0.001))
bits=4
max_val=np.max(signal)
min_val=np.min(signal)
step_size=(max_val-min_val)/(2**bits-1)
quantized_signal=np.round((signal-min_val)/step_size)
digital_bit_stream=[]
for val in quantized_signal:
	digital_bit_stream.extend([int(b)for b in format(int(val),'04b')])
print(digital_bit_stream)
