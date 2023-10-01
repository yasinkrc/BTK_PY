import requests 
from bs4 import BeautifulSoup 

url='https://www.n11.com/bilgisayar/dizustu-bilgisayar'

html=requests.get(url).content
soup=BeautifulSoup(html,'html.parser')
# print(html)

# list=soup.find_all('li',{'class':'column'},limit=1) #limit=1 sadece bir li getir 
# print(list)
list=soup.find_all('li',{'class':'column'})

for li in list:
    name=li.div.a.h3.text.strip()
    link=li.div.a.get("href")
    oldprice=li.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip("TL")
    newprice=li.find("div",{"class":"proDetail"}).find_all("a")[1].text.strip("TL")
    
    # print(name )
    # print(link)
    # print(oldprice,new)
    print(f"name:{name} link : {link}  old price : {oldprice} newprice : {newprice}")