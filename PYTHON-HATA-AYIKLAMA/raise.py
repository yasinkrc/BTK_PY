# x=10 
# if x>5 :
#     raise Exception("X 5'den büyük değer alamaz")


# def check_password(psw):
#     import re 
#     if len (psw)<8:
#         raise Exception ("Parola en az 7 karekter olmalıdır")  
#     elif not re.search("[a-z]",psw):
#         raise Exception("Parola küçük harf içermelidir.")
#     elif not re.search("[a-z]",psw):
#         raise Exception("Parola küçük harf içermelidir.")
#     elif not re.search("[A-Z]",psw):
#         raise Exception("Parola Büyük harf içermelidir.")
#     elif not re.search("[0-9]",psw):
#         raise Exception("Parola rakam harf içermelidir.")
#     elif not re.search("[_@$]",psw):
#         raise Exception("Parola  alpa numeric karekter  içermelidir.")
#     elif not re.search("\s",psw):
#         raise Exception("Parola boşluk  içermemelidir .")
#     else :
#         print("geçerli parola")
    

# parola=input("Parola:")

# try :
#     check_password(parola)
# except Exception as ex :
#     print(ex)
# else :
#     print("geçerli parola  : else ")
# finally :
#     print("validation tamamlandı.")


class Person :
    
    def __init__(self,name,year):
        if len(name)>10 :
            raise Exception("Name alanı fazla karekter içeriyor")
        else :
            self.name=name

p=Person("yas",200) 
        