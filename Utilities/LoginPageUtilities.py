import time
from selenium.webdriver.common.by import By
from Locators.LoginPageLocators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conftest import *

class LoginPageFunctions:

    def account_button(self):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_icon)))
        driver.find_element(By.CSS_SELECTOR, account_icon).click()


    def sign_in(self):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, sign_in_button)))
        driver.find_element(By.CSS_SELECTOR, sign_in_button).click()

    def fill_username(self, correct_number):
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, number_field)))
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, number_field).send_keys(correct_number)

    def submit_button(self):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, submit_button)))
        driver.find_element(By.CSS_SELECTOR, submit_button).click()

    def fill_otp(self):
        time.sleep(20)
        driver.find_element(By.CSS_SELECTOR, verify_otp).click()

    def perform_login(self,correct_number):
        self.fill_username(correct_number)
        self.submit_button()
        self.fill_otp()

