import pandas as pd 
import numpy as np

data = {
    "Colum1": [1,2,3,4,5],
    "Colum2": [10,20,13,20,25],
    "Colum3": ["abc","bcaa","ade","cb","dea"]
}

df=pd.DataFrame(data)

def kareAl(x):
    return x*x 

kareAl2=lambda x:x*x

result=df
result=df["Colum2"].unique()
result=df["Colum2"].nunique() #kaç tane tekil sayı varsa 
result=df["Colum2"].value_counts()
result=df["Colum1"]*2
result=df["Colum2"].apply(kareAl) #Obje olarak 
result=df["Colum2"].apply(kareAl2) #Obje olarak 
result=df["Colum2"].apply(lambda x:x*x) #Obje olarak 
# result=df["Colum2"].apply(len) #Obje olarak 

# df["Colum4"]=df["Colum2"].apply(len) hata veriyor güncelemden buyük ihtimale 

result=df.columns
result=len(df.columns)
result=df.index #RangeIndex(start=0, stop=5, step=1)
result=len(df.index)
result=df.info
result=df.sort_values("Colum2")
result=df.sort_values("Colum3")
result=df.sort_values("Colum3",ascending=False)


data = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data) 
df=df.pivot_table(index="Ay",columns="Kategori",values="Gelir")
print(df)