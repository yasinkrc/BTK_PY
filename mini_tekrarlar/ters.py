""" 
Problem: Kelime Ters Çevirme
Bir kullanıcının girdiği bir kelimeyi tersine çeviren bir Python fonksiyonu yazın. 
Örneğin, "merhaba" kelimesini girdi olarak alırsanız, fonksiyon "abahrem" kelimesini döndürmelidir. 
Fonksiyonun sadece bir kelimeyi ters çevirmesi ve boşlukları, 
noktalama işaretlerini veya diğer karakterleri dikkate almaması gerekir.

"""
def kelime_ters_cevir(kelime):
    ters_ceviri = {
        'a': 'a',
        'b': 'b',
        'c': 'c',
        'd': 'd',
        'e': 'e',
        'f': 'f',
        'g': 'g',
        'h': 'h',
        'i': 'i',
        'j': 'j',
        'k': 'k',
        'l': 'l',
        'm': 'm',
        'n': 'n',
        'o': 'o',
        'p': 'p',
        'q': 'q',
        'r': 'r',
        's': 's',
        't': 't',
        'u': 'u',
        'v': 'v',
        'w': 'w',
        'x': 'x',
        'y': 'y',
        'z': 'z',
    }

    ters_kelime = ''
    for harf in kelime:
        ters_harf = ters_ceviri.get(harf, '')
        ters_kelime = ters_harf + ters_kelime

    return ters_kelime

kelime = "merhaba"
ters_kelime = kelime_ters_cevir(kelime)
print(ters_kelime)
