from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
import sqlite3
from selenium.webdriver.firefox.options import Options
import numpy as np

from threading import Thread


while 1 ==1 :
  options = Options()
  options.headless = True
  info_nft = np.array(['','','','','',''], str)
  connector = sqlite3.connect('nft_toned_ape.db')
  cursor = connector.cursor()

  cursor.execute("""CREATE TABLE IF NOT EXISTS list_NFT_APE(
         Name_Nft TEXT ,
         number_in_collection TEXT,
         price TEXT,
         owner TEXT,
         photo_adress TEXT
         date TEXT);
      """)
  connector.commit()

  url = "https://beta.disintar.io/collection/UQCzuSjkgUND61l7gIH3NvVWNtZ0RX1hxz1rWnmJqGPmZkMX"


#  service1 = Service("/Users\Тимур\PycharmProjects\pythonProject\chromedriver.exe")
  service1 = Service("/Users\Тимур\PycharmProjects\pythonProject\geckodriver.exe")
#  driver = webdriver.Chrome(service = service1, options=options)
  driver = webdriver.Firefox(service=service1, options=options)

  html = driver.get(url)

  assert "Disintar - TON NFT marketplace" in driver.title
  while 1 == 1:
      try:
          table = driver.find_element(By.ID , "app")
          table1 = table.find_element(By.CLASS_NAME, 'collection_screen__container___BCDZU')
          table2 = table1.find_element(By.CLASS_NAME, 'nftsContainer__container___22o8R')
          table3 = table2.find_element(By.CLASS_NAME, 'nftsContainer__nftsContainer___1425M')
          table4 = table3
      except Exception:
          driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
      else:
          break

  table = driver.find_element(By.ID , "app")
  table1 = table.find_element(By.CLASS_NAME , 'collection_screen__container___BCDZU')
  table2 = table1.find_element(By.CLASS_NAME , 'nftsContainer__container___22o8R')
  table3 = table2.find_element(By.CLASS_NAME , 'nftsContainer__nftsContainer___1425M')

  table4 = table3

  driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
  print(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()))

  for d in np.arange(0, 1470):
      connector = sqlite3.connect('nft_toned_ape.db')
      cursor = connector.cursor()

      driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
      while 1 == 1:
          try:
              table4 = table3.find_elements(By.CLASS_NAME, 'NFTCard__container___2XJg7')[d]
          except Exception:
              driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
          else:
              break
      table4 = table3.find_elements(By.CLASS_NAME, 'NFTCard__container___2XJg7')[d]
      table5 = table4.find_element(By.CLASS_NAME, 'NFTCard__contentContainer___3iQ7F')
      splits = table4.text.split()
      photo_nft = table5.find_elements(By.XPATH, "//div[contains(@class, 'NFTCard__content___28_Xp')]/img")[
          d].get_attribute('src')
      if splits[10] == "Collection":
          owner_nft = splits[11]
      else:
          owner_nft = splits[10]
      info_nft[0] = splits[0] + ' ' + splits[1] + ' ' + splits[2] + " " + splits[3]
      info_nft[1] = splits[3].replace('#', '')
      info_nft[2] = splits[4]
      info_nft[3] = owner_nft
      cursor.execute(
          "SELECT * FROM list_NFT_APE WHERE (Name_Nft= ?) AND (number_in_collection= ?) AND (price= ?) AND (owner= ?)",
          (
              splits[0] + ' ' + splits[1] + ' ' + splits[2] + " " + splits[3], splits[3].replace('#', ''), splits[4],
              owner_nft,))
      yess = cursor.fetchall()
      print(d, time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()))

      if not bool(len(yess)):
          print(1)
          cursor.execute("INSERT INTO list_NFT_APE VALUES(?, ?, ?, ?,?,?)", (
              splits[0] + ' ' + splits[1] + ' ' + splits[2] + " " + splits[3], splits[3].replace('#', ''), splits[4],
              owner_nft,
              table5.find_elements(By.XPATH, "//div[contains(@class, 'NFTCard__content___28_Xp')]/img")[
                  d].get_attribute(
                  'src'), time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())))
      connector.commit()
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")


  driver.quit()


