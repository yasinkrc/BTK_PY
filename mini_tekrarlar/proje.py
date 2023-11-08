
""" 

Problem: Banka Hesabı Sınıfı
Bir banka hesabı sınıfı oluşturmanız gerekiyor. Bu sınıf aşağıdaki işlevlere sahip olmalıdır:

Başlangıç bakiyesiyle bir banka hesabı oluşturabilme.
Para yatırma ve para çekme işlemlerini gerçekleştirebilme.
Hesap bakiyesini görüntüleyebilme.
Hesap geçmişini görüntüleyebilme (yani para yatırma ve çekme işlemlerini zaman sırasına göre kaydedebilme).
Banka Hesabı sınıfını oluşturup bu işlevleri uygulayarak, bir örnek hesap oluşturmalı ve bu hesabı kullanarak çeşitli işlemler gerçekleştirmelisiniz. Bu sınıf, OOP prensiplerini uygulamak için iyi bir egzersiz olabilir.

Unutmayın, bu problemi çözerken sınıf, metodlar, özellikler ve gerektiğinde özel metodlar kullanmanız gerekebilir. İyi şanslar!
"""
from datetime import datetime
class Banka_Hesabi :
    
    def __init__(self,baslangic_bakiye) :
        
        self.baslangic_bakiye=baslangic_bakiye
        self.para=0
        self.para+=self.baslangic_bakiye
        self.hesap_gecmisi=[]
    
    def para_yatirma(self,yatirim):
        simdi=datetime.now()
        self.para+=yatirim
        self.hesap_gecmisi.append([ {
            
            f"para_yatiridi :{yatirim}":f"{simdi}"
        }
            
            
        ])

        
    def para_cekme(self ,cekme):
        simdi=datetime.now()
        if self.para!=0 :
            
            self.para-=cekme
            self.hesap_gecmisi.append([{
                
                f"para_cekildi :{cekme}":f"{simdi}"
            }])
        else :
            print("Ne yaziki paraniz yok para çekemezsiniz :(")
        

    def hesap_goruntule(self):
        print(f"Şu anki bankadaki paraniz : {self.para} ")
           
    def hesap_gecmisi_genel(self):
        
        print(self.hesap_gecmisi)
        
    
banka=Banka_Hesabi(0)
banka.hesap_goruntule()
banka.para_cekme(5)

    


    
    
        
        
        
