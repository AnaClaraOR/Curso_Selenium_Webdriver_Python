import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://wcaquino.me/selenium/componentes.html")

iframe1 = browser.find_element(By.ID, "frame1")
browser.switch_to.frame(iframe1)
bnt_iframe1 = browser.find_element(By.ID, "frameButton")
bnt_iframe1.click()
time.sleep(3)

#muda para a página principal para entrar em um novo frame
#não foi realizado devido alerta
# browser.switch_to.default_content()

#dados do novo frame
# iframe2 = browser.find_element(By.ID, "frame2")
# browser.switch_to.frame(iframe2)
# bnt_iframe2 = browser.find_element(By.ID, "frameButton")
# bnt_iframe2.click()
# time.sleep(3)
