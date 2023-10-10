import pandas as pd 
from numpy.random import randn

df=pd.DataFrame(randn(3,3),index=["A","B","C"],columns=['Colum1','Colum2','Colum3'])
result=df
result=result["Colum1"] #Kolonları seçme 
# print(type(result)) --><class 'pandas.core.series.Series'>
result=df[["Colum1","Colum2"]] #Kolonları Seçme 

#loc ['row','column'] => loc["row"]=> loc[":","column"] #Önemli bir nokta 
result=df.loc["A"] # Burada ise sana satırlar gelir  her satırın ilk elemanı seri şeklinde gellir 
""" 
Colum1    0.820337
Colum2   -0.731280
Colum3    0.864776

"""

# print(type(df.loc["A"])) <class 'pandas.core.series.Series'>

result=df.loc[:,"Colum1"]
result=df.loc[ : ,["Colum1","Colum2"]] #Önemli Noktalardan biri  iki sutunu alırsın 
result=df.loc[:,"Colum1":"Colum2"]


#Ara 
result=df.loc[:,:"Colum2"]

result=df.loc["A",:"Colum2"]
result=df.loc["A":"C",:"Colum2"]
result=df.loc[:"B","Colum1":"Colum2"] #Bak buralarda dikkat etmen gereken 2 nokta var bunlardan biri
# evet A  , B gibi harfler kullanıyoruz ama bu indeksleri biz belirledik

# result=df.loc[2] hata verdi 
""" ama kullanmak istersen """
result=df.iloc[2]
result=df.loc["A","Colum1"]
result=df.loc["C","Colum2"]
result=df.loc[["A","B"],["Colum1","Colum2"]]

""" Peki yeni bir satır yeni bir kolan eklemek istersek """

df["Colum4"]=pd.Series(randn(3),["A","B","C"])
df["Colum5"]=df["Colum1"]+df["Colum4"]

""" Peki yeni bir satır yeni bir kolan silmek istersek """

# print(df.drop("Colum5",axis=1)) #orjinalnde değişen bir şey olmadı 
# print(df)

""" Peki orjinalinde değişiklik yapmak istersek  """
result=df.drop("Colum5",axis=1)
# print(result)
print(df)
result=df.drop("Colum5",axis=1,inplace=True)
print(df)

""" Yukarıddakinin en büyük nedeni bir nesne döndürüyor ve onun üzerinde değişiklik yapma şansımız var """ 

# print(result)