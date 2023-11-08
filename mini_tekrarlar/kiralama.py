""" 
Problem: Araç Kiralama Sistemi

Bir araç kiralama sistemi tasarlamalısınız. Bu sistem, farklı türde araçları (örneğin, otomobil, kamyonet, motosiklet) ve müşterileri temsil eden sınıfları içermelidir. Ayrıca, kiralama işlemlerini yöneten bir sınıf da oluşturmalısınız.

Aşağıdaki gereksinimleri karşılayan bir sınıf yapısı oluşturmalısınız:

Araç sınıfı: Bu sınıf, araçların temel özelliklerini ve metodlarını içermelidir. Her aracın plaka numarası, marka, model, yıl, kiralama fiyatı gibi özellikleri olmalıdır. Ayrıca, aracın kiralanabilir durumu (kirada mı değil mi) takip edilmelidir.

Farklı araç türlerini temsil eden alt sınıflar oluşturun (örneğin, Otomobil, Kamyonet, Motosiklet). Bu alt sınıflar, ana Araç sınıfını kalıtım yoluyla almalıdır ve kendi özel özelliklerini içermelidir (örneğin, otomobilin yolcu kapasitesi, kamyonetin taşıma kapasitesi).

Müşteri sınıfı: Bu sınıf, müşterilerin temel bilgilerini (ad, soyad, telefon numarası) içermelidir.

Kiralama sınıfı: Bu sınıf, kiralama işlemlerini yönetmelidir. Müşteriler, belirli bir süre boyunca belirli bir aracı kiralayabilmelidir. Bu sınıf, kiralanabilir araçları, müşterileri ve kiralama işlemlerini yönetmelidir. Kiralama işlemi gerçekleştiğinde, araç kiralandı olarak işaretlenmeli ve kiralama süresi boyunca hesaplamalar yapılmalıdır (toplam kira ücreti, kalan süre vb.).

Bu problem, OOP prensiplerini kullanarak farklı sınıfların oluşturulmasını ve kalıtımın nasıl kullanılacağını anlamanıza yardımcı olacaktır. İyi şanslar!

"""   

class Araç:
    def __init__(self, plaka, marka, model, yıl, kiralama_fiyatı):
        self.plaka = plaka
        self.marka = marka
        self.model = model
        self.yıl = yıl
        self.kiralama_fiyatı = kiralama_fiyatı
        self.kirada = False

    def kirala(self):
        if not self.kirada:
            self.kirada = True
            return f"{self.marka} {self.model} aracı kiralama işlemi başarıyla tamamlandı."
        else:
            return f"{self.marka} {self.model} aracı zaten kirada."

    def iade(self):
        if self.kirada:
            self.kirada = False
            return f"{self.marka} {self.model} aracı iade edildi. Toplam kira ücreti: {self.kiralama_fiyatı} TL."
        else:
            return f"{self.marka} {self.model} aracı zaten kirada değil."

class Otomobil(Araç):
    def __init__(self, plaka, marka, model, yıl, kiralama_fiyatı, yolcu_kapasitesi):
        super().__init__(plaka, marka, model, yıl, kiralama_fiyatı)
        self.yolcu_kapasitesi = yolcu_kapasitesi

class Kamyonet(Araç):
    def __init__(self, plaka, marka, model, yıl, kiralama_fiyatı, taşıma_kapasitesi):
        super().__init__(plaka, marka, model, yıl, kiralama_fiyatı)
        self.taşıma_kapasitesi = taşıma_kapasitesi

class Motosiklet(Araç):
    def __init__(self, plaka, marka, model, yıl, kiralama_fiyatı, motor_hacmi):
        super().__init__(plaka, marka, model, yıl, kiralama_fiyatı)
        self.motor_hacmi = motor_hacmi

class Müşteri:
    def __init__(self, ad, soyad, telefon):
        self.ad = ad
        self.soyad = soyad
        self.telefon = telefon

    def kira_yap(self, araç, süre):
        if not araç.kirada:
            araç.kirala()
            return f"{self.ad} {self.soyad}, {süre} günlük kiralama işlemi başarıyla tamamlandı. Toplam kira ücreti: {araç.kiralama_fiyatı * süre} TL."
        else:
            return f"{self.ad} {self.soyad}, seçilen araç zaten kirada."

# Örnek kullanım
oto1 = Otomobil("34 ABC 123", "Ford", "Focus", 2020, 150, 5)
kam1 = Kamyonet("34 XYZ 456", "Mercedes", "Sprinter", 2019, 200, 1500)
moto1 = Motosiklet("34 DEF 789", "Honda", "CBR600RR", 2021, 100, 600)

musteri1 = Müşteri("Ahmet", "Yılmaz", "555-555-55-55")

print(musteri1.kira_yap(oto1, 3))
print(musteri1.kira_yap(kam1, 2))
print(musteri1.kira_yap(moto1, 5))

print(oto1.iade())
print(kam1.iade())
print(moto1.iade())
