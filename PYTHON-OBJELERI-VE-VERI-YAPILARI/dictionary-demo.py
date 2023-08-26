# 1- 3 ürün bilgisini (id,ad,fiyat) kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
# 2- Ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin.


ogrenciler={}

number=int(input("the number of student : "))
name=input(("the name of the student : "))
surname=input("the surname of the student : ")
phone=input("the phone number of the student : ")

# ogrenciler[number]={
#     'ad':name,
#     'soyad':surname,
#     'telefon':phone,

# }
number=int(input("the number of student : "))
name=input(("the name of the student : "))
surname=input("the surname of the student : ")
phone=input("the phone number of the student : ")
ogrenciler.update({ #update kullanırsan birde fazla kullanma hakkın var 
    number: {
        'ad':name,
        'soyad':surname,
        'telefon:':phone
    }
})
number=int(input("the number of student : "))
name=input(("the name of the student : "))
surname=input("the surname of the student : ")
phone=input("the phone number of the student : ")
ogrenciler.update({ #update kullanırsan birde fazla kullanma hakkın var 
    number: {
        'ad':name,
        'soyad':surname,
        'telefon:':phone
    }
})
number=int(input("the number of student : "))
name=input(("the name of the student : "))
surname=input("the surname of the student : ")
phone=input("the phone number of the student : ")
ogrenciler.update({ #update kullanırsan birde fazla kullanma hakkın var 
    number: {
        'ad':name,
        'soyad':surname,
        'telefon:':phone
    }
})
print(ogrenciler)


