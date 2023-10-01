#Tarih  ve zaman varsa datetime modülünü kullanırız 

from datetime import datetime 
from datetime import timedelta
# from datetime import date
# from datetime import time 
#import datetime



#Eğer yanlızca tarih ile ilgili işlem : Date modülü
#Eğer yanlızca zaman  ile ilgili işlem : time modülü
#Eğer  tarih ile zaman ilgili işlem : datetime modülü 

# result=dir(datetime.time)
# result=dir(datetime.date)
simdi=datetime.now()
simdi=datetime.today()
result=simdi.year
result=simdi.month
result=simdi.day
result=simdi.hour
result=simdi.minute
result=simdi.second

result=datetime.ctime(simdi)
print(result)
result=datetime.strftime(simdi,'%Y')  #Y: YEAR
result=datetime.strftime(simdi,'%X')  #X: HOUR
result=datetime.strftime(simdi,'%d')  #D: DAY
result=datetime.strftime(simdi,'%A')  #A: DAY NAME  Thursday
result=datetime.strftime(simdi,'%B')  #B: MONTH September 
result=datetime.strftime(simdi,'%Y %B %A')  

# t='21 Nisan 2019'
# gun,ay,yil=t.split()
# print(gun)
# print(ay)
# print(yil)
# print(result)

t='15 April 2019 hour 10:12:30'
dt=datetime.strptime(t,'%d %B %Y hour %H:%M:%S')
print(dt)
result=dt.year
print(result)

birthday=datetime(1983,5,9,12,45,32)
print(birthday)

result=datetime.timestamp(birthday) #saniye yapar
result=datetime.fromtimestamp(result) # saniye to datetime 
result=datetime.fromtimestamp(0) #Bilgisayarlar için kullanılan milat sayı :1970-01-01 03:00:00


result=simdi-birthday #timedelta iki tane fark yaparsan bu sefer değişik bir tane nesne gelir 
result=result.days
# result=result.seconds => bende okumuyor :( 
# result=result.microseconds  => bende buda okumuyor :( 

#ileri bir tarih bulmak için ise  timedelta'yı import etmemiz gerek :) 

print(simdi)

result=simdi+timedelta(days=10)
result=simdi+timedelta(days=730) #yıl geldi mesela  ama + geldi 
result=simdi-timedelta(days=730) #yıl geldi mesela  ama - oldu

print(result)

def factorial_d(num):
    
    if num <0 :
        raise Exception ("Sayı 0 ya da 0'dan büyük olmalıdır.")
    
    def factotorial_i(num):
        
        if num ==0:
            return 1
        
        return num * factotorial_i(num-1)        
    return factorial_i(num)

sayi=factorial_d(5)

print(sayi)    