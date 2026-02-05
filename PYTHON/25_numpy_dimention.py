import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
e=np.array([1, 2, 3, 4], ndmin=10)

print(a)
print('number of dimensions :',a.ndim)

print(b)
print('number of dimensions :',b.ndim)

print(c)
print('number of dimensions :',c.ndim)

print(d)
print('number of dimensions :',d.ndim)

print(e)
print('number of dimensions :',e.ndim)