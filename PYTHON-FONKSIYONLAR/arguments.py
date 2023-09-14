def changeName(n):
    n='ada'
    print("fonksiyonun içinde : ",n)

name='Yiğit'
print("Fonksiyondan önce : ",name)
changeName(name)
print("Fonksiyondan sonra : ",name)


def change(n):
    n[0]='istanbul'
    print("fonksiyonun içinde : ",n)

sehirler=['Ankara','İzmir']
print("Fonksiyondan önce : ",sehirler)
change(sehirler)
print("Fonksiyondan sonra : ",sehirler)

n=sehirler
n[0]='diyarbakır'
print(sehirler)
print("****************************************************")
""" eğer kopyalama yapmak istersen tüm elemanları karşıya kopyalaman lazım """ 
print(sehirler)
print(n)
print("****************************************************")
n=sehirler[::]
n[::]=["urfa","antep"]
print("****************************************************")
print(sehirler)
print(n)

def add(a,b,c=0 ,d=0,e=0):
    return sum((a,b,c,d,e))

print(add(10,20))
print(add(10,20,30))

def addX(*params):
    print(params)
    print(params[0])
    print(params[6])
    return sum(params)

print(addX(1,2,3,4,6,6,6,4,2,5,4,5,4,6,646,6,4))

def addY(*params):
    sum=0
    for i in params:
        sum+=sum+i
    print(sum)

print(addY(1,2,3,4,6,6,6,4,2,5,4,5,4,6,646,6,4,4545))


def displayUser(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key} is {value}")
    
# İlk kullanıcıyı görüntüle
displayUser(name='Çınar', age=2, city='istanbul')

# İkinci kullanıcıyı görüntüle
displayUser(name='Ada', age=12, city='kocaeli', phone='123456')

# Üçüncü kullanıcıyı görüntüle
displayUser(name='Yiğit', age=12, city='ankara', phone='1234567', e_mail='yiğit@gmail.com')



def myfunc(a,b,*args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)  
myfunc(10,20,30,40,50,key1='value1',key2="value2")
 
