#Inheritance (Kalıtım) : Miras alma 


#Person => name  , lastname  , age , eat() , run() , drink() 

#Stundent(Person), Teacher(Person)

#Animal => Dog(Animal) , Cat(Animal) 

class Person():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        print("Person Created")
    def who_am_i(self):
        print("I am a person")
    
    def eat(self):
        print("I am eating")
        
        

class Stundent(Person):
    def __init__(self,fname ,lname,number):
        Person.__init__(self,fname,lname)
        self.studentNumber=number
        print("Stunent Created") 
       #override
    def who_am_i(self):
        print("I am a stundent")
    
    def sayHello(self):
        print("Hello I am a stundent")


class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        self.branch=branch
        
    def who_am_i(self):
        print(f"I am a {self.branch}")
        
    
p1=Person("Yasin","Karaca")
s1=Stundent("Çınar","Turan",1256)
t1=Teacher("Serkan","Beşaltı","Mühendis")

print(p1.fname+' '+p1.lname)
print(s1.fname+' '+s1.lname+f" numaramda : {s1.studentNumber}")

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()

p1.eat()
s1.eat()

s1.sayHello() #bunu sadece class Stundent ereşebillir 


