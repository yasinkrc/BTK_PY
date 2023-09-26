#Error handling => hata yönetimi 

# try :
    
#   x=int(input("X: "))
#   y=int(input("Y: "))
#   print(x/y)
# except (ZeroDivisionError , ValueError) as e :
#     print("Yanlış bilgi girdiniz :/ ")
#     print(e)
# except  :
#     print("X ve Y için sayısal değer girmelisiniz . ")
""" Böyle olursa ne yaziki bu sefer hata objesine erişemeyiz """
# except :
#     print("Yanlış bilgi girdiniz. ")

# while  True:

#     try :
        
#         x=int(input("X: "))
#         y=int(input("Y: "))
#         print(x/y)

#     except :
#         print("Yanlış bilgi girdiniz. ")
#     else :
#         print("Her şey yolunda ")


while  True:

    try :
        
        x=int(input("X: "))
        y=int(input("Y: "))
        print(x/y)

    except Exception  as ex :
        print("Yanlış bilgi girdiniz. ",ex)
    else : #except çalışmazsa else çalışır 
        break
    finally:#yanlış da doğru da gelse bu çalşır  
        print("Try except sonlandı")
    
    