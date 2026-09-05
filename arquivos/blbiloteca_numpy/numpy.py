import numpy as np
import time
a=np.array(([1,2,3,4,5,6],[3,4,5,6,7,8]))
print(a)
print(type(a))

zero_array=np.zeros(shape=(5,3,6))
print(zero_array)
um_array=np.ones(shape=(2,3))
print(um_array)

vazio=np.empty((3,4))
print(vazio)


arr=np.arange(50,200,30)
print(arr)

array_linear=np.linspace(0,100, num=40,retstep=True)
print(array_linear)
print(zero_array.shape)
print(zero_array.size)
print(zero_array.ndim)

