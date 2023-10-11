import pandas as pd 
import numpy as np 


personeller = {
    'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [5000,3000,4000,3500,2750,6500,4500]
}

df=pd.DataFrame(personeller)
result=df
result=df["Maaş"].sum()
result=df.groupby("Departman") #Bir adet nesne dönderiyor  
result=df.groupby("Departman").groups
result=df.groupby("Semt") 
result=df.groupby("Semt").groups
result=df.groupby(["Semt","Departman"]).groups #ikisinde ortak olanları alır 
semtler=df.groupby("Semt")

# for name , group in semtler:
#     print(name)
#     print(group)

# for name , group in  df.groupby("Semt") :
#     print(name)
#     print(group)
    
""" 
Kadıköy
        Çalışan         Departman  Yaş     Semt  Maaş
0  Ahmet Yılmaz  İnsan Kaynakları   30  Kadıköy  5000
6   Mustafa Can  İnsan Kaynakları   42  Kadıköy  4500

Maltepe
         Çalışan    Departman  Yaş     Semt  Maaş
2  Hasan Korkmaz     Muhasebe   45  Maltepe  4000
4      Ali Turan  Bilgi İşlem   23  Maltepe  2750

Tuzla
       Çalışan         Departman  Yaş   Semt  Maaş
1   Can Ertürk       Bilgi İşlem   25  Tuzla  3000
3  Cenk Saymaz  İnsan Kaynakları   50  Tuzla  3500
5  Rıza Ertürk          Muhasebe   34  Tuzla  6500


"""
result=df.groupby("Semt").get_group("Kadıköy")
result=df.groupby("Departman").get_group("Muhasebe")


  


 



print(result)
    
# print(result)