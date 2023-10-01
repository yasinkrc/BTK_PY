#regular expressions 

import re 

# result=dir(re)
#genelde arama moodülüdür bellirl karekterler sonucunda 
#re module 
#1-re.finadall() --> O kelimeyi dizinde arar 
# result=re.findall("Python",str)
# result=len(result)

#2-re.split() --> Ayırma işlemi yapar 
# result=re.split(" ",str)
# result=re.split("R",str)

#3-re.sub() --> yer değiştirme yapar bize 
# result=re.sub(" ","-",str)
# result=re.sub("\s","-",str) --> \s - boşluk anlamına geliyor 

#4-re.search()
# result=re.search("Python",str)
# result=result.span()
# result=result.start()
# result=result.end()
# result=result.string --> burada parantez yok dikkat et 
#regular 

#regular expression 

str="Python Kursu: Python Programlama Rehperiniz | 40 saat taammam"

"""

    [] - Köşeli parantezler arasına yazılan bütün karakterler
         aranır.

         [abc] => a      : 1 match
                  ac     : 2 match 
                  Python : No matches

         [a-e]  => [abcde]
         [1-5]  => [12345]
         [0-39] => [01239] #DİKKAT burada dikkat et 0-3 ) --> 9 sabit kalır   

         [^abc] => abc dışındaki karakterler.
         [^0-9] => rakam olmayan karakterler.

"""

result=re.findall("[abc]",str) #['a', 'a', 'a', 'a', 'a']
result=re.findall("[sat]",str) #['t', 's', 't', 'a', 'a', 'a', 's', 'a', 'a', 't']
result=re.findall("[a-e]",str) #['a', 'a', 'a', 'e', 'e', 'a', 'a']
result=re.findall("[a-z]",str) #['y', 't', 'h', 'o', 'n', 'u', 'r', 's', 'u', 'y', 't', 'h', 'o', 'n', 'r', 'o', 'g', 'r', 'a', 'm', 'l', 'a', 'm', 'a', 'e', 'h', 'p', 'e', 'r', 'i', 'n', 'i', 'z', 's', 'a', 'a', 't']
result=re.findall("[0-5]",str) #['4', '0']
result=re.findall("[1-5]",str) #['4']
result=re.findall("[^abc]",str)#['P', 'y', 't', 'h', 'o', 'n', ' ', 'K', 'u', 'r', 's', 'u', ':', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', 'P', 'r', 'o', 'g', 'r', 'm', 'l', 'm', ' ', 'R', 'e', 'h', 'p', 'e', 'r', 'i', 'n', 'i', 'z', ' ', '|', ' ', '4', '0', ' ', 's', 't']
result=re.findall("[^0-9]",str)#['P', 'y', 't', 'h', 'o', 'n', ' ', 'K', 'u', 'r', 's', 'u', ':', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', 'P', 'r', 'o', 'g', 'r', 'a', 'm', 'l', 'a', 'm', 'a', ' ', 'R', 'e', 'h', 'p', 'e', 'r', 'i', 'n', 'i', 'z', ' ', '|', ' ', ' ', 's', 'a', 'a', 't']

"""
    . - Her hangi bir tek karakteri belirtir.

        .. => a    : No match
              ab   : 1 match
              abc  : 1 match
              abcd : 2 matches

    
"""

result = re.findall("...", str)
result = re.findall("Py..on", str)

"""
    ^ - Belirtilen string karakterlerle başlıyor mu ?

    ^a => a:    1 match
          abc:  1 match
          bac:  No match

"""

result=re.findall("^a",str)
result=re.findall("^P",str)

"""
    $ - Belirtilen karakterle bitiyor mu ?

    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match 

"""

result=re.findall("t$",str)
result=re.findall("saat$",str)
result=re.findall("saatt$",str)

"""
     * - Bir karakterin sıfır ya da daha fazla sayıda olmasını 
         kontrol eder

         ma*n => mn     : 1 match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""
result=re.findall("sa*t",str)
result=re.findall("Python*",str)
"""
     + - Bir karakterin bir ya da daha fazla sayıda olmasını 
         kontrol eder.

         ma+n => mn     : No match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""

result=re.findall("sa+t",str)

"""
    ? - Bir karakterin sıfır ya da bir kez olmasını 
        kontrol eder.

        ma+n => mn     : No match
                man    : 1 match
                maaan  : 1 match
                main   : No match (a' nın arkasına n gelmiyor.) 
"""

result=re.findall("sa?t",str)

"""
    {} - Karakter sayısını kontrol eder.

        al{2}   => a karakterinin arkasına l karakteri 2 kez tekrarlamalı.
        al{2,3} => a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlamalı.
        [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.
"""

result=re.findall("a{2}",str)
result=re.findall("taam{1}",str)
result=re.findall("[0-9]{2}",str)

"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.

        a|b => a ya da b

            cde =>    no match
            ade =>    1 match
            acdbea => 3 match 
"""

"""
    () - gruplamak için kullanılır.

         (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.
"""

result = re.findall("\APython", str)
result = re.findall("saat\Z", str)

"""
    \ - Özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterinin arar. Yani
               $ regular exp. engine tarafından yorumlanmaz.

    \A - Belirtilen karakter string in başında mı ?
         \Athe => the string in başındamı



    \Z - Belirtilen karakter string in sonunda mı ?
         the\Z => the string in sonunda mı

    \b - Belirtilen karakter kelimenin in başında ya da sonunda mı ?
         \bthe => the kelimenin in başında mı?
         the\b => the kelimenin in sonunda mı?

    \B - Belirtilen karakter kelimenin in başında ya da sonunda değil mı ?
         \Bthe => the kelimenin in başında değil mi?
         the\B => the kelimenin in sonunda değil mi?
    
    \d - [0-9] ile aynı anlama gelir yani rakamları arar.
         \d => 12abc34

    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
         \D => 1ab44_50

    \s - Boşluk karakterlerini arar.  
    \S - Boşluk karakterleri dışındakiler.
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
    \W - \w nin tam tersi
    
"""

print(result)