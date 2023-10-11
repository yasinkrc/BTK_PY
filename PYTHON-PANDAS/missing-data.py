import pandas as pd 

import numpy as np 

data =np.random.randint(10,100,15).reshape(5,3)

df=pd.DataFrame(data,index=['a','c','e','f','h'],columns=['colum1','colum2','colum3'])

df=df.reindex(['a','b','c','d','e','f','g','h']) #Tekrardan indeksleme başlatır 

newColumn=[np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["newColumn"]=newColumn

""" 
a    59.0    46.0    25.0        NaN
b     NaN     NaN     NaN       30.0
c    55.0    50.0    92.0        NaN
d     NaN     NaN     NaN       51.0
e    72.0    91.0    96.0        NaN
f    10.0    32.0    43.0       30.0
g     NaN     NaN     NaN        NaN
h    49.0    26.0    76.0       10.0
"""
result=df
# result=df.drop("colum1",axis=1)
# result=df.drop(["colum1","colum2"],axis=1) kolon
# result=df.drop("a",axis=0)
# result=df.drop(["a","c","b"],axis=0) satırlar

result=df.isnull()
result=df.notnull()
result=df.isnull().sum()
result=df #kontrol ettim doğru 

result=df["colum1"].isnull().sum()
result=df #kontrol ettim doğru 
result=df["colum1"].isnull()
result=df[df["colum1"].isnull()]
result=df[df["colum1"].isnull()]["colum1"]
result=df[df["colum1"].notnull()]["colum1"]
result=df[df["colum1"].notnull()]


""" Satırlar için """


result=df.dropna() #varsayılan değeri  0 #yazmasan bile axis=0 olarak ayarlar  ve satırda bir tane bile Nan varsa siler 

result=df.dropna(axis=1) #axis = 1 => sütüna 

result=df.dropna(how="any") # yine gösterir 

result=df.dropna(how="all") # tüm satırda varsa ya da sütünda onu siler 
 

result =df.dropna(subset =["colum1","colum2"]) #--> buda hangi sütünlarda istediğini belirtit 
result =df.dropna(subset =["colum1","colum2"],how="all") #--> buda hangi sütünlarda istediğini belirtit 
result =df.dropna(subset =["colum1","colum2"],how="any") #--> buda hangi sütünlarda istediğini belirtit 

result=df.dropna(thresh=2) # en az ikki veri varsa silme bunları 
result=df.dropna(thresh=3) #satırlara bakar 
result=df.dropna(thresh=4) #satırlara bakar 


result=df.fillna(value="No input")
result=df.fillna(value=1)

result=df.sum() #her kolon kendi yağında kavurulma
result=df.sum().sum() #tum kolonlar kendi yağında kavrulma
result=df.size
result=df.isnull().sum()
result=df.isnull().sum().sum()

def ortalama(df):
    toplam=df.sum().sum()
    adet=df.size-df.isnull().sum().sum()
    
    return toplam/adet

result=df.fillna(value=ortalama(df))
print(result)
