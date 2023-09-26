# file=open("newfile.txt","r",encoding="utf-8")

# content=file.read()

# print(content)
# file.close()  
""" Bu kodda bazı şeyler doğru ama her zaman  
file.close() yazman gerek Bu derten kurtulaman içn 
sama güzel bir yöntem gösterecem aşağıda 
"""

with open("newfile.txt","r",encoding="utf-8") as file:
    content=file.read(10)
    print(content)
    file.seek(0) #dosyayı tekrar çağırmadan bizim nerede olmak istedğimize yarıdmcı olur
    print(file.tell()) #bize nerede kaldığımızı söyler 
    content2=file.read(10) #okumaz çünkü yukarısında bir tane read var 
    print(content2)