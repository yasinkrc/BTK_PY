message="Hello There. My name is Yasin Karaca !"

result=message.split()
print(result)
sozluk1 = {"ad": "Ahmet", "yas": 30}
sozluk2 = {"sehir": "İstanbul", "meslek": "Mühendis"}

# Bir sözlüğü diğer sözlükle güncellemek için update kullanabiliriz.
sozluk1.update(sozluk2)

print(sozluk1)

my_set = {1, 2, 3}
my_list = [4, 5, 6]

# update yöntemi ile bir liste ekleyelim
my_set.update(my_list)

print(my_set)  # Çıktı: {1, 2, 3, 4, 5, 6}
"""

import  datetime

tarih=input("lütfen araç kayıt tarihini giriniz : format(11/09/1654)")

tarih=tarih.split('/')
x=tarih[2]
y=tarih[1]
z=tarih[0]
simdi=datetime.datetime.now()
trafige_cikis_tarihi=datetime.datetime(int(x),int(y),int(z))

fark=simdi-trafige_cikis_tarihi
print(fark.days) """
"""  
name ="Sadik turan "

for n in name:
    print(n,end="")

 """
tuple=[(1,2),(3,4),(5,6)]
dict={"k1":1,"k2":2,"k3":3}


"""                              
for key , value in tuple :
    print(key,end="")
    print(value,end="")
"""

for i , ı in dict.items():
    print(i," ",ı)