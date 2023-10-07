import numpy as np 

numbers1=np.random.randint(10,100,6)
numbers2=np.random.randint(10,100,6)

# print(numbers1) #[83 58 11 49 16 64]
# print(numbers2) #[42 42 24 27 93 17]

result=numbers1+numbers2 #[125, 100,  35,  76, 109,  81]
result=[numbers1+numbers2] #[array([125, 100,  35,  76, 109,  81])]
result=numbers1+10 #Hepsine 10 eklenir  [107  82  66  76  88  88]
result=numbers1-numbers2 #çıkarılır   [ 27 -57  -8 -50 -16  37]
result=numbers1-10 #hepsinden 10 çıkarılır   [22  4 63 64 63 60]
result=numbers1*numbers2 # Her eleman birbiriyle çarpılır [4307  252 1216 2304  240 4964]
result=numbers1*10 # hepsi 10 ile çarpılur [750 290 720 590 700 100]
result=numbers1/10 # hepsi 10 ile böler  [750 290 720 590 700 100]
result=np.sin(numbers1) #hepsinin sinisunu alur 
result=np.cos(numbers1) #hepsinin cosinüsü alır 
result=np.sqrt(numbers1) #her bir elemanın karekökünü alır 
result=np.log(numbers1) #her bir elemanın logoritmasnı alır   

# numbers1=numbers1.reshape(2,3)
numbers2=numbers1.reshape(2,3)
print(numbers1)
print(numbers2)
# result=np.vstack((numbers1,numbers2)) #tek parametre şeklinde ver bunları sana bunları matriks yapra 
#mesela 2,3 idi 4 e 3 oldu  dikey olarak birleştirdi  
# result=np.hstack((numbers1,numbers2))  
##mesela 2,3 idi 2 e 6 oldu  yatay olarak birleştirdi  

result =numbers1>=50 

""" 
[[ True False False]
 [ True  True  True]]
"""

result=numbers1%2==0


print(result) 