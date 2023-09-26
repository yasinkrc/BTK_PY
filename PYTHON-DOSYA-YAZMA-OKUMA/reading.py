# try:
#     file = open("newfile2.txt", "r")  # Dosyayı okuma modunda aç
#     print(file)
# except FileNotFoundError:
#     print("Dosya okuma hatası : Dosya bulunamadı")
# finally:
#     if 'file' in locals():
#         print("Dosya kapandı")
#         file.close()  # Dosyayı her durumda kapat


# file=open("newfile.txt","r",encoding="utf-8")

#for döngüsü 

# for i in file:
#     print(i,end="")

# file.close()

#*****************************read() fonksiyonnu 

# content1=file.read()
# print("içerik 1 ")
# print(content1)
file=open("newfile.txt","r",encoding="utf-8")
# content2=file.read(5)
# content2=file.read(3)
# content2=file.read(3)

# # print("içerik 2 ")
# print(content2)
#*****************************readline () fonksiyonnu 

#readline fonkisyonu herseferinde birtane satır okur 

# content=file.readline()
# content1=file.readline()
# content2=file.readline()
# content3=file.readline()
# content4=file.readline()
# print(content)
# print(content1)
# print(content2)
# print(content3)
# print(content4)

# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")


#*****************************readlines () fonksiyonnu  

liste=file.readlines()

print(liste[0][2])

"harika bir not bunlar "

file.close()


