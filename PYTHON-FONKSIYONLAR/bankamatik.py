#Bankamatik uygulaması 


sadikhesap={
    
    'ad':"Sadık Turan",
    'hesapNo':'13245678',
    'bakiye':3000,
    'ekHesap':2000
}
alihesap={
    
    'ad':"Ali Turan",
    'hesapNo':'123456789',
    'bakiye':2000,
    'ekHesap':1000
}
def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    
    if hesap['bakiye']>=miktar:
        hesap['bakiye']-=miktar
        bakiyeSorgula(hesap)
        print("paranızı alabilirsiniz")
    
    else :
        toplam=hesap['bakiye']+hesap['ekHesap']
        
        if toplam>=miktar:
            ekHesapKullanimi=input("Ek hesap kullanılsın mı ? (e/h)")
            
            if ekHesapKullanimi=='e':
                ekHesapKullanilacakMiktar=miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekHesap']-=ekHesapKullanilacakMiktar
                
                print("paranızı alabilirsiniz")
                bakiyeSorgula(hesap)

            else :
                print(f"{hesap ['hesapNo']} nolu hesabınızda  {hesap['bakiye']}bulunmaktadır ")
        else :
            print("Üzgünüz bakiye yetersizdir")
            bakiyeSorgula(hesap)


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır .Ek Hesap limitiniz ise {hesap['ekHesap']} TL bulunmkatdır")

paraCek(sadikhesap,3000)
# bakiyeSorgula(sadikhesap)
paraCek(sadikhesap,2000)
# bakiyeSorgula(sadikhesap)
