from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import sqlite3
from selenium.webdriver.chrome.options import Options
import numpy as np

nft = np.ones((1470, 6) , np.dtype('U100'))

while 1 ==1 :
  options = Options()

  connector = sqlite3.connect('nft_toned_ape.db')
  cursor = connector.cursor()

  cursor.execute("""CREATE TABLE IF NOT EXISTS test(
         Name_Nft TEXT ,
         number_in_collection TEXT,
         price TEXT,
         owner TEXT,
         photo_adress TEXT
         date TEXT);
      """)
  connector.commit()

  url = "https://beta.disintar.io/collection/UQCzuSjkgUND61l7gIH3NvVWNtZ0RX1hxz1rWnmJqGPmZkMX"


  service1 = Service("/Users\Тимур\PycharmProjects\pythonProject\geckodriver.exe")
  driver = webdriver.Firefox(service = service1)


  html = driver.get(url)

  assert "Disintar - TON NFT marketplace" in driver.title
  while 1 == 1:
      try:
          table = driver.find_element(By.ID, "app")
          table1 = table.find_element(By.CLASS_NAME, 'collection_screen__container___BCDZU')
          table2 = table1.find_element(By.CLASS_NAME, 'nftsContainer__container___22o8R')
          table3 = table2.find_element(By.CLASS_NAME, 'nftsContainer__nftsContainer___1425M')
          table4 = table3
      except Exception:
           driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
      else:
          break

  table = driver.find_element(By.ID, "app")
  table1 = table.find_element(By.CLASS_NAME, 'collection_screen__container___BCDZU')
  table2 = table1.find_element(By.CLASS_NAME, 'nftsContainer__container___22o8R')
  table3 = table2.find_element(By.CLASS_NAME, 'nftsContainer__nftsContainer___1425M')

  table4 = table3

  driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
  print(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()))

  for d in np.arange(1471, dtype=int):
       print(d , time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()))
       while 1:
          try:
              table3.find_elements(By.CLASS_NAME, 'NFTCard__container___2XJg7')[d]

          except Exception:
              driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
          else:
              break
       splits = table3.find_elements(By.CLASS_NAME, 'NFTCard__container___2XJg7')[d].text.split()
       driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
       driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
       if splits[10] =="Collection":
         nft[d][3] = splits[11]
       else:
         nft[d][3] = splits[10]

       nft[d][0] =splits[0]+' '+splits[1]+' '+splits[2]+" "+splits[3]
       nft[d][1] =splits[3].replace('#','')
       nft[d][2] =splits[4]
       nft[d][5] = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
       nft[d][4] = table3.find_elements(By.CLASS_NAME, 'NFTCard__container___2XJg7')[d].find_elements(By.XPATH ,"//div[contains(@class, 'NFTCard__content___28_Xp')]/img")[d].get_attribute('src')
       driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
  print(nft)


  driver.quit()
