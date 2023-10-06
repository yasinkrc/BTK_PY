from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#driver=webdriver.Chrome(ChhromeDriverManager().install())
driver=webdriver.Chrome()
sleep(1)
driver.maximize_window()
sleep(1)
driver.get("https://www.google.com/")
sleep(1)

input=driver.find_element(By.NAME,"q")
sleep(1)

input.send_keys("kodlama.io")
sleep(2)
searchButton=driver.find_element(By.NAME,'btnK')
sleep(2) 
searchButton.click()
sleep(2)
first_result=driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')
sleep(1)
first_result.click()
listOfCourses=driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlama.io sitesinde şu anda : {len(listOfCourses)} kurs var. ")
# sleep(3)
# searchButton.click()
#Web scraping 
#Data scraping 
#sleep(10)

while True :
    continue