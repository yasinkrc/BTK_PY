from selenium import webdriver 
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep 
from selenium.webdriver.common.keys import Keys
from personal import kullanici_Adi , sifre ,ayse
 
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
sleep(3)
input=driver.find_element(By.NAME,"q")
sleep(2)
input.send_keys("instagram")
sleep(3)
searchButton=driver.find_element(By.NAME,"btnK")
sleep(4)
# print(searchButton)
searchButton.click()
sleep(2)
#xpath
#//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3
#fullXpath
#/html/body/div[6]/div/div[9]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3
tick=driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3').click()
sleep(3)
username=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(kullanici_Adi)
password=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(sifre)
sleep(5)

button_tik=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
sleep(10)

bul=driver.find_element(By.XPATH,'//*[@id="mount_0_0_fA"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div[1]/nav/div/header/div/div/div[1]/div/div/div/div/div/input').send_keys(ayse)
Keys.ENTER()

sleep(2)


tıkla=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/div/div/button/div/div').click()


# print(f"Input : {input}")
#sleep(10)
while True:
    continue 
#input