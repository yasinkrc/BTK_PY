# while True: 
#         try : 
#             x=int(input("x: "))
#             y=int(input("y: "))
#             print("Sonuç",(x/y))
#         except Exception as ex :
#             print("Yanlış bilgi girdiniz :  ",ex)
#         else :
#              break
#         finally :
#              print("deneme 1 ")

""" Kendi nesnemizi oluşturma """ 

x=10 

if x>5 :
    raise Exception("x 5 den büyüktür")
else :
    print("TAMAMDIR")