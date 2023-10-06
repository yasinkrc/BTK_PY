from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Test_Kodlamaio:
    
    def test_invalid_login(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        sleep(3)

        driver.get("https://www.kodlama.io/")
        sleep(5)
        loginBtn=driver.find_element(By.XPATH,'//*[@id="navbar"]/div/div/div/ul/li[3]/a')
        sleep(3)
        loginBtn.click() 
        #selenium kullanrak veri çektiğini anlammak için google bazı korumlar alıyor 
        sleep(30)
        
        
        
        while True:
            continue


testClass=Test_Kodlamaio()
testClass.test_invalid_login()
