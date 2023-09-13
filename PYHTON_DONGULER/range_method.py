""" range """
# lista= [1,2,3]

# for i in lista :
    
#     print(i)
    
# for i in range(50,100,20):
#     print(i)

# print(list(range(5,100,10)))

# index=0

# greeting = " Hello There"

# for letter in greeting :
#     print(f"index: {index} letter {letter}")
#     index+=1

""" enumarete """ 

# greeting = "Hello"

# for index , letter in enumerate(greeting):
#     print(f"index : {index} letter : {letter}")
# for item in enumerate(greeting):
#     print(item)


list1=[1,2,3,4,5,6,7,8,9]
list2=['a','b','c','d','e']
list3=["yasin","yazgülü","beşaltı","karaca"]


print(list(zip(list1,list2,list3)))

for item in zip(list1,list2,list3) :
    print(item)

for a , b ,c in zip(list1,list2,list3):
    print(a)
    print(b)
    print(c)