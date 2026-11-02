#easy way of making arrays

import numpy as np

#1. np.zeros(size, dtype)
a = np.zeros(10)
print(a)

#2. np.ones(size, dtype)
b = np.ones(14, int)
print(b)

#3. np.arrange(start, stop, step)
#simple way of writing list(range()), but it is array
c = np.arange(1, 13, 3)
print(c) #exclude stop

#4. np.linspace(start, stop, number)
d = np.linspace(0, 10, 2)
print(d)
#include stop, and it is compulsory, just exlusive of two cases
#a. where number = 1
#b. np.linspace(0, 10, 5, endpoint=False), other argument
np.linspace(0, 10, 5, endpoint=False)

#also, it only give dtype float even there are only integers, but the case for default,
#we can change that with, dtype
e = np.linspace(0, 10, 2, dtype = int)
print(e)
