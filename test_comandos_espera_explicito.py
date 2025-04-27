from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get("https://www.hyrtutorials.com/p/waits-demo.html")

wait = WebDriverWait(browser, 10)

# textbox is present
browser.find_element(By.ID, "btn1").click()
wait.until(EC.visibility_of_element_located((By.ID, "txt1")))

print("O textbox está em tela!")
