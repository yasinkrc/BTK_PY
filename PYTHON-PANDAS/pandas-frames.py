import pandas as pd 

# df=pd.DataFrame([1,2,3,4])
# print(df)
# s1=pd.Series([3,2,0,1])
# s2=pd.Series([0,3,7,2])

# data=dict(apples=s1,oranges=s2)

# df=pd.DataFrame(data)
# print(df)

# df=pd.DataFrame([['ahmet',50],['ali',40],['yazgülü',20],['Ayse',10 ]]) #bunlar dict değil
data=[['ahmet',50],['ali',40],['yazgülü',20],['Ayse',10 ]]
dict={"Name":['Ahmet','Ali','Yağmur','Çınar'],'Grade':[50,60,70,80]}
# df=pd.DataFrame(data,columns=['isim','not'], index=[1,2,3,4],dtype=float) 
""" Verilerde Str de vr  bu yuzden kullanmamm gerek dtype = float diye 
"""
# df=pd.DataFrame(data,index=[1,2,3,4], columns=['isim','not'], dtype=float)
# df=pd.DataFrame(dict,index=[1,2,3,4]) #Bu formata daha hızlı ve daha kolay sonuç elde ederisin 

dict_list=[
    
    {'Name':'Ahmet','Grade':40},    
    {'ad':'Leyla','Grade':30},    
    {'Name':'Diyar','not':45},    
    {'isim':'Mehmet','Grade':60}    
]


df=pd.DataFrame(dict_list)
print(df)