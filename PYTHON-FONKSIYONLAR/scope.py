#globalscope 
x="global x "

def function():
    #local scope 
    x='local x '
    print(x)

function()
print(x)


name ='Çınar'

def changeName(new_name):
    global name
    name=new_name
    print(name)
    
changeName("Ada")
print(name)

print("********************************************")

name = "global string"

def greeting():
    name="Çınar"
    
    def hello():
        name='ada'
        print("hello "+name) #ona en yakın olan hangisi ise onu çağırır 
    hello()


greeting()

print("**********************")

x=50

# def test():
#     global x 
#     print(f"x : {x}")
    
#     x=100
#     print(f"changed x to {x}")

# test()
# print(x)

