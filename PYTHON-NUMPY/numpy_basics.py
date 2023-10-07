import numpy as np 

#python list
py_list=[1,2,3,4,5,6,7,8,9]
# numpy array 
np_array=np.array([1,2,3,4,5,6,7,8,9])

print(type(py_list))
print(type(np_array))

py_multi=[[1,2,3],[4,5,6],[7,8,9]] 
#Yukarıda yapılan mesela bu 3 tane bölgenin hava durumu olabilir Örneğin 

np_multi=np_array.reshape(3,3)

print(py_multi)
print(np_multi)

print(np_array.ndim) #kaç boyutlu 1 boyutlı
print(np_multi.ndim) #2 boyutlıu

print(np_array.shape) #kaça-kaç  1-1 matriks
print(np_multi.shape) #3-3 -- matriks 
