from bs4 import BeautifulSoup 
import requests
url="https://www.glassdoor.com/Reviews/index.htm?overall_rating_low=3.5&page=1&locId=3827614&locType=C  "
header={
    
    "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"

}
get=requests.get(url,headers=header)
#404 code is wrong 
content=get.content

soup=BeautifulSoup(content,"html.parser")
titles=soup.find_all("span",{"class":"align-items-center mb-xsm"})

for i in titles :
    i=i.text
    print(i)
# print(get.status_code)