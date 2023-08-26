#Key - value
#41 => kocaeli 34=> istanbul 

# sehirler=["kocaeli","istanbul"]

# plakalar=[41,34]

# print(plakalar[sehirler.index("istanbul")])
# print(plakalar[sehirler.index("kocaeli")])


# plakalar ={'kocaeli':41 ,'istanbul':34}

# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])


# plakalar['ankara']=6
#plakalar['kocaeli']='new value'

# print(plakalar)


users={
    'sadikturan':{
    'age':36,
    'roles':['user'],
    'e-mail':'sadik@gmail.com',
    'address':'kocaeli',
    'phone':'123456789'
    #Buraya bakman gerekli yiğidim hiç olmazsa notlar almaya çalışş 

    },
    'cinarturan':{
    'age':36,
    'roles':['admin', 'user'],
    'e-mail':'cinar@gmail.com',
    'address':'istanbul',
    'phone':'44521548'
    }
}


print(users['cinarturan'])
print(users['cinarturan']['e-mail'])