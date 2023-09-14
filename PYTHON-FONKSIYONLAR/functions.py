def sayHello(name="user-x"):
    return 'Hello' + name
    
a=sayHello("Çınar ")
b=sayHello("ADA ")
c=sayHello()

print(a)
print(b)
print(c)


def total(num1,num2):
    return num1+num2

result=total(10,20)
print(result)
result=total(15,20)
print(result)


def yasHesapla(dogumYili):
    return 2019-dogumYili

ageCinar=yasHesapla(2017)
print(ageCinar)
ageSeda=yasHesapla(2010)
print(ageSeda)
ageSena=yasHesapla(1999)
print(ageSena)

def EmekliligeKacYilKaldi(dogumYili,isim):
    '''
    DOCSTRING = Doğum yılınıza göre emekliliğinize kaç yıl kaldı 
    INPUT : Doğum yılı
    OUTPUT:Hesaplanan yıl bilgisi 
    
    '''
    yas=yasHesapla(dogumYili)
    emeklilik=65-yas
    
    if emeklilik>0 :
        print(f"emekliliğine {emeklilik} yıl kaldı")
    else:
        print("Zaten emekli oldunuz")


EmekliligeKacYilKaldi(1983,"ali")
EmekliligeKacYilKaldi(2135,"ahmet")
EmekliligeKacYilKaldi(1954,"ali")

print(help(EmekliligeKacYilKaldi))