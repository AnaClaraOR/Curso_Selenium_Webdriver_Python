import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()

browser.get("https://seubarriga.wcaquino.me/login")

# find_element()
# Username = browser.find_element(By.ID, "email")
# Password = browser.find_element(By.ID, "senha")

# send_keys
# Username.send_keys("teste.selenium@email.com")
# Password.send_keys("12345")

auth_fields = browser.find_elements(By.XPATH, "//*[@class='form-control']")
print(auth_fields)
print(len(auth_fields))

time.sleep(3)
browser.quit()

# find_elements()
