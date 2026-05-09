import numpy as np

arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(arr[0])

print(np.zeros((2,2)))

print(np.linspace(0,1,5))

x = np.array([[1, 2], [3, 4]])


m = np.asmatrix(x)

y = np.arange(35).reshape(5,7)
print(y)

print(y[np.array([0,2,4]), np.array([1,3,5])])
