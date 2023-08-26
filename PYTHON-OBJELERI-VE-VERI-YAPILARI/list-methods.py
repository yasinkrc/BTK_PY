# names=["Ali","Yağmur","Hakan","Deniz"]
# years=[1998,2000,1998,1987]

# # 1-  "Cenk" ismini listenin sonuna ekleyiniz.

# names.append("Cenk")

# # 2-  "Sena" değerini listenin başına ekleyiniz.

# names.insert(0, "Sena")

# # 3-  "Deniz" ismini listeden siliniz.

# # names.remove("Deniz")
# # 4-  "Deniz" isminin indeksi nedir ?

# # result=names.index("Deniz")
# # 

# # 5-  "Ali" listenin bir elemanı mıdır ?

# result="Ali" in names

# # 6-  Liste elemanlarını ters çevirin.

# # names.reverse()
# # print(names)

# # 7-  Liste elemanlarını alfabetik olarak sıralayınız.

# names.sort()


# # 8-  years listesini rakamsal büyüklüğe göre sıralayınız.
# years.sort()
# print(years[::-1])
# # 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
# strX = "Chevrolet,Dacia" 
# strX =strX.split(",")
# print(strX[0])
# # 10- years dizisinin en büyük ve en küçük elemanı nedir ?
# print(max(years))
# print(min(years))
# # 11- years dizisinde kaç tane 1998 değeri vardır ?

# print(years.count(1998))

# # 12- years dizisinin tüm elemanlarını siliniz.
# years.clear()
# print(years)

# # 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

# # marka1=input("Marka 1 :")
# # marka2=input("Marka 2 :")
# # marka3=input("Marka 3 :")

# # dizi=[]

# # dizi.append(marka1)
# # dizi.append(marka2)
# # dizi.append(marka3)

# # print(dizi)


# i=0 
# dizi=[]
# while i<3:
# ldfklşddkfşdkşfk
   
#     marka1=input("Marka 1 :")
#     dizi.append(marka1)
#     i+=1  



# print(dizi)

sayi=int(input("sayi : "))
carpma=1

while 0<sayi :

    carpma=carpma*sayi
    sayi-=1


print(carpma)