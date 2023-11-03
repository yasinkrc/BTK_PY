urunler=[]

adet = int(input("Merhaba kaç adet sayı istiyorsun ? "))

i=0

while (i<adet):
    name=input("Name: ")
    price=int(input("Price: "))
    urunler.append({

        "name":name,
        "price":price
    })
    i+=1

print(" ürünler ".center(50,"*"))
print(urunler)

for ürün in urunler :
    print(ürün["name"])


#unutma /n her zaman böyle yazılır


