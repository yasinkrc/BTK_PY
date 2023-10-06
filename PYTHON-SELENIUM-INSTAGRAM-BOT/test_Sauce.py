from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Test_Sauce:
    
    def test_invalid_login(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        sleep(3)

        driver.get("https://www.saucedemo.com/v1/")
        sleep(5)
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        
        usernameInput.send_keys(1)
        passwordInput.send_keys(1)
        sleep(3)
        
        button=driver.find_element(By.ID,'login-button').click()
        #selenium kullanrak veri çektiğini anlammak için google bazı korumlar alıyor
        sleep(3)
        erorrMessage=driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/h3')
        testResult=erorrMessage.text == 'HATALI GİRİS'#eğer fonkisyon ise mavi ikon değilse anahtar gelir 
        print(f'TEST SONUCU : {testResult}')
        
        
        
        
        while True:
            continue


testClass=Test_Sauce()
testClass.test_invalid_login()
