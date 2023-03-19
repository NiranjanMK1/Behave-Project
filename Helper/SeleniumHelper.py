from selenium import webdriver
from selenium.webdriver.common.by import By


class SeleniumHelper:
    def __init__(self,driver):
        self.driver = driver

    def open_page(self, page_url):
        self.driver.get(page_url)

    # @staticmethod
    def text_box_entry(self, x_path, value):
        self. driver.find_element(By.XPATH, x_path).send_keys(value)

    # @staticmethod
    def click_button(self, x_path):
        self.driver.find_element(By.XPATH, x_path).click()
