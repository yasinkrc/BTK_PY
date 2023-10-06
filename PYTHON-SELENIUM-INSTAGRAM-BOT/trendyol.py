from bs4 import BeautifulSoup 
import requests 
while True : 
    url='https://www.trendyol.com/fups/kart-p-147893922'
    #link değişse bile kodlar değişmez 

    sayfa=requests.get(url)

    html_sayfa=BeautifulSoup(sayfa.content,"html.parser")

    isim=html_sayfa.find('h1' ,{"class":"pr-new-br"}).text
    print(isim)

    fiyat=html_sayfa.find('span' ,{"class":"prc-dsc"}).text
    print(fiyat)

    #Telegram 

    api="https://api.telegram.org/bot6484388696:AAEDfb_Inod9W-EtYEYfqDJ1vi7clzoczyk/SendMessage"

    mesaj=isim+"\n"+fiyat
    requests.post(url=api,data={"chat_id":"5619771051","text":mesaj}).json()

    print(mesaj)