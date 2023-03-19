from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Helper.SeleniumHelper import SeleniumHelper
from locators import locators
from TestData import login_details

import time
log_url = r"https://www.facebook.com/"

@given(u'User on the login page')
def step_impl(context):
    SeleniumHelper(context.driver).open_page(log_url)
    print("face book page is opend")



@when(u'user input incorrect credentials')
def step_impl(context):
    SeleniumHelper(context.driver).text_box_entry(locators.input_field_login, login_details.correct_login_id )
    SeleniumHelper(context.driver).text_box_entry(locators.input_field_password, login_details.incorrect_login_password)
    SeleniumHelper(context.driver).click_button(locators.login_button)
    time.sleep(10)
    # context.driver.find_element(By.XPATH, "//input[@name = 'email']").send_keys("niranjan1111@gmail.com")
    # context.driver.find_element(By.XPATH, "//input[@name = 'pass']").send_keys("niranjan1111@gmail.com")
    # context.driver.find_element(By.XPATH, "//button[@name = 'login']").click()


@then(u'Error message will come')
def step_impl(context):
    try:

        element = WebDriverWait(context.driver,5).until(EC.presence_of_element_located(
            (By.XPATH, r"//div[@class='_9ay7']//a[contains(text(),'Forgotten password?')]")))
        print("test_passed")
    finally:
        print("test_failed")