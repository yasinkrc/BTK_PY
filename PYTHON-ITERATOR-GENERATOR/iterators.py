# # liste=[1,2,3,4,5]

# # for i in liste:
# #     print(i)
    
# # print(dir(liste))
# liste=[1,2,3,4,5]

# iterator=iter(liste)


# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# # print(next(iterator))

# for i in liste:
#     print(i)

# iterator=iter(liste)
# print("Sonra ")

# while True :
    
#     try :
#         element=next(iterator)
#         print(element)
#     except StopIteration :
#         break

""" Peki bunlara neden ihtiyacaımız var zaten bizler for kullanmıyormuyuz 
nedeni : bazen kendimiz bir tane iterator oluşturmak isteyebiliriz """

class MyNumbers:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start<=self.stop:
            x=self.start
            self.start+=1
            return x 
        else :
            raise StopIteration 
list=MyNumbers(10,20)

myiter=iter(list)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

while True:
    try :
        element=next(myiter)
        print(element)
    
    except StopIteration :
        break 
# for x in list:
#     print(x)