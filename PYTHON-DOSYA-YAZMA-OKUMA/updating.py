# with open("newfile.txt","r+",encoding="utf-8") as file :
#     file.seek(20)
#     file.write("Deneme")
# with open("newfile.txt","r+",encoding="utf-8") as file :
#     print(file.read())

# ***** Sayfa sonunda güncelleme *****

# with open("newfile.txt","a",encoding="utf-8") as file :
#     file.write("\nEmel Turan")   #dikkkat tek bir adet parametre alır 
#     #file.write("\nEmel Turan",end="") burada hata var end olmaz dikkat  et .

# ***** Sayfa başında  güncelleme *****

 
# with open("newfile.txt","r+",encoding="utf-8") as file:
#    content=file.read()
#    content="Efe Turan\n"+content
#    file.seek(0)
#    file.write(content)
# #    print(content)
# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read()) 
    
# ***** Sayfa ortasında   güncelleme *****

with open("newfile.txt","r+",encoding="utf-8") as file :
    list=file.readlines()
    # print(list) ['Efe Turan\n', 'Sadık Turan\n', 'Çınar Turan \n', 'Ada Bilgi \n', 'Yiğit Bilgi \n', 'Emel Turan']
    list.insert(1,"Yılmaz Güney\n")
    # print(list)
    file.seek(0)
    # for i in list:  #bunun yerine kullanabileceğin bir tane daha var 
    #     file.write(i)
    file.writelines(list)

with open("newfile.txt","r",encoding="utf-8") as file :
    print(file.read())

