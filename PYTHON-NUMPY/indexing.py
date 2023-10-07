import  numpy as np 



numbers=np.arange(0,80,5)
result=numbers[5]
result=numbers[-1]
result=numbers[0:3] #[ 0  5 10]
result=numbers[3:] 
result=numbers[::] 
result=numbers[::-1] 
numbers=np.arange(0,80,5).reshape(4,4)
result=numbers[0]
result=numbers[1]
result=numbers[2]
result=numbers[3][3]
result=numbers[1,2] #dikkkat önemli 
result=numbers[0,0] #dikkkat önemli 
# result=numbers[4] okumaz çünkü indeksi geçtik 
result=numbers[:,2] #satır sütün  tek eleman alır 
result=numbers[2,:] #sütün  satir tek eleman akır 
result=numbers[:,0:2] #tüm satırları al ama 1. ve 2. elemanlarıda al
""" 
[[ 0  5]
 [20 25]
 [40 45]
 [60 65]]
"""
result=numbers[-1,:] #son satırdaki tüm sütünlar 
result=numbers[:3,:3] #ilk 3 satır ve ilk 3 sutun 
result=numbers[:2,:2] #ilk 2 satır ve ilk 2 sutun 
# print(result)
# print(result)

# arr1=np.arange(0,10) #bunlar da referans yapılı 
# arr2=arr1 #ikide aynı yeri ve elemanları gösteriyor 
# print(arr1)
# print(arr2)
# print("değişikliten sonra ")
# arr2[0]=20
# print(arr1)
# print(arr2)
""" Eğer yaptığın diğeri üzerind bir değişiklik yapmasını istemiyorsan """ 
arr1=np.arange(0,10) 
arr2=arr1.copy() 
print(arr1)
print(arr2)
print("değişikliten sonra ")
arr2[0]=20
print(arr1)
print(arr2)