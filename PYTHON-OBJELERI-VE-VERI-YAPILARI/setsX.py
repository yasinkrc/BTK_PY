""" PYTHON'DA SETS """

fruits = {'orange','apple','banana'}

#indekslenemez baba: /

for x in fruits:
    print(x)


fruits.add("cherry") 
fruits.update(['mango','grape',"apple"])

#her elemandan yalnızca bir adet var 

myList = [1,2,3,4,5,6,7,8,9,10,10,10,6,6,6]

print(set(myList))

print(fruits)