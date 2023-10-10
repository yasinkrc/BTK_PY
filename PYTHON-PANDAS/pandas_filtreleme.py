import pandas  as pd 
import numpy as np

data =np.random.randint(10,100,75).reshape(15,5)
df=pd.DataFrame(data,columns=["Colum1","Colum2","Colum3","Colum4","Colum5"])
result=df
result=df.columns
result=df.head() #ilk beş colum
result=df.head(10)
result=df.tail() #son 5 colum 
result=df.tail(10)
result=df["Colum1"]
result=df["Colum1"].head() #colum1 in ilk 5 colonu 
result=df.Colum1.head() #Yukardaki ile aynı sonucu verir yazmana gerek ama yazarsan okunabilirliğini artırır
result=df[["Colum1","Colum2"]]
result=df[["Colum1","Colum2"]].head()
result=df[["Colum1","Colum2"]].tail()
result=df[5:15][["Colum1","Colum2"]].head()
result=df[5:15][["Colum1","Colum2"]].tail()

""" Şeçmeyi öğrendik peki belli bir kritere göre nasıl seçeriz """ 

result =df>50 #True - False 
result=df[df>50]
result=df[df%2==0]
result=df["Colum1"]>50
result=df[df["Colum1"]>50]
result=df[df["Colum1"]>50]["Colum1"]
result=df[df["Colum1"]>50][["Colum1","Colum2"]]
result=df[(df["Colum2"]>50) & (df["Colum1"]<=70)]
result=df[(df["Colum1"]>50) & (df["Colum2"]<=70)]
result=df[(df["Colum1"]>50) | (df["Colum2"]<=70)]
result=df[(df["Colum1"]>50) | (df["Colum2"]>=70)][["Colum1","Colum2"]]

""" Daha kısa bir yöntem de  var """
result=df.query("Colum1 >=50 & Colum1%2==0")
result=df.query("Colum1 >=50 & Colum1%2==0")[["Colum1","Colum3"]]

print(result)