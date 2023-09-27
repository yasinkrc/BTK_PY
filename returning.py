def usalma(number):
    # two=usalma(2)
    # three=usalma(3)
    
    def inner(power):
        return number **power
    
    return inner


two=usalma(2)
three=usalma(3)
print(two(3))
print(three(3))


def yetki_Sorgula(page):
    def inner(role):
        if role=='Admin':
            return "{0} rölü {1} sayfasına ulaşabillir".format(role,page)
        else :
            return  "{0} rölü {1} sayfasına ulaşamaz".format(role,page)
    return inner

user1=yetki_Sorgula("Product Edit")
print(user1("Admin"))
print(user1("USER"))


def islem(islem_ad):
    def toplam(*args):
        toplam=0
        for i in args :
            toplam+=i
        return toplam 
    def carpma(*args):
        carpim =1
        
        for i in args :
            carpim*=i
        return carpim 
    if islem_ad=="toplama":
        return toplam 
    else :
        return carpma 


toplama=islem("toplama")
print(toplama(1,2,3,4,5))    

carpma=islem("carpma")
print(carpma(1,2,3,4,5))