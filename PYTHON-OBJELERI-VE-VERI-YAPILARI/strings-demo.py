website ="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehperiniz (40 saat)"

#1- 'course ' karekter dizisinde kaç karekter bulunmakktadır .
result=len(course)
#2- 'website' içinden www karekterlerini alın .
result=website[0:7]+website[10:]
#3- 'website' içinden com karekterlerini alın .
result=website[0:-3]
#4- 'course'  içinden ilk 15 ve son 15 karekterlerini alın .
result=course[0:15]+course[-15:]

#5- 'course'  ifadesindeki karekterleri tersten yazdırın .

result=course[::-1]

# print(result)

name , surname , age , job = 'Bora' , 'Yilmaz' ,32 , "mühendis"

#6- Yukarıda verilen değişkenler ile ekrana aşağidaki ifadeyi yazdırınn 
# " Benim adım Bora Yilmaz ,Yaşimm 32 ve mesleğim mühendis."

# print(f"Benim adim {name} {surname} , Yaşim {age} ve mesleğim {job}")

# 'Hello World' ifadesindeki w harfini "W" harfi ile değiştirin .

# isim="Hello World"

# result=isim[0:5]+' w'+isim[7:]

""" abc ifadesini yan yana 3 defa yazdirin """
result="abc"*3
print(result)

