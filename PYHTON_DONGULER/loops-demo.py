""" 
1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı 
ifadeleri ile bulmaya çalışın (hak=5)

** random modülü için "python random" şeklinde arama yapın
** 100 üzerinden puanlama yapın . Her soru 20 puan 
** Hak bilgisini kullanıcıdan alın  ve her soru belirtilen can saysı üzerinden 
hesaplansınn 



"""

import random 

sayi=random.randint(1,10)

can=int(input("Kaç hak istiyorsunuz ? "))
hak=can
sayac=0
while hak>0 :
    hak-=1
    sayac+=1
    tahmin=int(input("tahmin"))
    
    if sayi==tahmin:
        print(f"tebrikler bildiniz {sayac}.defa da bildiniz Toplam puanınz {100-((100/can)*(sayac-1))} ")
        break 
    elif sayi >tahmin :
        print("yukarı")
    else :
        print("aşağı")
    
    if hak==0:
        print(f"hakkınız bitti ... tutulan sayı : {sayi}")
    