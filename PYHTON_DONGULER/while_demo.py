sayilar=[1,3,5,7,9,12,19,21,22,23,24,25,]

#1:Sayilar  listesini while ile ekrana yazdırın 
i=0
while i < len(sayilar):
    print(sayilar[i])
    i=i+1
# #2:Başlangıç ve bitiş değerlerini kulllanıcıdan alıp oradaki tüm teksayıları ekrana yazdırın
# bas=int(input("baslangic"))
# son=int(input("son"))

# while bas <=son :
#     if bas%2!=0:
#         print(bas)
#     bas=bas+1
# #3:1-100 arasındaki sayiları azalan şekilde yazdırın 
# i=99
# while i>1:
#     print(i)
#     i=i-1
    
    
#4:Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın 
number=[]
i=1
while i<6:
    sayi=int(input("Sayi giriniz lütfen"))
    number.append(sayi)
    i=i+1


for t in number:
    print(t)
#5:Kullanıcıdan alacağınız sınırsız ürün bilgisi urunler listesi içinde saklayın 
# **ürün sayısını kullanıcıya sorun 
# **dictionary listesi yapısı (name , price ) şeklinde olsun 
# **ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin 

urunler =[]
adet=int(input("kaç adet ürün istiyorsunuz"))

i=0

while (i<adet) :
  name=input("name")
  price=input("price")
  urunler.append({
      
      'name':name,
      'price':price
  })
  i+=1
  

for urun in urunler:
    print(f"Ürün adı : {urun['name']} ürün fiyatı {urun['price']}")