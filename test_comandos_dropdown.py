import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://wcaquino.me/selenium/componentes.html")

dropdown_simples = Select(browser.find_element(By.XPATH, "//select[@id='elementosForm:escolaridade']"))
dropdown_simples.select_by_visible_text("Especializacao")
time.sleep(5)

dropdown_multiplo = Select(browser.find_element(By.XPATH, "//select[@id='elementosForm:esportes']"))
dropdown_multiplo.select_by_visible_text("Natacao")
time.sleep(2)
dropdown_multiplo.select_by_visible_text("Corrida")
time.sleep(3)
