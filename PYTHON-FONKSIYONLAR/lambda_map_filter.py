def square(num): return num ** 2

numbers=[1,3,4,6,8,10,16,18,96,5,9]
map(square,numbers)
result=map(square,numbers)


# result=square(2)
print(list(result))

""" ya da ikinci  yol var """ 

for item in map(square,numbers):
    print(item)

""" lambda exspression""" 
sayilar=[1,23,4,6,4,6,5,9,4,33,5,1,5,2]
print("Artamadan önce : ",(map(lambda num : num**2,sayilar)))
result=list(map(lambda num : num**2,sayilar))
print(result)

"""Hata daha değişik bir şey var  """

kareler=[1,2,3,4,6,4,6,46,54,6,9,64,9,46,4,64]
my_func=lambda num :num**2
result=list(map(my_func,kareler))
print(result)

""" Hatta sadece fonksiyon şeklinde bile kullanabillirsin"""
 
new_func=lambda num :num**2
adetler=[1,3,5,9]
result=new_func(3)
print(result) 


""" filtre""" 

def check_even(num): return num%2==0

result=list(filter(check_even,numbers))
result=list(filter(lambda num : num%2==0,numbers))
result=list(filter(check_even,numbers))
check_even=lambda num : num%2==0
result=check_even(numbers[2])
print(result)


