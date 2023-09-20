""" YÖNTEM1 """
# import math
# import math as islem 

# value=dir(math)
# value=help(math)
# value=help(math.factorial)
# print(math.factorial(5))
# value=math.sqrt(49)
# value=math.factorial(8)
# value=math.floor(5.9)
# value=math.ceil(5.9)
# value=islem.factorial(5)

""" YÖNTEM2 """

def sqrt(x):
    print("x : "+str(x))

# from math import *  => ya da daha da güzel bir yöntemi var 
from math import factorial ,sqrt , ceil 

def sqrt(x):
    # print("x : "+str(x))
    return x

# value=factorial(5)
value=sqrt(9)
# value=ceil(9.8)
print(value)
