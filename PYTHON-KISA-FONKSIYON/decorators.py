# #bir özelliği birden fazla yerde kullanmak istiyorsak decorators kullanmamız gerek
# #Amaç daha az kod yazmak


# def my_decorator(func):
#     def wrapper(name):
#         print("Fonksiyondan önce işlemler")
#         func(name)
#         print("Fonksiyondan sonraki işlemler")
        
#     return wrapper
# """************************"""
# # @my_decorator
# # def sayHello():
# #     print("hello")
# # sayHello()
    
# """************************"""
# @my_decorator
# def sayHello(name):
#     print("hello ",name)

# sayHello("Ali")
# # def sayHello():
# #     print("Hello")
# # def sayGreeting():
# #     print("greeting")
    

# # sayHello=my_decorator(sayHello)
# # sayGreeting=my_decorator(sayGreeting)
# # # sayHello()
# # sayGreeting()

import math
import time 

def calculate_time(func):
    def inner(*args, **kwargs):
        start=time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish=time.time()
        print("Fonksiyon : "+func.__name__ +" "+str(finish-start)+" saniye sürdü")
    return inner

        
@calculate_time
def usalma(a,b):
    # start=time.time()
    # time.sleep(1)
    print(math.pow(a,b))
    # finish=time.time()
    # print("Fonksiyon : "+str(finish-start)+" saniye sürdü")
@calculate_time
def faktoriyel(num):
    # start=time.time()
    # time.sleep(1)
    print(math.factorial(num))
    # finish=time.time()
    # print("Fonksiyon : "+str(finish-start)+" saniye sürdü")


usalma(2,3)
faktoriyel(4)