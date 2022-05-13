from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests
import time

url = "https://beta.disintar.io/marketplace"


service1 = Service("/Users\Тимур\PycharmProjects\pythonProject\chromedriver.exe")
driver = webdriver.Chrome(service = service1)


html = driver.get(url)

assert "Disintar - TON NFT marketplace" in driver.title
time.sleep(1)
elem=driver.find_element(By.CLASS_NAME, 'marketplace_screen__variant___25Ulb')
elem.click()
time.sleep(4)
table = driver.find_element(By.ID , "app")
table1 = table.find_element(By.CLASS_NAME , 'marketplace_screen__container___wVbzs')
table2 = table1.find_element(By.CLASS_NAME , 'nftsContainer__container___22o8R')
table3 = table2.find_element(By.CLASS_NAME , 'nftsContainer__nftsContainer___1425M')

time.sleep(2)

for i in range(100):
  y=0
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
  y+=1080
  for d in range(1):
    table4 = table3.find_elements(By.CLASS_NAME, 'NFTCard__container___2XJg7')[i]
    table5 = table4.find_element(By.CLASS_NAME, 'NFTCard__contentContainer___3iQ7F')
    photo = table5.find_element(By.XPATH ,"//div[contains(@class, 'NFTCard__content___28_Xp')]/img").get_attribute('src')
    print(table4.text)
    print(photo)




while 1 == 1 :
  assert "No results found." not in driver.page_source
