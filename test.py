from os.path import abspath
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service(abspath('./geckodriver.exe'))
browser = webdriver.Firefox(service=s)

browser.get('https://www.google.com.tw/')

elem = browser.find_element(By.CLASS_NAME, value='gLFyf')
elem.send_keys('龍華科技大學' + Keys.RETURN)

wait = WebDriverWait(browser, 10)

try:
  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div#search')))
  result = browser.find_elements(By.CSS_SELECTOR, "div#search a[href^='https://']")
  # TODO: 遍歷取出資料
  oneItem = result[0]
  print(oneItem.text)
except TimeoutException:
  print('等待逾時！')
finally:
  browser.quit()


# browser.close()