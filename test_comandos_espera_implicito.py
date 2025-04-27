from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://www.hyrtutorials.com/p/waits-demo.html")

bnt_textbox = browser.find_element(By.ID, "btn1")
bnt_textbox.click()

browser.implicitly_wait(12)
textbox = browser.find_element(By.XPATH, "//input[@type='text']")

print("O textbox está em tela!")
