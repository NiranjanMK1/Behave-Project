import time

from selenium import webdriver
def before_scenario(context,scenario):
    print("chrome driver executed")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def after_scenario(context,scenario):
     print("Chrome Driver Closed")
     context.driver.close()