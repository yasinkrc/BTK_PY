""" 
numbers = [1,2,3,4,5,6,7,8,9,10]  yapardik for ile eğer olmasaydı buna benzer sıralama bir şey yapamazık 
"""
x=0

while x <100:
    
    if x%2==1:
        print("Tek  : ",x)
    else :
        print("Çift : ",x)
    x=x+1

print("bitiiiii ")


name = " " #false 

while not name.strip():
    name=input("isminizi giriniz: ")

print(f"Merhaba ,{name}")