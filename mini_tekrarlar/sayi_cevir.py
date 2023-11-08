""" 
Problem: Sayıları Ters Çevirme
Verilen bir sayıyı tersine çeviren bir Python fonksiyonu yazın. 
Örneğin, 12345 sayısını girdi olarak alırsanız, fonksiyon 54321 sayısını döndürmelidir.

"""

def sayi (number) :
    
    number1=str(number)
    ters_sayi=""
    for i in number1 :
        
        ters_sayi=i+ters_sayi
    return ters_sayi
print(sayi(123))