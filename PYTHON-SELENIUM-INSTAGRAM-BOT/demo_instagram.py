from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from personal import password,username,ayse
import time

class Instagram():
    
    def __init__(self,username,password,ayse):
        self.username=username
        self.password=password
        self.ayse=ayse
        self.driver=webdriver.Chrome()
    
    def kullaniciGiris(self): #buradan webbrowser de eğer kayıtlı bir  tane hesabın varsa Chromde misafir kullanıcı ile gir 
        
        self.driver.get("https://instagram.com/accounts/login/")
        time.sleep(2)
        
        username=self.driver.find_element(By.NAME,"username")
        password=self.driver.find_element(By.NAME,"password")
        time.sleep(1)
        username.send_keys(self.username)
        time.sleep(1)
        password.send_keys(self.password)  
        time.sleep(1)      
        button=self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
        #yukarıda kullandın By.XPATH ama bir nokta var XPATH çok değişiyor ve bunun senin için iyi sorunlar doğurmuyor 
        #Bu yüzdeb css selector kullanabilirsiin 
        #self.driver.find_element(BY.CSS_SELECTOR,"button[type=submit]")
        
        time.sleep(1)
        button.click()
        time.sleep(4)
       
        tik=self.driver.find_element(By.CLASS_NAME,'_ac8f')
        tik.click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,"._a9-z").find_element(By.CSS_SELECTOR,"._a9--._a9_1").click()
        time.sleep(3)
        
    def  takipci_Al(self):
        self.driver.get("https://www.instagram.com/osatdrive/?next=%2F")
        time.sleep(3)
        a=self.driver.find_element(By.CSS_SELECTOR,'.x78zum5.x1q0g3np.xieb3on')
        time.sleep(2)
        a.find_element(By.TAG_NAME,'a').click() 
        time.sleep(2)
        users=self.driver.find_element(By.CSS_SELECTOR,"div[role=dialog]").find_elements(By.CSS_SELECTOR,'.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3')
        for user in users :
            followerName=user.find_element(By.CSS_SELECTOR,"._aacl._aaco._aacw._aacx._aad7._aade").text
            print(followerName)
            
    def tumTakipcileriAl(self):
        self.driver.get("https://www.instagram.com/osatdrive/?next=%2F")
        time.sleep(3)
        a=self.driver.find_element(By.CSS_SELECTOR,'.x78zum5.x1q0g3np.xieb3on')
        time.sleep(2)
        a.find_element(By.TAG_NAME,'a').click() 
        time.sleep(2)
        fallowerList=self.driver.find_element(By.CSS_SELECTOR,"div[role=dialog]")
        usersCount=len(fallowerList.find_elements(By.CSS_SELECTOR,'.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3'))
        print(f'ilk takipçi adedi :{usersCount}')
        
        while True:
            fallowerList.click()
            
            scroll_count=4
            
            for i in range(scroll_count):
                #sayfada aşağıya doğru kaydırmak içibb PAGE_DOWN tuşuna basıyoruz 
                self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
                time.sleep(1)
                
            newCount=len(fallowerList.find_elements(By.CSS_SELECTOR,'.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3'))
            if usersCount!=newCount:
                usersCount=newCount
                print(f"toplam takipçi : {newCount}")
            else :
                break
        users=self.driver.find_element(By.CSS_SELECTOR,"div[role=dialog]").find_elements(By.CSS_SELECTOR,'.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3')
        for user in users :
            followerName=user.find_element(By.CSS_SELECTOR,"._aacl._aaco._aacw._aacx._aad7._aade").text
            print(followerName)       
        
    def takipEt(self,followerName):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{followerName}")
        time.sleep(4)
        
      
        text=self.driver.find_element(By.CSS_SELECTOR,'._acan._acap._acat._aj1-').text 
        time.sleep(2)
        if text !='Following':
            takip=self.driver.find_element(By.CSS_SELECTOR,'//*[@id="mount_0_0_rP"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/div/div[1]/button')
            time.sleep(2)
            takip.click()
        else :
            print("Zaten Takiptesin ....")
            
     
        
    def takipciBirak(self,followerName):
        self.driver.get(f"https://www.instagram.com/{followerName}")
        time.sleep(2)
        
        text=self.driver.find_element(By.CSS_SELECTOR,'._acan._acap._acat._aj1-').text
        if text=="Following":
            
            self.driver.find_element(By.CSS_SELECTOR,'._acan._acap._acat._aj1-').click()
            time.sleep(2)
            button=self.driver.find_element(By.CSS_SELECTOR,'.x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1'.replace(' ','.'))
            time.sleep(2)
            button.click()
            time.sleep(5)
        else :
            print("Zaten takip etmiyorsunuz....")
        
        while True :
            continue

    def takipciKaydet(self):
        self.driver.get("https://www.instagram.com/osatdrive/?next=%2F")
        time.sleep(3)
        a=self.driver.find_element(By.CSS_SELECTOR,'.x78zum5.x1q0g3np.xieb3on')
        time.sleep(2)
        a.find_element(By.TAG_NAME,'a').click() 
        time.sleep(2)
        fallowerList=self.driver.find_element(By.CSS_SELECTOR,"div[role=dialog]")
        usersCount=len(fallowerList.find_elements(By.CSS_SELECTOR,'.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3'))
        print(f'ilk takipçi adedi :{usersCount}')
        
        while True:
            fallowerList.click()
            
            scroll_count=4
            
            for i in range(scroll_count):
                #sayfada aşağıya doğru kaydırmak içibb PAGE_DOWN tuşuna basıyoruz 
                self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
                time.sleep(1)
                
            newCount=len(fallowerList.find_elements(By.CSS_SELECTOR,'.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3'))
            if usersCount!=newCount:
                usersCount=newCount
                print(f"toplam takipçi : {newCount}")
            else :
                break
        users=self.driver.find_element(By.CSS_SELECTOR,"div[role=dialog]").find_elements(By.CSS_SELECTOR,'.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3')
        userList=[]
        for user in users :
            followerName=user.find_element(By.CSS_SELECTOR,"._aacl._aaco._aacw._aacx._aad7._aade").text
            userList.append(followerName)
            
        
        with open('kulanici_adlari.txt','w',encoding='utf-8') as file :
            
            for user in userList:
                file.write(user+"\n")
        

       
        
    
        
    
    
instagram =Instagram(username,password,ayse)
instagram.kullaniciGiris()
# instagram.takipci_Al()
# instagram.tumTakipcileriAl()
# instagram.takipEt("upcornco")
# instagram.takipciBirak('upcornco')
instagram.takipciKaydet()
