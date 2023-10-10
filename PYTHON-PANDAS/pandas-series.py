import pandas as pd 
import numpy as np 
#data 

numbers=[20,30,40,50]
numbers_array=np.array([20,30,40,50])

letters=['a','b','c','d']
letters=['a','b','c','d',1,2,85]
scala=5
dict={'a':10 ,'b':20,'c':30,'d':40}
random_numbers=np.random.randint(10,100,6)

# pandas_series=pd.Series() bir tane obje oluşturur
# pandas_series=pd.Series(letters)  
# pandas_series=pd.Series(numbers)
pandas_series=pd.Series(scala)
pandas_series=pd.Series(scala,[0,1,2,3,4,5])
pandas_series=pd.Series(scala,[1,2,3,4,5]) # buradd kaçran verirsen öyle devam eder 
# pandas_series=pd.Series(numbers,['a','b','c','d','e']) #ValueError: Length of values (4) does not match length of index (5)
pandas_series=pd.Series(numbers,['a','b','c','d']) #diziler için sıkıntu çıkar 
pandas_series=pd.Series(numbers,'a') #Bu ikiside hata verir index orantılı olmak zorunda 
print(pandas_series)
pandas_series=pd.Series(numbers,5)  #By ikiside hata verir 
""" scala 
1    5
2    5
3    5
4    5
5    5


"""
""" 
0    a
1    b
2    c
3    d
"""
# pandas_series=pd.Series(dict) #hepsini okur ama indeks almaz zaten indeksleri var 
# pandas_series=pd.Series(dict,[1,2,3,4]) #hepsini okur ama  ama değelere nan yazar 
# pandas_series=pd.Series(dict,[1,2,3,4,5,6]) #hepsini okur ama nan yazar bide fazla yazar
# pandas_series=pd.Series(random_numbers)

# result=pandas_series[0]
# result=pandas_series[-1]
# result=pandas_series[0]
# result=pandas_series[0:3]
# result=pandas_series[::]
# result=pandas_series['a']
# result=pandas_series['d']
result=pandas_series[['a','d']] #dikkat parantez içinde parantez kullanman gerek 
result=pandas_series.ndim
result=pandas_series.dtype
result=pandas_series.shape
result=pandas_series.sum()
result=pandas_series.min()
result=pandas_series.max()
result=pandas_series.mean()
result=pandas_series+pandas_series
result=pandas_series+50
result=np.sqrt(pandas_series)
result=pandas_series>=50
result=pandas_series[pandas_series%2==0]
result=pandas_series%2==0

# print(pandas_series)
# print(result)
# print(type(pandas_series))

opel2018=pd.Series([20,30,40,10],['astra','corsa','mokka','insinga'])
opel2019=pd.Series([40,30,20,10],['astra','corsa','Grandland','insinga'])

total=opel2018+opel2019
""" 
Grandland     NaN
astra        60.0
corsa        60.0
insinga      20.0
mokka         NaN

# """
# print(total)
# print(total['astra'])
