class Person:
    address = "no information"
    
    def __init__(self, name, year):
        self.name = name
        self.birthday = year
        print("init methodu çalıştı")
    
    def intro(self):
        print("Merhaba. Ben " + self.name)
        
    def calculateAge(self):
        return 2023 - self.birthday

p1 = Person("Yasin", 1978)
p2 = Person("Leyla", 1971)

p1.intro()
p2.intro()

print(f"Adım {p1.name}, Yaşım {p1.calculateAge()}")
print(f"Adım {p2.name}, Yaşım {p2.calculateAge()}")

# p1.address = "yes information"
# print(p1.address)
# print(Person.address)

# p1.name = "Ahmet"
# print(f'Adı: {p1.name}, Doğum Yılı: {p1.birthday}')
# print(f'Adı: {p2.name}, Doğum Yılı: {p2.birthday}')

class Circle :
    #class object attribute
    pi=3.14 
    
    def __init__(self,yaricap=1):
        self.yaricap=yaricap
    #Methods
    
    def cevre_hesapla(self):
        return 2*self.pi * self.yaricap
    
    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)
    

c1=Circle() #yarıçap==1
c2=Circle(5)

print(f" c1 : alan {c1.alan_hesapla()} çevre : {c1.cevre_hesapla()}")
print(f" c2 : alan {c2.alan_hesapla()} çevre : {c2.cevre_hesapla()}")