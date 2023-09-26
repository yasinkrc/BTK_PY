liste=["1","2","5a","10b","abc","10","50"]

#1: liste elemanları içindeki sayısal değerleri bulunuz.

# for i in liste :
    
#     if i.isnumeric():
#         print(i)
#     else :
#         continue

# for x in liste :
#     try :
#         result=int(x)
#         print(x)
#     except ValueError :
#         continue
    


#Kullanıcı 'q' değerini girmedikçe aldığınız inputun sayı olduğundan 
#emin olunuz aksi halde hata mesajı yazın 

# while True :
#     sayi=input("sayi")
#     if sayi=='q':
#         break
    
#     try :
#         result=float(sayi)
#         print("Girdinğiniz sayı  : ",result)
#     except ValueError:
#         print ("geçersiz sayı ! ")
#         continue 



#Girilen parola içinde türkçe karekter hatası veriniz 

# turkce_karekterler='şçğüöıİ'

# parola=input("Parola ")
# for i in parola :
#     if i in turkce_karekterler:
#         raise  TypeError("Parola Türkçe karekter içeremez ! ")
#     else :
#         pass

# print("Geçerli parola ")

#Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için 
#hata mesajları verin 

# def _factorial(sayi):
#     try:
#         if sayi < 0:
#             raise ValueError("Girdiğin sayı sıfırdan küçük olamaz!")
#         carp = 1
#         if sayi == 0:
#             return 1
#         else:
#             while sayi >= 1:
#                 carp *= sayi
#                 sayi -= 1
#             return carp
#     except ValueError as hata:
#         return str(hata)

# result = _factorial(-5)
# print(result)

 
def faktoriyel(x):
    
    x=int(x)
    
    if x<0 :
        raise ValueError("Negatif değer ")
    
    result=1
    
    for i in range(1,(x+1)):
        
        result*=i
    return result

for x in [5,10,20,-3,'10a']:
    
    try  :
        y=faktoriyel(x)
    except ValueError as err:
        print(err)
        continue

    print((y))
    
        