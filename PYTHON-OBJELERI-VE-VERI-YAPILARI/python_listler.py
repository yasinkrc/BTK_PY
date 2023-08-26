


# message="Hello There. My name is Sadik Turan"
# mylist=[1,2,3]
# mylist2=['bir',2,True]

# # print(message[0])

# # list=[mylist+mylist2]
# # print(list)

# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

araba =["BMW","MERCEDES","OPEL","MAZDA"]
# 2-  Liste Kaç elemanlıdır ?
result=len(araba)

# 3-  Listenin ilk ve son elemanı nedir ?
result=araba[0]
result=araba[-1]

# 4-  Mazda değerini Toyota ile değiştirin.

araba[-1]="TOYATA"
# print(araba)
# 5-  Mercedes listenin bir elemanı mıdır ?

result = "MERCEDES" in araba

# 6-  Listenin -2 indeksindeki değer nedir ?

result=araba[-2]

# 7-  Listenin ilk 3 elemanını alın.

result=araba[:3]

# 8-  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.

araba[-2:]="TOYATA","RENAULT"
result=araba

# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.

result=araba + ["AUDİ","NİSSAN"]
# 10- Listenin son elemanını silin.

del araba[-1]
# 11- Liste elemanlarını tersten yazdırınız.

result=araba[::-1]
# 12- Aşağıdaki verileri bir liste içinde saklayınız. 

      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90) 


studentA= [["Yiğit Bilgi"], [2010],[70,60,70]]
studentB =[["Sena Turan" ] ,[1999] ,[(80,80,70)]]
studentC= [["Ahmet Turan"] ,[1998] ,[(80,70,90)]]
# 13- Liste elemanlarını ekrana yazdırınız.

result=studentA+studentB+studentC
print(result)
