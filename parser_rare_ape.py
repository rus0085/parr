from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import sqlite3
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
info_nft = ['','','','','','','','','','','','','','',]
connector = sqlite3.connect('nft_toned_ape.db')
cursor = connector.cursor()

url = "https://nftstatistic.com/tonedapeclub"


service1 = Service("/Users\Тимур\PycharmProjects\pythonProject\chromedriver.exe")
driver = webdriver.Chrome(service = service1, options=options)


html = driver.get(url)

time.sleep(2)


table = driver.find_element(By.XPATH , "//div[contains(@class, 'bg-white')] ")
table1 = table.find_element(By.CLASS_NAME , 'bg-white')
table2 = table1.find_element(By.XPATH , "//main[contains(@class, 'max-w-7xl mx-auto px-4 sm:px-6 lg:px-8')] ")
table3 = table2.find_element(By.XPATH , "//div[contains(@class, 'grid grid-cols-1 lg:grid-cols-4 gap-x-8 gap-y-10')] ")
table4 = table3.find_element(By.XPATH , "//div[contains(@class, 'lg:col-span-3')] ")
table5 = table4.find_element(By.XPATH , "//div[contains(@class, 'bg-white')] ")
table6 = table5.find_element(By.XPATH , "//div[contains(@class, 'max-w-2xl mx-auto py-4 px-4 sm:py-6 sm:px-6 lg:max-w-7xl lg:px-8')] ")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

for d in range(1470):

      driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

      table7 = table6.find_elements(By.XPATH , "//div[contains(@class, 'group relative bg-white border border-gray-200 rounded-lg flex flex-col overflow-hidden')] ")[d]
      print(table7.text)
      splits = table7.text.split()
      cursor.execute("INSERT INTO options_ape VALUES(?, ?, ?, ?,?,?,?,?,?,?,?,?,?,?)", (splits[4].replace('#', ''),splits[0],splits[6],splits[8],splits[10],splits[12],splits[14],splits[16],splits[18],splits[20],splits[22],splits[25],splits[28],splits[30]))
      connector.commit()
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

driver.quit()


