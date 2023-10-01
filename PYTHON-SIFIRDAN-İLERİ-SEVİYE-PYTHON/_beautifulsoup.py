from bs4 import BeautifulSoup 

html_doc="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ilk web sayfam </title>
</head>
<body>
    <h1 id="header">
     Python Kursu 
    </h1>
    <div class="grup1">
        <h2>
            Programlama
        </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>

    </div>
    <div class="grup2">
        <h2>
            Modüller
        </h2>
        <ul>
            <li>Modül 1</li>
            <li>Modül 2</li>
            <li>Modül 3</li>
        </ul>

    </div>
    <div class="grup3">
        <h2>
            Django
        </h2>
        <ul>
            <li>Django 1</li>
            <li>Django 2</li>
            <li>Django 3</li>
        </ul>

    </div>

    <img src="resim.png" alt="">

    <a class="sister1" href="http://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister2" href="http://example2.com/elsie" id="link2">Elsie</a>
    <a class="sister3" href="http://example3.com/elsie" id="link3">Elsie</a>

</body>
</html>
"""

soup=BeautifulSoup(html_doc,'html.parser')
# print(soup)
result=soup.prettify() #consollerdeki hepsini düzenli yapar prettfy 
result=soup.title
result=soup.head
result=soup.body
""" Yukarıdakileri özele indirgemek içim """
result=soup.title.name #alanı söyler 
result=soup.title.string #stringi söyler 

result=soup.h1
result=soup.h2
result=soup.h2.name
result=soup.h2.string
result=soup.h1.string


result=soup.find_all('h2') #yukarıda sadece h2 vardı bir tane tek getirdi ama h1 bir tane tek var ama h2  daha da fazla olabilir h2 
#find_all() methodu ise tüm h2'leri sana bir  dizi şeklinde verir 
result=soup.find_all('h2')[0]
result=soup.find_all('h2')[1]

result=soup.div #sadece ilk divi verir 
result=soup.find_all('div')[0]
result=soup.find_all('div')[1].ul
result=soup.find_all('div')[1].ul.find_all('li')
# for i in result:
#     print(i)
result=soup.div.findChildren() #div altındaki hepsi gelir 
result=soup.div.findNextSibling() #Modüller
result=soup.div.findNextSibling().findNextSibling() #Django
result=soup.find_all('a')

for i in result :
    print(i.get('id'))




print(result)