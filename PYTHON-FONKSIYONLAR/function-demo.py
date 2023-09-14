#1-Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın 
def yazdır(kelime,adet):
    print(kelime*adet)
yazdır("Merhaba\n",10)
#2-Kendine Gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız
def listeyeCevir(*params):
    liste=[]
    for param in params:
        liste.append(param)
    return liste
a=listeyeCevir(10,20,"Yasin","karaca",45,'f')
print(a)

#3-Gönderilen 2 sayı arasındaki tüm asal sayıları bulun 

def asalSayılariBul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi>1:
            for i in range(2,sayi):
                if (sayi%i==0):
                    break
            else :
                print(sayi)

# sayi1=int(input("Sayi 1 : "))
# sayi2=int(input("sayi 2 :"))
asalSayılariBul(4,5)
#4-Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız

    
def tam_Bol(sayi):
    for i in range(1, sayi + 1):
        if sayi % i == 0:
            print(i)

sayi = int(input("Sayı giriniz: "))
tam_Bol(sayi)

     