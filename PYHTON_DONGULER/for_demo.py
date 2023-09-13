sayilar =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#Sayılar listesindeki hangi sayilar 3'ün katıdır 

for i in sayilar : 
    if i %3==0 : 
        print(i)
#Sayilar listesinde  sayıların toplamı kaçtır 

toplam=0

for i in sayilar :
    toplam=toplam+i

print("sayilar listesindeki sayilarin toplamı : ",toplam)
#Sayilar listesindeki tek sayilarin karesini alınız 

for i in sayilar :
    
    if i%2!=0 : 
        print(i**2)
        


sehirler=['kocaeli','istanbul','Ankara',"İzmir","Rize"]

#Şehirlerden hangileri en fazla 5 karekterlidir 

for sehir in sehirler:
    
    if len(sehir)<=5 :
        print(sehir)


ürünler=[
    
    {'name':'Samsung S6','price':'3000'},
    {'name':'Samsung S7','price':'4000'},
    {'name':'Samsung S8','price':'5000'},
    {'name':'Samsung S9','price':'6000'},
    {'name':'Samsung S10','price':'7000'},
]
    
#ürünlerin fiyatları toplamı nedir  ?

toplam=0
for urun in ürünler:
    toplam=toplam+int(urun['price'])

print(toplam)

#Ürünlerin fiyatı en fazla 5000 olan ürünleri gösteriniz .

for urun in ürünler :
    
    if int(urun['price'])<=5000 :
        print(urun['name'])