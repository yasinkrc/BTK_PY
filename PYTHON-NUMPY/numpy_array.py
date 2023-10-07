import numpy as np


# result=np.array([1,3,5,7,9]) # Burada elemanları kendimiz belirliyoruz 
#ama otomotik olarak da kendin de bir şeyler yapabilirsin 
# result=np.arange(1,10)
# result=np.arange(1,100,10)
# result=np.zeros(10) #float cinsinden geliyorlar bak 
# result=np.ones(10) 

# result=np.linspace(0,100,5) bu o aralığı istenilen parametre nezdinde bölüyor ve artış sağlıyor 
result=np.linspace(0,5,5)
result=np.random.randint(0,10)
result=np.random.randint(20)
result=np.random.randint(1,10,3)
print(result)
result=np.random.rand(1,100,2) #100 tane 2 şer adet sayılar  0-1 arası sayı
result=np.random.randn(5) #[ 0.05929523 -1.63823034  0.57625163 -0.76735954 -0.23779114]
np_array=np.arange(50)
np_multi=np_array.reshape(5,10)
# print(np_multi.sum(axis=1))
# print(np_multi.sum(axis=0))

rnd_numbers=np.random.randint(1,100,10) #[ 5 64 78 99 40 79 93 85 45 20]
result=rnd_numbers.max()
result=rnd_numbers.min()
result=rnd_numbers.mean() #ortalamasını sana verir en büyüğü hangisi ise 
result=rnd_numbers.argmax() #sana o sayının (en buyuk) indeksini verir 
result=rnd_numbers.argmin() #sana o sayının (en en küçük ) indeksini verir 
# print(result)

# print(result)