import numpy as np
from matplotlib import pyplot as plt
x=[1,2,3,4,5]
y=[]
sum=0
for i in x:
	y.append(i)
for j in y:
	sum=sum+j
plt.plot(y)
plt.show()
plt.plot(x)
plt.show()
