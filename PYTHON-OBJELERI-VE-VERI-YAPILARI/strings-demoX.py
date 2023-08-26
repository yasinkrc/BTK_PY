website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehperiniz (40 saat)"

#1- 'Hello World ' karekter dizisinin baş ve sondaki boşluk karekterlerini silin.
x=" Hello World " 
# result=x.strip()
# result=x.lstrip() 
# result=website.lstrip('htp:/')

#2- "www.sadikturan.com" içindeki sadıkturan bilgisi haricindeki her karekteri silin

result="www.sadikturan.com".strip("e.comw")
#3- 'course" karekter dizisinin tüm karekterlerini küçük harf yapın 
result=course.lower()
#4- 'website' içinde kaç tane a karekteri vardir ? (count("a"))
result=website.count("a")
#5-  "website"  www ile başlayıp com ile bitiyor mu ?


# x = website.startswith("www")
# y = website.endswith("com")

# if x:
#     if y:
#         print("Website 'www' ile başlıyor ve 'com' ile bitiyor.")
#     else:
#         print("Website 'www' ile başlıyor ancak 'com' ile bitmiyor.")
# else:
#     if y:
#         print("Website 'www' ile başlamıyor ancak 'com' ile bitiyor.")
#     else:
#         print("Website ne 'www' ile başlıyor ne de 'com' ile bitiyor.")

    

#6-  "website"  içinde ".com" ifadesi var mı ?
result=website.find(".com")
#7-  "course" içindeki karekterlerin hepsi alfabetik mi (isalpha , weisdigit)
result=course.isalpha()
result=course.isdigit()

#8-   "Contents" ifadesini satırda 50 karekter içine yerleştirip sağ ve soluna * ekleyiniz .

result="Contents".center(50,"*")

#9- "course"  karekter dizisindeki tüm boşluk karekterlerini "-" ile değiştirin

result=course.replace(" ", "*")

#10- "Hello World" karekter dizisinin "World" ifadesini "There" olarak değiştirin

result="Hello World".split(" ")

result[1]="There"


#11- "course"  karekkter dizisini boşluk karekterlerinden ayırın .

result=course.split(" ")




print(result)