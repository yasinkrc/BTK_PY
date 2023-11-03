
print("_________")
print("/","*"," ","*","\\")
print("  \\",".","/")
""" 
print(" ilk notunuzu giriniz ")
not1=int(input("not 1 "))
print(" ikinci notunuzu giriniz ")
not2=int(input("not 2"))
print(" Üçüncü  notunuzu giriniz ")
not3=int(input("not 3 "))

ortalama=(not1+not2+not3)/3
if ortalama>=60 :
    print(f'Tebrikler geçtiniz ve ortalamanız : {ortalama} ')
elif ortalama ==50 :
    print(f"Geçmek için son bir sınav hakkın var ve ortalamanız : {ortalama} ")
else :
    print(f"Ne yaziki kaldınız ve ortalamanız : {ortalama}")
"""

"""   
import  datetime

Doğum_tarihi=input("Doğum Tarihinizi giriniz (gün/ay/yıl) formatında  : ")

tarih=Doğum_tarihi.split("/")
gün=int(tarih[0])
ay=int(tarih[1])
yıl=int(tarih[2])

print(gün)
print(ay)
print(yıl)
tarih_=datetime.datetime(yıl,ay,gün)
now_=datetime.datetime.now()
yas=now_-tarih_
print((yas/365))
"""
"""   
not_=float(input("not : "))
if not_>=50 :
    print("tebrikler")
else :
    print("başarısız :(")
    
"""

"""
kullanıcı_adi=input("Kullanıcı adı : ")
password=int(input("Şifre  : "))
x="yasin"
y=123
if (kullanıcı_adi==x) and (password==y):
    print("tebrikler")
else :
    print("Tekrar deneyiniz ")
     
"""
list=list(range(150,44,-6))
print(list)