#numpy: numerical python
#library, for mathematics

import numpy as np

vector = np.array([2, 4, 5])
print(type(vector)) # <class 'numpy.ndarray'>
#ndarray: N-dimensional array

vector = np.array([[1, 2], [3, 4]])
print(type(vector))  # <class 'numpy.ndarray'>


#attributes
a = np.array([10, 30, 50, 10, 30, 50])

b = np.array([
    [10, 30, 70],
    [60, 70, 70]
])

print(b.ndim) #diving dimension, like 1d or 2d
print(b.shape) #giving order of array, i mean matrix
print(b.size) #order ❌ multiplication ✔️
print(b.dtype) #datatype arrayname[size];


