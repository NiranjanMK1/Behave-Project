from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get(r"https://www.facebook.com/")
driver.find_element(By.XPATH,"//input[@name = 'email']").send_keys("niranjan1111@gmail.com")
driver.find_element(By.XPATH,"//input[@name = 'pass']").send_keys("niranjan1111@gmail.com")
driver.find_element(By.XPATH,"//button[@name = 'login']").click()

try:

    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,r"//div[@class='_9ay7']//a[contains(text(),'Forgotten password?')]")))
    print("test_passed")
finally:
    driver.quit()