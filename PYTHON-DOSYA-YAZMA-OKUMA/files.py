#Dosyadd açmak ve oluşturmak için open() fonksiyonu kulllanılır 
#Kullanımı : open(dosya_adi ,  dosya_erişme_modu)
#dosya_erişme_modu=> dosyayı hangi amaçla açtığımızı belirtir 


# "w": (Write) yazma modu . Dosyayı konumda oluşturur 
""" 
** Dosyayı konumda oluşturur 
** Dosya içeriğini siler ve yeniden ekleme yapar 
"""

# file=open("newfile.txt","w",)   #  => burada "r" kullanamayız mesela çunkü öyle bir dosya yok önnce bunun oluşması lazımdı 
# print(result)
# file.close()
# file=open("C:/Users/ismai/OneDrive/Masaüstü/newfile.txt","w")
# print(file)
# file=open("newfile.txt","w",encoding="utf-8")
# file.write("Sadık Turan ")
# file.close()
# "a": (Append) ekleme . Dosya konumda yoksa oluşturur 

# file=open("newfile.txt","a",encoding="utf-8")
# file.write("Sadık Turan \n")
# file.close()

# "x": (Create) oluşturma. Dosya zaten varsa hata verir

file=open("newfile2.txt","x",encoding="utf-8")
file.write("Sadık Turan /n") #ikinci defasında hata veriri sana 
file.close()
# "r": (Read) okuma. varsayılan dosya konumda yoksa hata verir



