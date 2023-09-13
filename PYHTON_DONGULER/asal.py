"""

Girilen bir sayının asal olup olmadığını bulun  
"""


sayı=int(input("Lütfen bir sayı girin"))
asal_mi=True
if sayı==1 :
        asal_mi=False
        
for i in range(2,sayı):
    if sayı%i==0 :
        asal_mi=False
        break

if asal_mi:
    print(" sayı asaldır ")
else :
    print("Sayi asal değildir")
        
            
    
    