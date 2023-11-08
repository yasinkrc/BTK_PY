""" 
Soru: Tekrarlanan Harf ve Rakam Bulma
Bir cümle veya kelime veriliyor. 
Bu cümlede veya kelimenin içinde tekrarlanan harf ve rakamları bulan bir Python 
fonksiyonu yazın. Fonksiyon, tekrarlanan harf ve rakamları saymalı ve sonuçları 
bir sözlük olarak döndürmelidir. Örnek olarak, "Merhaba, benim adım GPT-3.5 ve bu bir 
örnek cümle." cümlesi verildiğinde, fonksiyon hangi harf ve rakamların kaç kez tekrarlandığını 
göstermelidir. 
Örneğin, {'m': 4, 'a': 4, 'e': 8, 'r': 4, 'b': 3, 'i': 4, 'n': 5, 'g': 1, 'p': 1, 't': 1, '3': 1, '5': 1, 'u': 2, 'c': 1, 'ü': 1, 'l': 1}
gibi bir çıktı vermelidir.

Bu soruyu çözerek, bir Python fonksiyonu kullanarak tekrarlanan harf ve rakamları nasıl bulabileceğinizi görmüş olursunuz.

"""

def tekrarlanan_harfler_ve_sayilar(cumle):
    tekrarlanan_harfler = {}
    tekrarlanan_sayilar = {}

    for karakter in cumle:
        if karakter.isalnum():  # Harf veya rakam mı?
            karakter = karakter.lower()  # Harf ve rakamları küçük harfe çeviriyoruz (büyük/küçük harf duyarlı olmasın diye)
            if karakter in tekrarlanan_harfler:
                tekrarlanan_harfler[karakter] += 1
            else:
                tekrarlanan_harfler[karakter] = 1

    return tekrarlanan_harfler

cumle = "merhaba ben yasin"
tekrarlanan = tekrarlanan_harfler_ve_sayilar(cumle)

print("Tekrarlanan harfler ve rakamlar:")
for karakter, sayi in tekrarlanan.items():
    print(f"{karakter}: {sayi}")
