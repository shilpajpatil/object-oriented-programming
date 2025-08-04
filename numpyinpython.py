

import numpy as np



# Create a 1D array
"""
arr = np.array([1, 2, 3, 4])
print(arr)           
print(type(arr))    
"""

#-------------------------------------------Create a 2D array
"""
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)
"""
"""

zeros = np.zeros((3, 3)) 
print("all zeros inside array:", zeros)


ones = np.ones((2, 4))    # 2x4 array of ones
print("all ones inside array ", ones)


arr_range = np.arange(0, 10, 2)  # Values from 0 to 10, step 2
print("start end and steps:",arr_range)



identity = np.eye(3)  # 3x3 identity matrix
print(identity)
"""

#----------------------------------------Basic properties of numpy

arr = np.array([[1, 2, 3], [4, 5, 6]])   # two dimention array
"""

print("Finding shapeof array:",arr.shape) 

print("datatype of array based :",arr.dtype)  # Output: int64 you get system based output

 
print("print dimention of array:",arr.ndim)   

print("size of array",arr.size)   


print("0 row 1 column index value:",arr[0, 1])  
print("1 row 2 column index value: ",arr[1, 2])


print(arr[0, :])   # Output: [1 2 3] (first row)
print(arr[:, 1])   # Output: [2 5] (second column)

print(arr[:2, :2]) 
"""

print("sum of array elements:",arr.sum())        # Output: 21
print("mean of array elements:",arr.mean())       # Output: 3.5
print("max elements:",arr.max())        # Output: 6
print("min elements:",arr.min())        # Output: 1
print("standard deviation:",arr.std())        # Output: Standard deviation
print("sum of columns :",arr.sum(axis=0))  # Sum along columns: [5 7 9]
print("sum of rows:",arr.sum(axis=1))  # Sum along rows: [6 15]




