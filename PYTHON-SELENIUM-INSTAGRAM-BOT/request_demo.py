import requests 
from bs4 import BeautifulSoup

r=requests.get("https://en.yellowpages.com.tr/restaurants-c")
result=r.content
soup=BeautifulSoup(result,"html.parser")
print(soup.prettify())

linkler=soup.find_all("a")

for i in linkler :
    print(i)